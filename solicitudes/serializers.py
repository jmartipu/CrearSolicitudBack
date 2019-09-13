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