# Generated by Django 5.1.2 on 2024-10-24 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades Empleados',
            },
        ),
        migrations.AlterModelOptions(
            name='persona',
            options={'ordering': ['-fist_name'], 'verbose_name': 'Mi Empleado', 'verbose_name_plural': 'Empleados de la Empresa'},
        ),
        migrations.AlterUniqueTogether(
            name='persona',
            unique_together={('fist_name', 'last_name')},
        ),
    ]
