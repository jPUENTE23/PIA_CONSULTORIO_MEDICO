from datetime import datetime
from django import views
from django.http import HttpResponseRedirect
from django.shortcuts import render
from numpy import datetime64
from Citas.models import Cita
from Citas.views import *
from .models import Pagos
from django.urls import reverse
from Citas.views import obetenerFecha
# Create your views here.





def pagos(request,idCita):
    total = Cita.objects.filter(NoCita=idCita).values_list('TotalConsulta')
    print(total)
    pagado = Cita.objects.filter(NoCita=idCita).values_list('TotalConsulta')
    print(pagado)
    val_total = total[0][0]
    val_pagado = pagado[0][0]
    
    fechaEm = obetenerFecha()

    datos  = Pagos(NoCita=Cita.objects.get(NoCita=idCita),
                   MontoPagar=val_total,
                   fechaEmision=fechaEm,
                   Pagado=val_pagado)

    datos.save()

    return HttpResponseRedirect(reverse('main'))

def consultarPagos(request):
    _pagos = Pagos.objects.all()
    
    Pagos_ctx = {
        'consPagos': _pagos
    }
    
    return render(request, 'vistaPagos.html', Pagos_ctx)

def vistaPagos(request):
    consultas = Cita.objects.all()

    ctxConsultas = {
        'consultas':consultas
    }
    return render(request,'verifRegistros.html' ,ctxConsultas )


def eliminarPago(reques, idPago):

    pago = Pagos.objects.get(IdPago=idPago)
    pago.delete()
    
    return HttpResponseRedirect(reverse('consultarPagos'))