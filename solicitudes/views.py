from rest_framework import generics
from .models import Solicitud
from .serializers import SolicitudSerializer

# Create your views here.


class SolicitudList(generics.ListCreateAPIView):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer

class SolicitudDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Solicitud.objects.all()
    serializer_class = SolicitudSerializer