from django import forms
from .models import Persona


class EmpleadoForms(forms.ModelForm):
    
    class Meta:
        model = Persona
        fields = (
            'fist_name', 
            'last_name',
            'job',
            'departamento',
            'avatar',
            'habilidades',
            
                  )
        
        widgets = {
         'habilidades': forms.CheckboxSelectMultiple()
        }
