from django.shortcuts import render, redirect#Importamos las Funciones "render"
from django.views.generic import TemplateView#Importamos las Funciones "TemplateView"
from django.contrib.auth.decorators import login_required#Importa la Funcion de "login_required"
#from Base_Global.forms import GlobalForm
from Base_Global.models import EstadoMensual
from django.http import HttpResponse
from django.db.models import Q
from Base_User.decorators import allowed_users
from Base_Global.filters import Filtro_EstadoAWY

# Create your views here.
@login_required
@allowed_users(allowed_roles=['Director', 'Anfitrion'])
def Registro_Mensual(request):
	Lst_Estado=EstadoMensual.objects.all()
	Filtro_Estado = Filtro_EstadoAWY(request.GET, queryset=Lst_Estado)
	Lst_Estado = Filtro_Estado.qs
	context = {
		"Lista_HTML":Lst_Estado,
		'Filtro':Filtro_EstadoAWY
	}
	return render(request,"Registro_Estado.html", context)