from django.contrib import admin
from gm.models import Suscripciones, Categoria, Materia, Profesor, Programa, Tema, Sesion, Curso, RegistroMateria


class SuscripcionesAdmin(admin.ModelAdmin):
    list_display = ('email', 'fecha', 'hora')
    ordering = ('fecha', 'hora')
    search_fields = ('email',)


admin.site.register(Suscripciones, SuscripcionesAdmin)

admin.site.register(Categoria)


class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'company', 'aniocreacion', 'ultimaversion', 'link', 'imagen1', 'imagen2')
    ordering = ('categoria',)
    search_fields = ('nombre',)
    list_filter = ('categoria',)


admin.site.register(Materia, MateriaAdmin)


class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellido1', 'apellido2', 'cedula', 'email', 'twitter', 'linkedin')
    ordering = ('apellido1', 'apellido2', 'nombres')
    search_fields = ('apellido1', 'apellido2', 'nombres', 'cedula')


admin.site.register(Profesor, ProfesorAdmin)


class ProgramaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'materia', 'horas', 'profesor')
    ordering = ('materia__nombre',)
    search_fields = ('titulo', 'materia__nombre', 'profesor__nombres', 'profesor__apellido1', 'profesor__apellido2')


admin.site.register(Programa, ProgramaAdmin)


class TemaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'programa', 'horas',)
    ordering = ('programa', 'titulo')
    search_fields = ('titulo', 'programa__titulo', 'programa__profesor__nombres', 'programa__profesor__apellido1',
                     'programa__profesor__apellido2')


admin.site.register(Tema, TemaAdmin)


class SesionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'horainicio', 'horafin')
    ordering = ('nombre',)
    search_fields = ('nombre',)


admin.site.register(Sesion, SesionAdmin)


class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'programa', 'inicio', 'fin', 'sesion')
    ordering = ('sesion', 'inicio')
    search_fields = ('nombre', 'programa__titulo', 'programa__profesor__nombres', 'programa__profesor__apellido1',
                     'programa__profesor__apellido2')


admin.site.register(Curso, CursoAdmin)


class RegistroMateriaAdmin(admin.ModelAdmin):
    list_display = ('persona', 'email', 'materia', 'fecha', 'hora')
    ordering = ('materia', 'fecha', 'hora')
    search_fields = ('persona', 'materia__nombre')


admin.site.register(RegistroMateria, RegistroMateriaAdmin)
