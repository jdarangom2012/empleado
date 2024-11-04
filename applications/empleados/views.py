from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from .models import Persona
from django.urls import reverse_lazy
from .forms import EmpleadoForms

# Create your views here.
class InicioView(TemplateView):
    """Vista que carga la pagina de Inicio"""
    template_name = 'inicio.html'
    

class ListAllEmpleados(ListView):
    template_name = 'empleado/list_all_empleados.html'
    paginate_by = 4
    ordering = 'fist_name'
    context_object_name = 'Persona'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        lista =  Persona.objects.filter(
            full_name__icontains=palabra_clave
        )        
        return lista

class ListByAreaEmpleados(ListView):
    template_name = 'empleado/list_by_area_empleados.html'
    context_object_name = 'list_by_area_empleados'
  
    def get_queryset(self):
        area = self.kwargs['shorname']
        lista =  Persona.objects.filter(
            departamento__shor_name = area
        )
        return lista

class ListEmpeladosByKword(ListView):
    """Lista de empleados por palabra clave."""
    template_name = 'empleado/list_by_kword.html'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        print('********************************')
        palabra_clave = self.request.GET.get('kword','',)
        lista =  Persona.objects.filter(
            fist_name = palabra_clave
        )        
        return [lista]

class ListHabilidadesEmpledos(ListView):
    template_name = 'empleado/habilidades.html'
    context_object_name = 'habilidades'
    
    def get_queryset(self):
        empleado = Persona.objects.get(id=2)
        return [empleado.habilidades.all()]

class EmpleadoDetailView(DetailView):
    model = Persona
    template_name = "empleado/detail_empleado.html"
    context_object_name = "detalle_empleado"
    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context


class SuccessView(TemplateView):
    template_name = "empleado/success.html"


class EmpleadoCreateView(CreateView):
    model = Persona
    template_name = 'empleado/add.html'
    form_class = EmpleadoForms

    
    success_url = reverse_lazy('persona_app:lista_admin_empleados')
    
    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.fist_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)

class EmpleadoUpdateView(UpdateView):
    model = Persona
    template_name = "empleado/update.html"
    fields=[
        'fist_name', 
        'last_name',
        'job',
        'departamento',
        'habilidades'
        ]
    success_url = reverse_lazy('persona_app:lista_admin_empleados')
    
    def get_post(self, request,*args,**kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        form
        return super(EmpleadoUpdateView, self).form_valid(form)

class EmpleadoDeleteView(DeleteView):
    model = Persona
    template_name = "empleado/delete.html"
    context_object_name = "eliminar_empleado"
    success_url = reverse_lazy('persona_app:lista_admin_empleados')
        
class ListaEmpleadosAdminsView(ListView):
    model = Persona
    paginate_by = 10
    template_name = "empleado/listar_admin.html"
    context_object_name = 'empleados_admin'


    
    
    
    

