from django.contrib import admin

from Pagos.views import pagos
from .models import Pagos
# Register your models here.


admin.site.register(Pagos)