from email import message
from pyexpat.errors import messages
from django.shortcuts import render, redirect

from general.models import usuario

# Create your views here.
#VISTA DEL INICIO DE LA PLATAFORMA DONDE EL USUARIO INGRESARA LAS CREDENCIALES
def inicio(request):
    return render(request, 'html/login.html')