from django.urls import path
from general import views


app_name = 'general'
urlpatterns = [
    #LOGING, REGISTRO DE SUPER USER, VISTA SUPER USUARIO
    path('', views.login, name='login'),
    path('Principal/', views.principal, name='principal'),
    path('Registro/', views.regisSuperUser, name='registro'),
    path('AgregarUsuario/', views.agregarUsuario, name='agregar_usuario'),
    path('Personal/', views.personal, name='ver_personal'),
    path('seCreoUsuario/', views.agregandoUsuario, name='agregandoUsuario'),
    path('seCreoAdministrador/', views.agregandoSuperUser, name='agregandoSuperUser'),
    #Hola bobis xd 


    #ENVIO DE CORREO 

]

