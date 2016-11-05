from django.db import models
from django.db.models import Sum


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return u"{}".format(self.nombre)

    class Meta:
        verbose_name = u"Category"
        verbose_name_plural = u"Categories"
        db_table = 'categories'
        unique_together = ('nombre', )
        ordering = ('nombre', )

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        if self.nombre:
            self.nombre = self.nombre.upper()
        super(Categoria, self).save(force_insert, force_update, using)


class Suscripciones(models.Model):
    email = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return u"{0} ({1})".format(self.email, self.fecha.strftime('%d-%m-%Y'))

    class Meta:
        verbose_name = u"Newsletter"
        verbose_name_plural = u"Newsletters"
        db_table = 'newsletters'
        ordering = ('fecha', 'hora', 'email')


class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(default="")
    categoria = models.ForeignKey(Categoria)
    company = models.CharField(max_length=100, blank=True, null=True)
    aniocreacion = models.IntegerField(blank=True, null=True)
    ultimaversion = models.CharField(max_length=100, blank=True, null=True)
    link = models.CharField(max_length=100, blank=True, null=True)
    imagen1 = models.FileField(upload_to='imagenes1', blank=True, null=True)  # images to description medium Sliding 
    imagen2 = models.FileField(upload_to='imagenes2', blank=True, null=True)  # images to description small Sliding 

    def __str__(self):
        return u"{0} ({0})".format(self.nombre, self.categoria.nombre)

    class Meta:
        verbose_name = u"Subject"
        verbose_name_plural = u"Subjects"
        db_table = 'subjects'
        unique_together = ('nombre', 'categoria')
        ordering = ('-nombre', )

    def programa_asociado(self):
        return self.programa_set.all()[:1].get() if self.programa_set.exists() else None

    def download_imagen1(self):
        return self.imagen1.url

    def download_imagen2(self):
        return self.imagen2.url

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        if self.nombre:
            self.nombre = self.nombre.upper()
        if self.link:
            self.link = self.link.lower()
        super(Materia, self).save(force_insert, force_update, using)


class Profesor(models.Model):
    nombres = models.CharField(max_length=200)
    apellido1 = models.CharField(max_length=200)
    apellido2 = models.CharField(max_length=200, blank=True, null=True)
    cedula = models.CharField(max_length=10, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    linkedin = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return "{0} {1}".format(self.nombres, self.apellido1)

    class Meta:
        verbose_name = u"Teacher"
        verbose_name_plural = u"Teachers"
        db_table = 'teachers'
        unique_together = ('cedula', )
        ordering = ('apellido1', 'apellido2', 'nombres')

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        if self.nombre:
            self.nombre = self.nombre.upper()
        if self.apellido1:
            self.apellido1 = self.apellido1.upper()
        if self.apellido2:
            self.apellido2 = self.apellido2.upper()
        if self.email:
            self.email = self.email.lower()
        if self.twitter:
            self.twitter = self.twitter.lower()
        if self.linkedin:
            self.linkedin = self.linkedin.lower()
        super(Profesor, self).save(force_insert, force_update, using)


class Programa(models.Model):
    materia = models.ForeignKey(Materia)
    profesor = models.ForeignKey(Profesor, blank=True, null=True)
    titulo = models.CharField(max_length=200)
    objetivo = models.TextField(blank=True, null=True)
    horas = models.IntegerField(default=0)

    def __str__(self):
        return "{0} [{1}] - ({2} Hrs)".format(self.titulo, self.materia.nombre, self.horas)

    class Meta:
        verbose_name = u"Program"
        verbose_name_plural = u"Programs"
        db_table = 'programs'
        unique_together = ('titulo', 'materia', 'profesor')
        ordering = ('materia', )

    def nombre_simple(self):
        return self.titulo + ' (' + str(self.horas) + ' Horas)'

    def temas(self):
        return self.tema_set.all().order_by('id')

    def cantidad_horas(self):
        return self.temas().aggregate(Sum('horas'))['horas__sum'] if self.temas() else 0

    def get_materia(self):
        return self.materia.nombre

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        if self.titulo:
            self.titulo = self.titulo.upper()
        self.horas = self.cantidad_horas()
        super(Programa, self).save(force_insert, force_update, using)


class Tema(models.Model):
    programa = models.ForeignKey(Programa)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    horas = models.IntegerField(default=0)

    def __str__(self):
        return "{0} ({1}) [{2}]".format(self.titulo, self.horas, self.programa.titulo)

    class Meta:
        verbose_name = u"Issue"
        verbose_name_plural = u"Issues"
        db_table = 'issues'
        ordering = ('programa', )

    def repr_descripcion(self):
        return self.descripcion.split(".")

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        if self.titulo:
            self.titulo = self.titulo.upper()
        super(Tema, self).save(force_insert, force_update, using)
        self.programa.save()


class Sesion(models.Model):
    nombre = models.CharField(max_length=100)
    horainicio = models.TimeField()
    horafin = models.TimeField()

    def __str__(self):
        return "{0} ({1} - {2})".format(self.nombre, self.horainicio.strftime("%H:%M"), self.horafin.strftime("%H:%M"))

    class Meta:
        verbose_name = u"Session"
        verbose_name_plural = u"Sessions"
        db_table = 'sessions'
        unique_together = ('nombre', )
        ordering = ('horainicio', 'horafin')

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        if self.nombre:
            self.nombre = self.nombre.upper()
        super(Sesion, self).save(force_insert, force_update, using)


class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    programa = models.ForeignKey(Programa)
    inicio = models.DateField(blank=True, null=True)
    fin = models.DateField(blank=True, null=True)
    sesion = models.ForeignKey(Sesion, blank=True, null=True)

    def __str__(self):
        return "{0} ({1} - {2}) [{3}]".format(self.nombre, self.inicio.strftime('%d-%m-%Y'),
                                              self.fin.strftime('%d-%m-%Y'), self.programa.titulo)

    class Meta:
        verbose_name = u"Course"
        verbose_name_plural = u"Courses"
        db_table = 'courses'
        unique_together = ('nombre', 'programa')
        ordering = ('sesion', 'inicio')

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        if self.nombre:
            self.nombre = self.nombre.upper()
        super(Curso, self).save(force_insert, force_update, using)


class RegistroMateria(models.Model):
    persona = models.CharField(max_length=300)
    email = models.CharField(max_length=200)
    comentario = models.TextField(blank=True, null=True)
    materia = models.ForeignKey(Materia)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return "{0} ({1}) [{2}]".format(self.persona, self.materia.nombre, self.fecha.strftime('%d-%m-%Y'))

    class Meta:
        verbose_name = u"Subject Register"
        verbose_name_plural = u"Subjects Registers"
        db_table = 'subject_register'
        ordering = ('materia', 'fecha')

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        if self.persona:
            self.persona = self.persona.upper()
        if self.email:
            self.email = self.email.lower()
        super(RegistroMateria, self).save(force_insert, force_update, using)
