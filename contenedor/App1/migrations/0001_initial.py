# Generated by Django 5.1 on 2024-08-23 03:43

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CandidatoDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('edad', models.IntegerField(verbose_name='Edad')),
                ('correo', models.CharField(max_length=70, verbose_name='Correo')),
                ('contrasena', models.CharField(max_length=50, verbose_name='Contrasena')),
                ('tipo', models.TextField(max_length=20, verbose_name='Tipo de Usuario')),
                ('especialidades', models.TextField(max_length=100, verbose_name='Especialidades')),
                ('habilidades', models.CharField(max_length=100, verbose_name='Habilidades')),
                ('experiencia', models.CharField(choices=[('>4 años', 'Más de 4 años'), ('<4 años', 'Menos de 4 años'), ('ninguna', 'Ninguna')], max_length=70, verbose_name='Experiencia')),
            ],
            options={
                'verbose_name': 'Candidato',
                'verbose_name_plural': 'Candidatos',
                'db_table': 'Candidatos',
            },
        ),
        migrations.CreateModel(
            name='EmpleadorDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('edad', models.IntegerField(verbose_name='Edad')),
                ('correo', models.CharField(max_length=70, verbose_name='Correo')),
                ('contrasena', models.CharField(max_length=50, verbose_name='Contrasena')),
                ('tipo', models.TextField(max_length=20, verbose_name='Tipo de Usuario')),
                ('nombre_empresa', models.CharField(max_length=100, verbose_name='Nombre de Empresa')),
                ('descripcion', models.TextField(max_length=100, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Empleador',
                'verbose_name_plural': 'Empleadores',
                'db_table': 'Empleadores',
            },
        ),
        migrations.CreateModel(
            name='OfertaDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, verbose_name='Titulo')),
                ('descripcion', models.TextField(verbose_name='Descripcion')),
                ('topicos', models.CharField(max_length=50, verbose_name='Topico')),
                ('habilidades_requeridas', models.TextField(max_length=100, verbose_name='Habilidades Requeridas')),
                ('beneficios', models.TextField(verbose_name='Beneficios')),
                ('empleador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.empleadordb')),
            ],
            options={
                'verbose_name': 'Oferta',
                'verbose_name_plural': 'Ofertas',
                'db_table': 'Ofertas',
            },
        ),
        migrations.CreateModel(
            name='ResenasDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField(blank=True, verbose_name='Contenido')),
                ('calificacion', models.CharField(max_length=10, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Calificación')),
                ('empleador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.empleadordb')),
            ],
            options={
                'verbose_name': 'Reseña',
                'verbose_name_plural': 'Reseñas',
                'db_table': 'Reseñas',
            },
        ),
    ]
