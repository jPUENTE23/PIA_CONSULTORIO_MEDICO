from attr import attrs
from django import forms
from .models import Cita, Doctor

# class citaForm (forms.ModelForm):
#     class Meta:
        
#         model = Cita
        
#         fields = [
#             'DoctAsig',
#             'NomPaciente',
#             'Apeterno',
#             'Amaterno',
#             'FecNacimiento',
#             'Edad',
#             'Sexo',
#             'FechaConsulta',
#             'TotalConsulta',
#         ]

#         labels = {
#             'DoctAsig' : 'Doctor Asigando',
#             'NomPaciente': 'Nombre del Paciente',
#             'Apeterno': 'Apellido Paterno',
#             'Amaterno': 'Apellido Materno',
#             'FecNacimiento': 'Fecha de Nacimiento',
#             'Edad': 'Edad',
#             'Sexo': 'Sexo',
#             'FechaConsulta': 'Fecha de Consulta',
#             'TotalConsulta':  'Total Consulta'
#         }

#         widgets = {
#              'DoctAsig': forms.Select(attrs={'class':'form-control'}),
#              'NomPaciente': forms.TextInput(attrs={'class':'form-control'}),
#              'Apeterno': forms.TextInput(attrs={'class':'form-control'}),
#              'Amaterno': forms.TextInput(attrs={'class':'form-control'}),
#              'FecNacimiento':forms.DateField(attrs={'class':'form-control'}),
#              'Edad': forms.TextInput(attrs={'class':'form-control'}),
#              'Sexo': forms.TextInput(attrs={'class':'form-control'}),
#              'FechaConsulta': forms.DateTimeField(attrs={'class':'form-control'}),
#              'TotalConsulta': forms.TextInput(attrs={'class':'form-control'})
#         }


