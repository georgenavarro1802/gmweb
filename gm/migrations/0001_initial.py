# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-05 20:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('nombre',),
                'db_table': 'categories',
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('inicio', models.DateField(blank=True, null=True)),
                ('fin', models.DateField(blank=True, null=True)),
            ],
            options={
                'ordering': ('sesion', 'inicio'),
                'db_table': 'courses',
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(default=b'')),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('aniocreacion', models.IntegerField(blank=True, null=True)),
                ('ultimaversion', models.CharField(blank=True, max_length=100, null=True)),
                ('link', models.CharField(blank=True, max_length=100, null=True)),
                ('imagen1', models.FileField(blank=True, null=True, upload_to=b'imagenes1')),
                ('imagen2', models.FileField(blank=True, null=True, upload_to=b'imagenes2')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gm.Categoria')),
            ],
            options={
                'ordering': ('-nombre',),
                'db_table': 'subjects',
                'verbose_name': 'Subject',
                'verbose_name_plural': 'Subjects',
            },
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=200)),
                ('apellido1', models.CharField(max_length=200)),
                ('apellido2', models.CharField(blank=True, max_length=200, null=True)),
                ('cedula', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('linkedin', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ('apellido1', 'apellido2', 'nombres'),
                'db_table': 'teachers',
                'verbose_name': 'Teacher',
                'verbose_name_plural': 'Teachers',
            },
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('objetivo', models.TextField(blank=True, null=True)),
                ('horas', models.IntegerField(default=0)),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gm.Materia')),
                ('profesor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gm.Profesor')),
            ],
            options={
                'ordering': ('materia',),
                'db_table': 'programs',
                'verbose_name': 'Program',
                'verbose_name_plural': 'Programs',
            },
        ),
        migrations.CreateModel(
            name='RegistroMateria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persona', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=200)),
                ('comentario', models.TextField(blank=True, null=True)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gm.Materia')),
            ],
            options={
                'ordering': ('materia', 'fecha'),
                'db_table': 'subject_register',
                'verbose_name': 'Subject Register',
                'verbose_name_plural': 'Subjects Registers',
            },
        ),
        migrations.CreateModel(
            name='Sesion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('horainicio', models.TimeField()),
                ('horafin', models.TimeField()),
            ],
            options={
                'ordering': ('horainicio', 'horafin'),
                'db_table': 'sessions',
                'verbose_name': 'Session',
                'verbose_name_plural': 'Sessions',
            },
        ),
        migrations.CreateModel(
            name='Suscripciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
            ],
            options={
                'ordering': ('fecha', 'hora', 'email'),
                'db_table': 'newsletters',
                'verbose_name': 'Newsletter',
                'verbose_name_plural': 'Newsletters',
            },
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('horas', models.IntegerField(default=0)),
                ('programa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gm.Programa')),
            ],
            options={
                'ordering': ('programa',),
                'db_table': 'issues',
                'verbose_name': 'Issue',
                'verbose_name_plural': 'Issues',
            },
        ),
        migrations.AlterUniqueTogether(
            name='sesion',
            unique_together=set([('nombre',)]),
        ),
        migrations.AlterUniqueTogether(
            name='profesor',
            unique_together=set([('cedula',)]),
        ),
        migrations.AddField(
            model_name='curso',
            name='programa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gm.Programa'),
        ),
        migrations.AddField(
            model_name='curso',
            name='sesion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='gm.Sesion'),
        ),
        migrations.AlterUniqueTogether(
            name='categoria',
            unique_together=set([('nombre',)]),
        ),
        migrations.AlterUniqueTogether(
            name='programa',
            unique_together=set([('titulo', 'materia', 'profesor')]),
        ),
        migrations.AlterUniqueTogether(
            name='materia',
            unique_together=set([('nombre', 'categoria')]),
        ),
        migrations.AlterUniqueTogether(
            name='curso',
            unique_together=set([('nombre', 'programa')]),
        ),
    ]
