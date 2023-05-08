from django.urls import path

from .views import DokterAPIView


urlpatterns = [
    path('dokter/', DokterAPIView.as_view(), name='dokter_view_api')
]
