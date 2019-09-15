from rest_framework import permissions, viewsets
from .models import Solicitud
from .serializers import SolicitudSerializer, UserSerializer
from django.contrib.auth import get_user_model

# Create your views here.


class SolicitudViewsets(viewsets.ModelViewSet):
    allowed_methods = ['get', 'post', 'put', 'delete', 'options']
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer


class UserViewSet(viewsets.ModelViewSet):
    allowed_methods = ['get', 'post', 'put', 'delete', 'options']
    permission_classes = (permissions.IsAdminUser,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
