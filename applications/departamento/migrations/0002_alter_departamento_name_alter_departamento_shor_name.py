# Generated by Django 5.1.2 on 2024-10-24 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='name',
            field=models.CharField(blank=True, editable=False, help_text='Nombre Departamento', max_length=50, null=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='shor_name',
            field=models.CharField(help_text='Nombre Corto Departamento', max_length=20, unique=True, verbose_name='Nombre Corto'),
        ),
    ]
