from django.contrib import admin
from .models import Persona, Habilidades
# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    list_display = (
        'fist_name',
        'last_name',
        'departamento',
        'job',
        'full_name',        
    )
    
    def full_name(self, obj):
        full_name = obj.fist_name + ' ' + obj.last_name
        return full_name


    search_fields = ('fist_name',)
    list_filter= ('departamento','job', 'habilidades',)
    
    filter_horizontal = ('habilidades',)

admin.site.register(Habilidades)
admin.site.register(Persona, PersonaAdmin)
