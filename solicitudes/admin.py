from django.contrib import admin
from .models import Solicitud, TipoPrueba, TipoAplicacion, Aplicacion, Herramienta, Prueba, TipoEjecucion, Ejecutor

# Register your models here.


admin.site.register(TipoPrueba)
admin.site.register(TipoEjecucion)
admin.site.register(Ejecutor)
admin.site.register(TipoAplicacion)
admin.site.register(Aplicacion)
admin.site.register(Herramienta)
admin.site.register(Prueba)
admin.site.register(Solicitud)
