from rest_framework import serializers
from ranap.serializers import PasienSerializer
# from khanza.pegawai.models import Dokter

from .models import BookingPeriksa, BookingRegistrasi, RegPeriksa


class BookingPeriksaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingPeriksa
        fields = '__all__'


class BookingRegistrasiSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingRegistrasi
        fields = '__all__'


    
class JadwalSerializer(serializers.Serializer):
    kd_dokter = serializers.CharField()
    nm_dokter = serializers.CharField()
    tanggal_periksa = serializers.DateField()
    jam_mulai = serializers.TimeField()
    jam_selesai = serializers.TimeField()
    kd_poli = serializers.CharField()
    kuota = serializers.IntegerField()
    daftar = serializers.IntegerField()
    status = serializers.CharField()
    
    

class RegistrasiPeriksaSerializer(serializers.Serializer):
    kd_dokter = serializers.CharField()
    kd_dokter__nm_dokter = serializers.CharField()
    daftar = serializers.IntegerField()
    
    
class JadwalDokterSerializer(serializers.Serializer):
    hari_kerja = serializers.CharField()
    kd_dokter__nm_dokter = serializers.CharField()
    kd_poli__nm_poli = serializers.CharField()
    jam_mulai = serializers.TimeField()
    jam_selesai = serializers.TimeField()
    kuota = serializers.IntegerField()
    pasien_terdaftar = serializers.IntegerField()
    
class RegPeriksaSerializer(serializers.ModelSerializer):
    no_rkm_medis = PasienSerializer()
    class Meta:
        model = RegPeriksa
        fields = ['no_rawat', 'no_rkm_medis', 'no_rkm_medis', 'tgl_registrasi', 'jam_reg', 'kd_poli', 'kd_dokter']