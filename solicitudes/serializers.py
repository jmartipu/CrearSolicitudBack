import json

from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Solicitud, Herramienta, Aplicacion, TipoPrueba, TipoEjecucion, Ejecutor, Prueba, TipoAplicacion
from rest_framework_jwt.settings import api_settings
from crear_solicitudes_proyecto import settings
import boto3
import logging

logger = logging.getLogger(__name__)


class TipoPruebaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'tipo_prueba')
        model = TipoPrueba


class TipoEjecucionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'tipo_ejecucion', 'tipo_prueba')
        model = TipoEjecucion


class TipoAplicacionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'tipo_aplicacion')
        model = TipoAplicacion

class EjecutorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'ejecutor', 'version')
        model = Ejecutor


class AplicacionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'nombre', 'tipo_aplicacion', 'link', 'version', 'creado_por')
        model = Aplicacion


class HerramientaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'nombre', 'tipo_aplicacion', 'link', 'ejecutor', 'alto_pantalla', 'ancho_pantalla', 'creado_por')
        model = Herramienta


class PruebaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'nombre', 'aplicacion', 'tipo_prueba', 'script', 'descripcion', 'creado_por')
        model = Prueba


class SolicitudSerializer(serializers.ModelSerializer):
    pruebas = PruebaSerializer(many=True)
    tipo_ejecucion = TipoEjecucionSerializer()
    herramienta = HerramientaSerializer()
    aplicacion = AplicacionSerializer()
    tipo_prueba = TipoPruebaSerializer()
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
                'Id': {
                    'DataType': 'String',
                    'StringValue': str(self.data['id'])
                },
                'NombreAplicacion': {
                    'DataType': 'String',
                    'StringValue': Aplicacion.objects.filter(pk=self.data['aplicacion'])[0].nombre
                },
                'VersionAplicacion': {
                    'DataType': 'String',
                    'StringValue': Aplicacion.objects.filter(pk=self.data['aplicacion'])[0].version
                },
                'NombreHerramienta': {
                    'DataType': 'String',
                    'StringValue':  Herramienta.objects.filter(pk=self.data['herramienta'])[0].nombre
                },
                'NombreEjecutor': {
                    'DataType': 'String',
                    'StringValue': Herramienta.objects.filter(pk=self.data['herramienta'])[0].ejecutor.ejecutor
                },
                'VersionEjecutor': {
                    'DataType': 'String',
                    'StringValue': Herramienta.objects.filter(pk=self.data['herramienta'])[0].ejecutor.version
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

