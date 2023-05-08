from django.urls import path, re_path

from .views import RegPasienIGDView, ListPasienAPIView, PengkajianKeperawatanView


urlpatterns = [
    path('listpasien/', RegPasienIGDView.as_view(), name='listpasien_view'),
    path('pengkajianpasien/<slug:norawat>/', PengkajianKeperawatanView.as_view(), name='pengkajianpasien_view'),
    
    path('listpasienapi/', ListPasienAPIView.as_view(), name='listpasien_apiview')
]
