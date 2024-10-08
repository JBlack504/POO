from rest_framework import serializers
from.models import  UsuarioPersonalizado,EmpresaDB, OfertaDB,ResenasDB, Habilidades 

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioPersonalizado
        fields = ['id', 'nombre', 'correo']
        
        
class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpresaDB
        fields = '__all__'

class OfertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfertaDB
        fields = '__all__'
        
class ResenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResenasDB
        fields = '__all__'

class HabilidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habilidades
        fields = '__all__'