from django.views.generic import RedirectView
from rest_framework.routers import SimpleRouter
from .views import SolicitudViewsets, UserViewSet

router = SimpleRouter()
router.register('users', UserViewSet, base_name='users')
router.register('solicitudes', SolicitudViewsets, base_name='solicitudes')
urlpatterns = router.urls