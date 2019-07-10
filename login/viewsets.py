from rest_framework import viewsets

from .models import InicioSesion
from .serializer import InicioSesionSerializer

class InicioSesionViewSet(viewsets.ModelViewSet): 
    serializer_class= InicioSesionSerializer
