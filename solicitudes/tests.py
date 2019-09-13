from django.test import TestCase
from django.contrib.auth.models import User
from .models import Solicitud

# Create your tests here.


class SolicitudesTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Crea Usuario Para Prueba
        cls.test_user_1 = User.objects.create_user(
            username='testuser1', password='abc123'
        )
        cls.test_user_1.save()

        # Crea Solicitud Para Prueba
        cls.test_solicitud = Solicitud.objects.create(
            nombre="prueba 1",
            script="script de prueba",
            descripcion="descripcion de la prueba",
            creado_por=cls.test_user_1,
        )
        cls.test_solicitud.save()

    def test_probar_creacion(self):
        solicitud = Solicitud.objects.get(id=1)
        creado_por = f'{solicitud.creado_por}'
        nombre = f'{solicitud.nombre}'
        script = f'{solicitud.script}'
        descripcion = f'{solicitud.descripcion}'
        self.assertEqual(creado_por, 'testuser1')
        self.assertEqual(nombre, 'prueba 1')
        self.assertEqual(script, 'script de prueba')

        self.assertEqual(descripcion, 'descripcion de la prueba')