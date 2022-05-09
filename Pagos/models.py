from django.db import models
from Citas.models import Cita

# Create your models here.
class Pagos(models.Model):
    IdPago = models.AutoField(primary_key=True, verbose_name='Id de la cita')
    IdCita = models.ForeignKey(Cita, null=False, blank=False, verbose_name='Numero de cita correspondiente', on_delete=models.CASCADE)
    MontoPagar = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Monto que se requiere pagar',)
    Pagado = models.DecimalField(decimal_places=2 ,max_digits=10, verbose_name='Monto pagado por el paciente')
