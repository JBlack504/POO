from rest_framework import viewsets
from django.shortcuts import render
from django.http import HttpResponse
from .serializers import UsuarioSerializer, EmpresaSerializer,OfertaSerializer,HabilidadSerializer, ResenaSerializer
from .models import UsuarioPersonalizado, EmpresaDB, OfertaDB, Habilidades, ResenasDB

# Create your views here.
def IndexView(request):
    #esto es la pagina principal
    return HttpResponse(" Sekai Konnichiwa")

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = UsuarioPersonalizado.objects.all()
    serializer_class = UsuarioSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = EmpresaDB.objects.all()
    serializer_class = EmpresaSerializer
    
class OfertaViewSet(viewsets.ModelViewSet):
     queryset = OfertaDB.objects.all()
     serializer_class = OfertaSerializer
     
class HabilidadViewSet(viewsets.ModelViewSet):
    queryset = Habilidades.objects.all()
    serializer_class = HabilidadSerializer
    
class ResenaViewSet(viewsets.ModelViewSet):
    queryset = ResenasDB.objects.all()
    serializer_class = ResenaSerializer