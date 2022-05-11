from audioop import reverse
from urllib import request
from django.forms import modelform_factory
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from Citas.models import Cita, Doctor
# Create your views here
from django.shortcuts import render
import datetime
from django.urls import reverse


def main(request):
    
    vistaCitas = Cita.objects.all()
    
    ctxMain = {
        'vistaMain': vistaCitas
    }
    
    return render(request, 'main.html', ctxMain)

def calcula_edad(fecha_nac):
    hoy = datetime.date.today()
    return hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))

def vistaRegistro(request):
    fecha = datetime.date.today()

    # calEdad = calcula_edad(fechaNac)
    # edad = calEdad

    doctor = Doctor.objects.all()
    citas = Cita.objects.all()
    ctxDoc = {
        'Doctores': doctor, 'fechaSistema':fecha,'citasReg':citas
    }

    return render(request, 'regitroCita.html', ctxDoc)

citasForm = modelform_factory(Cita, exclude=[])

def agregarRegistro (request):
    
    nombre = request.POST['nombreP']
    apellidosP = request.POST['apellidosPP']
    apellidosM = request.POST['apellidosMP']
    fechaNac = request.POST['fechaNac']
    edad = request.POST['edadP']
    sexo = request.POST['sexoP']
    fechaConsulta = request.POST['fechaCons']
    totalConsulta = request.POST['TotalConsul']

    insertDatos = Cita(
            NomPaciente=nombre,
            Apeterno=apellidosP,
            Amaterno=apellidosM,
            FecNacimiento=fechaNac,
            Edad=edad,
            Sexo=sexo,
            FechaConsulta=fechaConsulta,
            TotalConsulta=totalConsulta)

    insertDatos.save()

    return HttpResponseRedirect(reverse('main'))



def verificarConsultas(request):
    
    consultas = Cita.objects.all()
    
    ctxConsultas = {
        'consultas':consultas
    }
    
    return render(request, 'verifRegistros.html',ctxConsultas)

# def nuevaCita(request):
#     if request.method == 'POST':
#         form = citaForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('main')
#     else:
#         form = citaForm()
    
#     return render (request, 'prueba.html', form)

