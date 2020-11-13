from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView

def CrearUsuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            residencia = form.cleaned_data.get('residencia')
            user = authenticate(username=username, password=raw_password, residencia=residencia)
            login(request, user)
            return redirect("Inicio.html")
    else:
        form = UsuarioForm()
    return render(request, 'CrearUsuarios.html',{'form': form})


def Lista_Usuarios(request):
	Lst_User=User.objects.all()
	return render(request,"Lista_User.html",{"Lista_HTML":Lst_User})

# Create your views here.
