from django.shortcuts import render
from django.urls import path
from . import views


urlpatterns = [
 path ('', views.index, name='index'),
 path('listar_passeios' , views.listar_passeios, name='listar_passeios'),
 path('incluir_passeios' , views.incluir_passeios, name='incluir_passeios'),
 path('alterar_passeio/<int:codigo>',views.alterar_passeio , name='alterar_passeio'),
 path('excluir_passeio/<int:codigo>', views.excluir_passeio, name='excluir_passeio'),
 ]

