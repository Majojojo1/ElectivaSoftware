from datetime import timezone
from django.db import models

# Create your models here.
#MODEL DEL REGISTRO DE USUARIO (ADMINISTRADOR Y ESTUDIANTE)
class usuario(models.Model): 
    codigoUsuario = models.CharField(primary_key=True, max_length=11, null=False, default= '300000')
    nombre = models.CharField(max_length=100)
    correoUsu = models.EmailField(max_length= 50, null=False)
    contrasena = models.CharField(max_length= 15, null=False)
    programa = models.CharField(max_length=100)
    programa2 = models.CharField(max_length=100, default= 'Sin segundo programa')
    rol = models.CharField(max_length=13, null=False, default='Seleccione su rol')
    
    def __str__(self):
        return "{0}".format(self.codigoUsuario)

#MODEL DEL DOCUMENTO
class documento(models.Model): 
    idDoc = models.CharField(primary_key=True, max_length=30, null=False)
    tipoDocumento = models.CharField(max_length=50, null=False)
    rutaDoc = models.CharField(max_length=200, null=False)

#MODEL DE ENVIO DE DOCUMENTO/DOCUMENTOS
class enviar(models.Model): 
    idEnvio = models.CharField(primary_key=True, max_length=30, null=False, default= '0000000')
    codigoUsuario = models.CharField(max_length=11, null=False)
    idDoc = models.CharField(max_length=30, null=False)
    destinatario = models.CharField(max_length=100, null=False)
    emisario = models.CharField(max_length=100, null=False)
    #fecha = models.DateTimeField(default=timezone.now) REVISAR
    mensaje = models.TextField(max_length=1000)
    etiqueta = models.CharField(max_length=50, null=False)
    
    def __str__(self):
        return "{0}".format(self.etiqueta)

#MODEL DE LA COLECCIÓN DE DOCUMENTOS
class coleccion(models.Model): 
    idColec = models.CharField(primary_key=True, max_length=30, null=False)
    idEnvio = models.CharField(max_length=30, null=False)
    
#MODEL DEL REPORTE QUE EL ADMINISTRADOR DEBE REALIZAR
class reporte(models.Model): 
    idReporte = models.CharField(primary_key=True, max_length=30, null=False)
    idColec = models.CharField(max_length=30, null=False)
    idEnvio = models.CharField(max_length=30, null=False)
    descripcion = models.TextField(max_length=1000, null=False) 