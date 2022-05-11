from django.shortcuts import render
from Citas.models import Cita
# Create your views here.


def pagos(request,idCita):
    
    pago = Cita.objects.get(NoCita=idCita)
    
    ctxPago = {
        'pago' : pago
    }
    
    return render(request,'genPago.html' ,ctxPago)


def vistaPagos(request):
    consultas = Cita.objects.all()
    
    ctxConsultas = {
        'consultas':consultas
    }
    return render(request,'verifRegistros.html' ,ctxConsultas )