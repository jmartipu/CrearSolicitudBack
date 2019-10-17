import json

from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Solicitud, Herramienta, Aplicacion, TipoPrueba, TipoEjecucion
from rest_framework_jwt.settings import api_settings
from crear_solicitudes_proyecto import settings
import boto3
import logging

logger = logging.getLogger(__name__)


class SolicitudSerializer(serializers.ModelSerializer):
    creado_por = serializers.SlugRelatedField(
        queryset=get_user_model().objects.all(),
        slug_field='username'
    )
    class Meta:
        fields = (
            'id',
            'nombre',
            'aplicacion',
            'herramienta',
            'tipo_prueba',
            'tipo_ejecucion',
            'pruebas',
            'descripcion',
            'creado_por',
            'fecha_creacion',
        )
        model = Solicitud

    def save(self, **kwargs):
        super(SolicitudSerializer, self).save()
        sqs = boto3.client('sqs')
        queue_url = settings.SQS_QUEUE_URL
        response = sqs.send_message(
            QueueUrl=queue_url,
            DelaySeconds=10,
            MessageAttributes={
                'Herramienta': {
                    'DataType': 'String',
                    'StringValue':  Herramienta.objects.filter(pk=self.data['herramienta'])[0].nombre
                },
                'VersionHerramienta': {
                    'DataType': 'String',
                    'StringValue': Herramienta.objects.filter(pk=self.data['herramienta'])[0].version
                },
                'Aplicacion': {
                    'DataType': 'String',
                    'StringValue': Aplicacion.objects.filter(pk=self.data['aplicacion'])[0].nombre
                },
                'TipoPrueba': {
                    'DataType': 'String',
                    'StringValue': TipoPrueba.objects.filter(pk=self.data['tipo_prueba'])[0].tipo_prueba
                }
                ,
                'TipoEjecucion': {
                    'DataType': 'String',
                    'StringValue': TipoEjecucion.objects.filter(pk=self.data['tipo_ejecucion'])[0].tipo_ejecucion
                }
            },
            MessageBody=json.dumps(self.data)

        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'username',
        )
        model = get_user_model()


class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = get_user_model()
        fields = ('token', 'username', 'password')

