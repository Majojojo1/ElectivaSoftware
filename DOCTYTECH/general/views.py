from email import message
from multiprocessing import context
from pyexpat.errors import messages
from django.shortcuts import render, redirect

from general.models import superUser, usuario 

# Create your views here.
#VISTA DEL INICIO DE LA PLATAFORMA DONDE EL USUARIO INGRESARA LAS CREDENCIALES
def login(request):
    return render(request, 'html/login.html')

def principal(request):
    correo = request.POST.get('email')
    contra = request.POST.get('psw')
    #AUTENTICACIÓN DE USUARIO
    correo_query = superUser.objects.filter(correoUser = correo)
    contra_query = superUser.objects.filter(contraUser = contra)
    if correo_query.exists() and contra_query.exists():
        id = superUser.objects.get(correoUser = correo)
        return opPrincipal(request, id.correoUser)
    else:
        return noExist(request)

def noExist(request):
    return render(request, 'html/login.html')

def opPrincipal(request,id):
    context = {}
    if id == 0:
        context['email'] = 'no'
        context['psw'] = 'no'
    #else:
     #   estudiante = usuario.objects.filter(rol = estudiante.objects.get(rol='estudiante'))
      #  super = superUser.objects.get(id = id)
       # context['email'] = super.correoUser
        #context['psw'] = super.contraUser
        #if estudiante.exists():
         #   context['estudi'] = estudiante
        #else:
         #   context ['no_estudiante'] = 'No hay estudiantes registrados'                
    return render(request, 'html/inicio.html', context)


def regisSuperUser(request):
    return render(request, 'html/registrarSuperUser.html')


def agregarUsuario(request):
    return render(request, 'html/agregarNuevoUser.html')

def personal(request):
    return render(request, 'html/verPersonal.html')

def agregandoUsuario(request):
    codigo = request.POST.get('codigoU')
    name = request.POST.get('nameU')
    email = request.POST.get('emailU')
    password = request.POST.get('psw')
    psw_repeat = request.POST.get('psw-repeat')
    progrma = request.POST.get('facultad')
    rolUsu = request.POST.get('rol')
    
    nuevo_usuario = usuario(codigoUsuario = codigo, nombre = name, correoUsu = email, contrasena = password, programa = progrma, rol =rolUsu)
    nuevo_usuario.save()
    id = nuevo_usuario.codigoUsuario
    return opPrincipal(request,id)

def agregandoSuperUser(request):
    email = request.POST.get('email')
    nombreSuper = request.POST.get('name')
    password = request.POST.get('psw')
    psw_repeat = request.POST.get('psw-repeat')
    
    nuevo_super = superUser(correoUser = email, nombreUser = nombreSuper, contraUser = password)
    nuevo_super.save()
    id = nuevo_super.correoUser
    return opPrincipal(request, id)