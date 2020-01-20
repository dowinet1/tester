from django.conf.urls import url,include
from django.contrib import admin
from . import views
from django.urls import path, re_path


urlpatterns = [
    
    path('', views.index),
    path('iniciosesion/', views.iniciosesion),
    path('cerrarsesion/', views.cerrarsesion),
    path('testuno/', views.testuno),
    path('registro/', views.register),
    path('registasp/', views.regist),
    path('registroalu/', views.registro),
    path('perfil/', views.perfil),
    path('test_aptitudes/', views.aptitu),
    path('test_intereses/', views.inte),
    path('lista/', views.lista),
    path('resultado/', views.resultado),
]