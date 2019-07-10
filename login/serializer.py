from rest_framework import serializers 
from .models import InicioSesion

class InicioSesionSerializer(serializers.ModelSerializer):
    class Meta: 
        model = InicioSesion
        fields = '__all__'
        
