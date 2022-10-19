from email import message
from pyexpat.errors import messages
from django.shortcuts import render, redirect

from general.models import superUser

# Create your views here.
#VISTA DEL INICIO DE LA PLATAFORMA DONDE EL USUARIO INGRESARA LAS CREDENCIALES
def login(request):
    return render(request, 'html/login.html')

def principal(request):
    return render(request, 'html/inicio.html')


def regisSuperUser(request):
    return render(request, 'html/registrarSuperUser.html')


def agregarUsuario(request):
    return render(request, 'html/agregarNuevoUser.html')

def personal(request):
    return render(request, 'html/verPersonal.html')

def agregandoUsuario(request):
    return render(request, 'html/agregarNuevoUser.html')

def agregandoSuperUser(request):
    
    return render(request, 'html/registrarSuperUser.html')