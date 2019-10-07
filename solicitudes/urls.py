from django.views.generic import RedirectView
from rest_framework.routers import SimpleRouter
from .views import SolicitudViewsets, UserViewSet, UserList

router = SimpleRouter()
router.register('users', UserViewSet, base_name='users')
router.register('solicitudes', SolicitudViewsets, base_name='solicitudes')
router.register('users', UserList, base_name='users')
urlpatterns = router.urls