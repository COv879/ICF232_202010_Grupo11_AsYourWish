from django.shortcuts import render, redirect#Importamos las Funciones "render"
from django.views.generic import TemplateView#Importamos las Funciones "TemplateView"
from django.contrib.auth.decorators import login_required#Importa la Funcion de "login_required"
from Base_Profesor.forms import ProfesorForm
from Base_Profesor.models import Profesor
from django.http import HttpResponse
from django.db.models import Q
from Base_Profesor.filters import Filtro_Profesor
from Base_User.decorators import allowed_users
# Create your views here.

@login_required
@allowed_users(allowed_roles=['Director', 'Anfitrion'])
def Lista_Profesores(request):
	Lst_Profesor=Profesor.objects.all().order_by('NombreProf')
	Filtro_Profe = Filtro_Profesor(request.GET, queryset=Lst_Profesor)
	Lst_Profesor = Filtro_Profe.qs
	context = {"Lista_HTML":Lst_Profesor, "Filtro":Filtro_Profe}
	return render(request,"Lista_Profesor.html",context)


@login_required
@allowed_users(allowed_roles=['Director'])
def Registrar_Profesores(request):
	data={
		'form': ProfesorForm()
	}
	if request.method == 'POST':
		Profe= ProfesorForm(request.POST)
		if  Profe.is_valid():
			Profe.save()
			data['mensaje']="Registro Completado"
		else:
			data['mensaje']="Ocurrio un ERROR al Registrar"
	return render(request,"Registrar_Profesor.html", data)



@login_required
@allowed_users(allowed_roles=['Director'])
def Modificar_Profesores(request, id):
	Profe= Profesor.objects.get(id=id)
	data={
		'form':ProfesorForm(instance=Profe)
	}

	if request.method=='POST':
		formulario =  ProfesorForm(data=request.POST, instance=Profe)
		if formulario.is_valid():
			formulario.save()
			data['mensaje']="Modificacion Completada"
			data['form']=formulario
		else:
			data['mensaje']="Ocurrio un ERROR al Modificar"
	return render(request,"Modificar_Profesor.html", data)



@login_required
@allowed_users(allowed_roles=['Director'])
def Eliminar_Profesores(request, id):
	Profe=Profesor.objects.get(id=id)
	Profe.delete()
	return redirect("/Listado_Profesores/")

