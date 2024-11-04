from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView
from .forms import NewDepartamentoForm
from applications.empleados.models import Persona
from .models import Departamento
# Create your views here.


class newDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'
    
    def form_valid(self, form):
        depa = Departamento(
            name = form.cleaned_data['departamento'],
            shor_name = form.cleaned_data['shorname'],
        )
        depa.save()
        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']
        Persona.objects.create(
            fist_name = nombre,
            last_name =apellidos,
            job = 1,
            departamento=depa
        ),
        
        

        return super(newDepartamentoView, self).form_valid(form)

class ListarDepartamentoView(ListView):
    model = Departamento
    template_name =  'departamento/listar_departamento.html'
    context_object_name='Departamento' 
