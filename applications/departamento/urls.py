from django.contrib import admin
from django.urls import path
from . import views

app_name = 'departamento_app'

urlpatterns = [
    path(
        'new-departamento/',
        views.newDepartamentoView.as_view(),
        name='nuevo-departamento'
        ),    
    path(
        'listar-departamento/',
        views.ListarDepartamentoView.as_view(),
        name='listar_departamento'
        ),  
]

