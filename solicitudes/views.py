from rest_framework import permissions, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from solicitudes.models import Prueba, TipoEjecucion, TipoPrueba, TipoAplicacion, Ejecutor, Aplicacion, Herramienta
from .models import Solicitud
from .serializers import SolicitudSerializer, UserSerializer, UserSerializerWithToken, PruebaSerializer, \
    TipoPruebaSerializer, TipoEjecucionSerializer, TipoAplicacionSerializer, EjecutorSerializer, AplicacionSerializer, \
    HerramientaSerializer
from django.contrib.auth import get_user_model

# Create your views here.

@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """

    serializer = UserSerializer(request.user)
    return Response(serializer.data)


class HerramientaViewsets(viewsets.ModelViewSet):
    queryset = Herramienta.objects.all()
    serializer_class = HerramientaSerializer


class AplicacionViewsets(viewsets.ModelViewSet):
    queryset = Aplicacion.objects.all()
    serializer_class = AplicacionSerializer


class EjecutorViewsets(viewsets.ModelViewSet):
    queryset = Ejecutor.objects.all()
    serializer_class = EjecutorSerializer


class TipoAplicacionViewsets(viewsets.ModelViewSet):
    queryset = TipoAplicacion.objects.all()
    serializer_class = TipoAplicacionSerializer


class TipoEjecucionViewsets(viewsets.ModelViewSet):
    queryset = TipoEjecucion.objects.all()
    serializer_class = TipoEjecucionSerializer


class TipoPruebaViewsets(viewsets.ModelViewSet):
    queryset = TipoPrueba.objects.all()
    serializer_class = TipoPruebaSerializer


class PruebaViewsets(viewsets.ModelViewSet):
    queryset = Prueba.objects.all()
    serializer_class = PruebaSerializer



class SolicitudViewsets(viewsets.ModelViewSet):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @classmethod
    def get_extra_actions(cls):
        return []
