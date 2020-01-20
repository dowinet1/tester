from django.shortcuts import render, redirect
from django.utils import timezone
from .models import *
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import JsonResponse, HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import login, authenticate, logout
from django.core.mail import EmailMessage
from django.conf import settings
from django.core import serializers
from django.contrib.auth.hashers import check_password
from django.views.generic import CreateView

import json
import smtplib
import sweetify
import datetime

# Create your views here.

#
def index(request):

    # return render(request, 'login.html',{})
    usuario = request.user
    if usuario.is_active:
        return render (request, 'index.html', {})
    else:
        return render(request, 'login.html',{})


# LOGIN Y CERRAR SESION
def iniciosesion(request):
    username = request.POST.get("usuario")
    password = request.POST.get("password")
    print("Esto llego: ", username)
    try: 
        username = authenticate(request, username=username, password=password)
        login(request,username)
        return redirect('/')
    except Exception as e:
        sweetify.error(request, 'Oops!', text='¡El Usuario y/o Contraseña es Incorrecto!', persistent=':´(')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def cerrarsesion(request):
	logout(request)
	return HttpResponseRedirect("/")

from django.contrib.auth.forms import UserCreationForm

# ...

def register(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/')

    # Si llegamos al final renderizamos el formulario
    return render(request, "registro.html", {'form': form})
def recu(request):
    #recuperar contraseña
    return render(request, "recupassword.html")

def testuno(request):
    #testunoio
    return render(request, "intereses.html")

def inicio(request):
    #inicio de la pagina
    return render(request, "inicio.html")

def regist(request):
    #register de aspirantes
    return render(request, "register.html")
def registro(request):
    #register de alumno
    return render(request, "registeralu.html")
def perfil(request):
    #perfil de alumno, aspirante,jefa,sicologo
    return render(request, "perfil.html")
def aptitu(request):
    #test de aptitudes
    return render(request, "testapti.html")
def inte(request):
    #test de intereses 
    return render(request, "testinte.html")
def lista(request):
    #lista de alumnos y aspirantes registrados
    return render(request, "lista.html")
def resultado(request):
    #test de intereses 
    return render(request, "resultado.html")