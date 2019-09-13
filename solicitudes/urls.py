from django.urls import path
from .views import SolicitudDetail,SolicitudList
urlpatterns = [
    path('<int:pk>/', SolicitudDetail.as_view()),
    path('', SolicitudList.as_view()),
]