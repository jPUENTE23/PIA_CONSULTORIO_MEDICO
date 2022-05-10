from audioop import reverse
from urllib import request
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render
from Citas.models import Cita, Doctor
# Create your views here
from django.shortcuts import render
import datetime



def main(request):
    return render(request, 'main.html', {})

def calcula_edad(fecha_nac):
    hoy = datetime.date.today()
    return hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))

def vistaRegistro(request):
    fecha = datetime.date.today()
 
    # calEdad = calcula_edad(fechaNac)
    # edad = calEdad

    doctor = Doctor.objects.all()
    ctxDoc = {
        'Doctores': doctor, 'fechaSistema':fecha
    }
    
    return render(request, 'regitroCita.html', ctxDoc)

def agregarRegistro (request):
    
    nombre = request.POST['nombreP']
    apellidosP = request.POST['apellidosPP']
    apellidosM = request.POST['apellidosMP']
    fechaNac = request.POST['fechaNac']
    edad = request.POST['edadP']
    sexo = request.POST['sexoP']
    fechaConsulta = request.POST['fechaCons']
    totalConsulta = request.POST['TotalConsul']
    doctorAsig = request.POST['doctorAsig']
    
    insertDatos = Cita(Doctor=doctorAsig, 
                       NomPaciente=nombre,
                       Apeterno=apellidosP,
                       Amaterno=apellidosM,
                       FecNacimiento=fechaNac,
                       Edad=edad,
                       Sexo=sexo,
                       FechaConsulta=fechaConsulta,
                       TotalConsulta=totalConsulta)
    
    insertDatos.save()
    
    return HttpResponsePermanentRedirect(reverse('main'))