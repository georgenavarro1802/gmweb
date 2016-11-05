# -*- coding: latin-1 -*-
import json
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render_to_response

from gm.models import Suscripciones, Categoria, Materia, RegistroMateria
from gm.tareas import send_html_mail
from gmweb.settings import NOMBRE_INSTITUCION, CONTACTO_FORM, EMAIL_ACTIVE


def index(request):
    return render_to_response("index.html",
                              {'title': NOMBRE_INSTITUCION + ' | Web Page',
                               'categorias': Categoria.objects.all().order_by('id'),
                               'materias': Materia.objects.all()})


def materia(request):
    materia = Materia.objects.get(pk=request.GET['mid'])
    return render_to_response("materia.html",
                              {'title': 'Issue: ' + materia.nombre,
                               'materia': materia,
                               'programa': materia.programa_asociado()})


def contacto(request):
    try:
        nombre = request.POST['nombre']
        email = request.POST['email']
        mensaje = request.POST['mensaje']
        data = {'nombre': nombre, 'email': email, 'mensaje': mensaje}
        if EMAIL_ACTIVE:
            send_html_mail("Mensaje Recibido desde GM WEB", "emails/usermensaje.html", data, CONTACTO_FORM)
        return HttpResponse(json.dumps({"result": "ok"}), content_type="application/json")
    except Exception:
        return HttpResponse(json.dumps({"result": "bad"}), content_type="application/json")


def suscripcion(request):
    try:
        email = request.POST['email']
        if not Suscripciones.objects.filter(email=email).exists():
            suscripcion = Suscripciones(email=email, fecha=datetime.now().date(), hora=datetime.now().time())
            suscripcion.save()
            cantidad_suscripciones = Suscripciones.objects.all().count()
            if EMAIL_ACTIVE:
                send_html_mail("Newsletter - GM WEB", "emails/suscripcion.html",
                               {'email': email, 'cantidad': cantidad_suscripciones}, CONTACTO_FORM)
        else:
            suscripcion = Suscripciones.objects.filter(email=email)[0]
            suscripcion.save()
        return HttpResponse(json.dumps({"result": "ok"}), content_type="application/json")
    except Exception:
        return HttpResponse(json.dumps({"result": "bad"}), content_type="application/json")


def registrointeres(request):
    try:
        nombre = request.POST['nombre']
        email = request.POST['email']
        mensaje = request.POST['mensaje']
        materia = Materia.objects.get(pk=request.POST['materiaid'])
        hoy = datetime.now()
        data = {'nombre': nombre, 'email': email, 'mensaje': mensaje, 'materia': materia, 'hoy': hoy}

        if not RegistroMateria.objects.filter(email=email, materia=materia).exists():
            rm = RegistroMateria(persona=nombre,
                                 email=email,
                                 comentario=mensaje,
                                 materia=materia,
                                 fecha=hoy.date(),
                                 hora=hoy.time())
            rm.save()
            if EMAIL_ACTIVE:
                send_html_mail("GM WEB Register", "emails/registrointeres.html", data, CONTACTO_FORM)
                send_html_mail("GM WEB Register Confirmation", "emails/registrointeresusuario.html", data, [email])
        return HttpResponse(json.dumps({"result": "ok"}), content_type="application/json")
    except Exception:
        return HttpResponse(json.dumps({"result": "bad"}), content_type="application/json")
