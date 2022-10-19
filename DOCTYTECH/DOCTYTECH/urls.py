from django.urls import path
from general import views


app_name = 'general'
urlpatterns = [
    #LOGING, REGISTRO DE SUPER USER, VISTA SUPER USUARIO
    path('', views.login, name='login'),
    path('Principal/', views.principal, name='principal'),
    path('opPrincipal/<int:_id>', views.opPrincipal, name='opPrincipal'),
    path('Principal/Registro/', views.regisSuperUser, name='registro'),
    path('Principal/AgregarUsuario/', views.agregarUsuario, name='agregar_usuario'),
    path('Principal/Personal/', views.personal, name='ver_personal'),
    path('seCreoUsuario/', views.agregandoUsuario, name='agregandoUsuario'),
    path('seCreoAdministrador/', views.agregandoSuperUser, name='agregandoSuperUser'),
    


    #ENVIO DE CORREO 

]

