from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Prueba
from .forms import PruebaForm
# Create your views here.

class IndexView(TemplateView):
    template_name = "home/home.html"

class ResumenFoundationView(TemplateView):
    template_name = "home/resumenfoundationview.html"

class PruebaListView(ListView):
    template_name = "home/lista.html"
    queryset = ['A', 'B', 'C', 'D']
    context_object_name = 'lista_prueba'


class ModeloPruebaListView(ListView):
    model = Prueba
    template_name = "home/pruebas.html"
    context_object_name = 'lista_prueba'


class PruebaCreateListView(ListView):
    template_name = "home/add.html"
    model = Prueba
    form_class = PruebaForm
    success_url = '/'
    
