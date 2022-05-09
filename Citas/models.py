from django.db import models

# Create your models here.


class Doctor(models.Model):
    IdDoctor = models.AutoField(primary_key=True,  verbose_name='Id del Doctor')
    NomDoctor = models.CharField(max_length=50, null=False, blank=False, verbose_name='Nombre del doctor')

class Cita(models.Model):
    NoCita = models.AutoField(primary_key=True, verbose_name='No. de Cita')
    Doctor = models.ForeignKey(Doctor, null=False, blank=False, verbose_name='Doctor asiganado',on_delete=models.CASCADE)
    NomPaciente = models.CharField(max_length=15, null=False, blank=False, verbose_name='Nombre del paciente')
    Apeterno = models.CharField(max_length=15, null=False, blank=False,  verbose_name='Apellido Paterno')
    Amaterno = models.CharField(max_length=15, null=False, blank=False,  verbose_name='Apellido Materno')
    FecNacimiento = models.DateTimeField(verbose_name='Fecha de nacimiento', null=False, blank=False)
    Edad = models.IntegerField(null=False, blank=False, verbose_name='Edad del paciente')
    Sexo = models.CharField(max_length=10, verbose_name='Sexo', null=False, blank=False)
    FechaConsulta = models.DateTimeField(verbose_name='Fecha de la Consulta', null=False, blank=False)
    TotalConsulta = models.DecimalField(decimal_places=2 ,max_digits=10, null=False, blank=False, verbose_name='Total a pagar por la consulta')