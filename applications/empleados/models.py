from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

class Habilidades(models.Model):
    habilidad = models.CharField("Habilidad", max_length=50)
    
    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad
    
    
class Persona(models.Model):
    """Modelo para tabla empleados."""
    JOB_CHOICES = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro'),
    )
    fist_name = models.CharField("Nombres", max_length=60)
    last_name = models.CharField("Apellidos", max_length=60)
    full_name = models.CharField("Nombres Completos", max_length=150, blank=True)
    job = models.CharField("Job", max_length=50, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento,  on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hojavida = RichTextField()
    
    class Meta:
        verbose_name = 'Mi Empleado'
        verbose_name_plural = 'Empleados de la Empresa'
        ordering = ['-fist_name']
        unique_together = ('fist_name', 'last_name')
    
    def __str__(self):
        return str(self.id) + '-' + self.fist_name + '-' + self.last_name