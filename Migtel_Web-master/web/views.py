from django.shortcuts import render
from datetime import date
import datetime
from django.core.mail import EmailMessage
from .forms import *
import time
import smtplib
from . import config
from .models import *


# Create your views here.


def main(request):
    localtime = datetime.date.today()
    year = int(date.today().year)
    title = 'Home'
    print(localtime, year)

    context = {
        'year': year,
        'localtime': localtime,
        'title': title,
    }
    return render(request, 'home.html', context)


def nosotros(request):
    localtime = datetime.date.today()
    year = int(date.today().year)
    print(localtime, year)

    context = {
        'year': year,
        'localtime': localtime,
    }
    return render(request, 'nosotros.html', context)


def cobertura(request):
    localtime = datetime.date.today()
    year = int(date.today().year)
    print(localtime, year)
    ccs_1 = Cobertura.objects.filter(ciudad='Caracas', zona='1')
    ccs_2 = Cobertura.objects.filter(ciudad='Caracas', zona='2')
    gte = Cobertura.objects.filter(ciudad='Guarenas - Guatire')
    hgt = Cobertura.objects.filter(ciudad='Higuerote')

    context = {
        'year': year,
        'localtime': localtime,
        'ccs_1': ccs_1,
        'ccs_2': ccs_2,
        'gte': gte,
        'hgt': hgt,
    }
    return render(request, 'cobertura.html', context)


def servicios(request):
    localtime = datetime.date.today()
    year = int(date.today().year)
    print(localtime, year)

    context = {
        'year': year,
        'localtime': localtime,
    }
    return render(request, 'servicios.html', context)


def solicitarservicio(request):
    localtime = datetime.date.today()
    year = int(date.today().year)
    print(localtime, year)

    form = ServicioForm(request.POST or None)

    if form.is_valid():
        context = {
            "form": form,
        }

    context = {
        'year': year,
        'localtime': localtime,
    }
    return render(request, 'solicitarservicio.html', {"form": form, 'year': year, 'localtime': localtime})


# def registrarpago(request):
#     localtime = datetime.date.today()
#     year = int(date.today().year)
#     print(localtime, year)
#
#     form = PagoForm(request.POST or None)
#
#     if form.is_valid():
#         context = {
#             "form": form,
#         }
#
#         Nombres = form.cleaned_data.get("Nombres")
#         Telefono = form.cleaned_data.get("Telefono")
#         Email = form.cleaned_data.get("Email")
#         Metodo_de_pago = form.cleaned_data.get("Metodo_de_pago")
#         Monto = form.cleaned_data.get("Monto")
#         Numero_de_Confirmacion = form.cleaned_data.get("Numero_de_Confirmacion")
#         Fecha = form.cleaned_data.get("Fecha")
#         Mensaje = form.cleaned_data.get("Mensaje")
#         Imagen = form.cleaned_data.get("Imagen")
#
#         print(Nombres, Telefono, Email, Metodo_de_pago, ' $', Monto, Fecha, Mensaje)
#
#         title = 'Notificacion de Pago - Cliente: ' + Nombres
#         body = Nombres + '\n ' + Telefono + '\n ' + Email + '\n ' + Metodo_de_pago + ' $' + str(Monto) + ' '\
#                + '\n Numero de Confirmacion: ' + Numero_de_Confirmacion + '\n ' + Mensaje + '\n\n  © Copyright 2020 - Comunicaciones MigTel, C.A. RIF.: J-40212711-1'
#
#         print(title, body)
#         email = EmailMessage(title, body, to=['diegoporro25@gmail.com'])
#         email.send()
#
#         form = PagoForm
#
#     context = {
#         'year': year,
#         'localtime': localtime,
#     }
#     return render(request, 'registrarpago.html', {"form": form, 'year': year, 'localtime': localtime})


def contacto(request):
    localtime = datetime.date.today()
    year = int(date.today().year)
    print(localtime, year)

    form = ContactForm(request.POST or None)

    if form.is_valid():
        context = {
            "form": form,
        }

        Nombres = form.cleaned_data.get("Nombres")
        Telefono = form.cleaned_data.get("Telefono")
        Email = form.cleaned_data.get("Email")
        Mensaje = form.cleaned_data.get("Mensaje")

        print(Nombres, Telefono, Email, Mensaje)

        title = 'Mensaje de: ' + Nombres
        body = Nombres + '\n ' + Telefono + '\n ' + Email + '\n ' + '\n ' + Mensaje + '\n\n  © Copyright 2020 - Comunicaciones MigTel, C.A. RIF.: J-40212711-1'

        print(title, body)
        email = EmailMessage(title, body, to=['diegoporro25@gmail.com'])
        email.send()

        form = PagoForm

    context = {
        'year': year,
        'localtime': localtime,
    }
    return render(request, 'contact.html', {"form": form, 'year': year, 'localtime': localtime})


def soporte(request):
    localtime = datetime.date.today()
    year = int(date.today().year)
    print(localtime, year)

    context = {
        'year': year,
        'localtime': localtime,
    }
    return render(request, 'soporte.html', context)

