from django.db import models

# Create your models here.

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50, blank=True, null=True,help_text="Nombre Departamento", editable=False)
    shor_name = models.CharField('Nombre Corto', max_length=20, unique=True, help_text="Nombre Corto Departamento")
    anulate = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Mi Departamento'
        verbose_name_plural = 'Areas de la Empresa'
        ordering = ['-name']
        unique_together = ('name', 'shor_name')
                         
    def __str__(self):
        return  str(self.id) + '-' + str(self.name) + '-' + str(self.shor_name)
    
    
    
    
    
    