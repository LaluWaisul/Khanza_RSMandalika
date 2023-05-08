from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    BookingPeriksaView, 
    BookingRegistrasiDetailView, 
    BookingRegistrasiListView, 
    JadwalRalan, KunjunganView, 
    RegistrasiPeriksaView, 
    BookingPeriksaAPIView,
    JadwalDokterRalanView,
    JadwalDokterRalanAPIView,
    RegPasienAPIView,
    
    RegPeriksaView,
    RegPasienView
    )


urlpatterns = [
    path('bookingapi/', BookingPeriksaAPIView.as_view(), name='booking_api_view'),
    path('booking/', BookingPeriksaView.as_view(), name='booking_view'),
    path('kunjungan/', KunjunganView.as_view(), name='kunjungan_view'),
    path('jadwal/', JadwalRalan.as_view(), name='jadwal_view'),
    path('jadwaldokter/', JadwalDokterRalanView.as_view(), name='jadwal_dokter_view'),
    path('jadwaldokterapi/', JadwalDokterRalanAPIView.as_view(), name='jadwal_dokter_api'),
    path('regperiksa/', RegistrasiPeriksaView.as_view(), name='regperiksa_view'),
    path('bookingreg/', BookingRegistrasiListView.as_view(), name='bookingreg_view'),
    path('bookingreg/<int:pk>/', BookingRegistrasiDetailView.as_view(), name='bookingreg_detail_view'),
    path('daftarpasienapi/', RegPasienAPIView.as_view(), name='daftarpasien_view'),
    
    #render html
    path('registrasi/', RegPeriksaView.as_view(), name='registrasi_view'),
    path('daftarpasien/', RegPasienView.as_view(), name='daftarpasien_view'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
