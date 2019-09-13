from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Solicitud

class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'creado_por',
            'nombre',
            'script',
            'descripcion',
            'fecha_creacion',
        )
        model = Solicitud

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'username',
        )
        model = get_user_model()