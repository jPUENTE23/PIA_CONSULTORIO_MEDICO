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

# FUNCION OBETENER FECHA DEL SISTEMA
'''
    Esta funcion se utliza para madar la fecha del sistema a hacia laa fecha al momento de registrar una consulta.
    Asi cuando se despliegue el calendario, tome la fecha actual en adelante'''

def obetenerFecha():
    fecha = datetime.date.today()
    return fecha

# FUNCION VISTA MAIN
'''
    La funcion main es la vista principal en donde mostraremos la pantallla principal al acceder a ala aplicacion
    Esta vista devueleve los citas que se han registrado hasta el momento y futuras'''

def main(request):
    vistaCitas = Cita.objects.all()
    ctxMain = {
        'vistaMain': vistaCitas
    }
    return render(request, 'main.html', ctxMain)


# FUNCION VISTA_REGISTRO
'''
    lA FUNCION vistaRegistro mostarara la el template en donde se encontrara el fomrulario para regitara una cita.
    Esta tambine al igual que en main, se veran todas las consultas registradas pero con mayor detalles'''

def vistaRegistro(request):
    fecha = datetime.date.today()
    doctor = Doctor.objects.all()
    citas = Cita.objects.all()
    ctxDoc = {
        'Doctores': doctor, 'fechaSistema':fecha,'citasReg':citas
    }
    return render(request, 'regitroCita.html', ctxDoc)


# FUNCION AGREGAR_REGISTRO
'''
    lA vista agregarRegistro obtendra los valores ingresados en el formulario y los alamacenara en el modelado de datos correspondiente'''

def agregarRegistro (request):
    nombre = request.POST['nombreP']
    apellidosP = request.POST['apellidosPP']
    apellidosM = request.POST['apellidosMP']
    fechaNac = request.POST['fechaNac']
    edad = request.POST['edadP']
    sexo = request.POST['sexoP']
    fechaConsulta = request.POST['fechaCons']
    totalConsulta = request.POST['TotalConsul']
    doctor = request.POST['doctorAsig']
    insertDatos = Cita(
            NomDoctor = Doctor.objects.get(IdDoctor=doctor),
            NomPaciente=nombre,
            Apeterno=apellidosP,
            Amaterno=apellidosM,
            FecNacimiento=fechaNac,
            Edad=edad,
            Sexo=sexo,
            FechaConsulta=fechaConsulta,
            TotalConsulta=totalConsulta)

    insertDatos.save()
    return HttpResponseRedirect(reverse('RegistroCitas'))

# FUNCION VERIFICAR_CONSULTAS
'''
    Esta vista vuelve a mostrar todas las consultass registradas, pero a diferencia de las otras, en esta se tendra la opciopn de
    si desea generar un pago de la conuslta seleccionada'''

def verificarConsultas(request):
    consultas = Cita.objects.all()
    ctxConsultas = {
        'consultas':consultas
    }
    return render(request, 'verifRegistros.html',ctxConsultas)


# FUNCION LISTADO_DOCTORES
'''
    MOstarar el listado de doctores que se encuentran trabajadno en el consultorio medico'''

def listadoDoctores(request):
    listaDoc  = Doctor.objects.all()
    ctxDoc = {
        'dcotores':listaDoc
    }
    return render (request, 'regDoc.html', ctxDoc)

# FUNCION AGREGAR_DOCTOR
'''
    En esta funcion, se obtendra los datos cuando que desea dar de alata un nuevo doctor'''

def agregarDoctor(request):

    nomDoc = request.POST['nombreDoc']
    nuevoDoc = Doctor(NomDoctor=nomDoc)
    nuevoDoc.save()

    return HttpResponseRedirect(reverse('listadoDoctores'))