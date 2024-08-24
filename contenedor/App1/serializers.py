from rest_framework import serializers
from.models import  EmpleadorDB, OfertaDB,ResenasDB, Habilidades 


class EmpleadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpleadorDB
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