from django.views.generic import RedirectView
from rest_framework.routers import SimpleRouter
from .views import SolicitudViewsets, UserViewSet, UserList, PruebaViewsets, TipoPruebaViewsets, \
    TipoAplicacionViewsets, TipoEjecucionViewsets, EjecutorViewsets, AplicacionViewsets, HerramientaViewsets

router = SimpleRouter()
router.register('users', UserViewSet, base_name='users')
router.register('solicitudes', SolicitudViewsets, base_name='solicitudes')
router.register('pruebas', PruebaViewsets, base_name='pruebas')
router.register('tipopruebas', TipoPruebaViewsets, base_name='tipopruebas')
router.register('tipoejecucion', TipoEjecucionViewsets, base_name='tipoejecucion')
router.register('tipoaplicacion', TipoAplicacionViewsets, base_name='tipoaplicacion')
router.register('ejecutor',EjecutorViewsets, base_name='ejecutor')
router.register('aplicacion',AplicacionViewsets, base_name='aplicacion')
router.register('herramienta',HerramientaViewsets, base_name='herramienta')
router.register('users', UserList, base_name='users')
urlpatterns = router.urls