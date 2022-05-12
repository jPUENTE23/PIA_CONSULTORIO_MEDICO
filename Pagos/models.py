from django.db import models
from Citas.models import Cita

# Create your models here.
class Pagos(models.Model):
    IdPago = models.AutoField(primary_key=True, verbose_name='Id de la cita')
    NoCita = models.ForeignKey(Cita, blank=False, verbose_name='Numero de cita correspondiente', on_delete=models.CASCADE)
    MontoPagar = models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Monto que se requiere pagar')
    fechaEmision = models.DateTimeField(verbose_name='Fecha en que se emtio el pago', null=True)
    Pagado = models.DecimalField(decimal_places=2 ,max_digits=10, verbose_name='Monto pagado por el paciente')
