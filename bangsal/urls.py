from django.urls import path

from .views import InformasiTempatTidur, InformasiTempatTidurAPIView


urlpatterns = [
    path('kamar/', InformasiTempatTidur.as_view(), name='kamar_ranap'),
    path('kamarapi/', InformasiTempatTidurAPIView.as_view(), name='kamar_ranap_api'),
]
