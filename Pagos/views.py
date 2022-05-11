from django.http import HttpResponseRedirect
from django.shortcuts import render
from Citas.models import Cita
from .models import Pagos
from django.urls import reverse
# Create your views here.


def pagos(request,idCita):
    total = Cita.objects.filter(NoCita=idCita).values_list('TotalConsulta')
    print(total)
    pagado = Cita.objects.filter(NoCita=idCita).values_list('TotalConsulta')
    print(pagado)
    val_total = total[0][0]
    val_pagado = pagado[0][0]


    datos  = Pagos(NoCita=Cita.objects.get(NoCita=idCita),
                   MontoPagar=val_total,
                   Pagado=val_pagado)

    datos.save()

    return HttpResponseRedirect(reverse('main'))

# def agregPago(request):

#     noCita = request.POST['Nocita']
#     total = request.POST['totalPag']
#     pagado = request.POST['totalPag']




def vistaPagos(request):
    consultas = Cita.objects.all()

    ctxConsultas = {
        'consultas':consultas
    }
    return render(request,'verifRegistros.html' ,ctxConsultas )