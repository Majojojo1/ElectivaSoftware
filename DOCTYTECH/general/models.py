from datetime import timezone
from django.db import models

# Create your models here.

#MODEL SUPER USUARIO 
class superUser(models.Model):
    correoUser = models.CharField(primary_key=True, max_length= 50, null=False)
    nombreUser = models.CharField(max_length=100, null=False)
    contraUser = models.CharField(max_length= 15, null=False)

#MODEL DEL REGISTRO DE USUARIO (PROFESORES Y ESTUDIANTE)
class usuario(models.Model): 
    codigoUsuario = models.CharField(primary_key=True, max_length=11, null=False)
    nombre = models.CharField(max_length=100)
    correoUsu = models.EmailField(max_length= 50, null=False)
    contrasena = models.CharField(max_length= 15, null=False)
    programa = models.CharField(max_length=100, null = False)
    rol = models.CharField(max_length=13, null=False, default='Estudiante')