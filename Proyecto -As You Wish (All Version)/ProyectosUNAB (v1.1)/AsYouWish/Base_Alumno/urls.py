from django.conf.urls import url#Importamos las Funciones "url"
from django.urls import path, include#Importamos las Funciones de "Path" & "Include"
from Base_Alumno import views #Importamos las Vistas(views.py) que se encuentran en Base_Alumno

urlpatterns=[
url('Listado_Alumnos/', views.Lista_Pag),#Creamos un nuevo URL para nuestra Pagina
url('Registrar_Alumnos/', views.Registrar_Pag),#URL con el Formulario de Registro
path('Modificar_Alumno/<id>/', views.Modificar_Pag),
path('Eliminar_Alumno/<id>/', views.Eliminar_Pag),
url('buscar/', views.BuscarAlumnos),
]