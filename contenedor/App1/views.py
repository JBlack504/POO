from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def IndexView(request):
    #esto es la pagina principal
    return HttpResponse(" Sekai Konnichiwa")
