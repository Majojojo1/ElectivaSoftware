from django.urls import path
from general import views


app_name = 'general'
urlpatterns = [
    #LOGING Y VISTA DE ADMINISTRADOR, REGISTRO DE USUARIOS Y ENVIO DE VERIFICACIÓN 
    path('', views.inicio, name='inicio'),

    
    #VISTA DE ESTUDIANTE, PROFESOR, COORDINADOR DE TRABAJO DE GRADO Y PRACTICAS
    #JURADO, ADVISOR, DIRECTOR DE TRABAJO DE GRADO, ASESOR DE TRABAJO DE GRADO
    
    
    #ENVIO DE CORREO 

]

