from rest_framework import serializers
from .models import KamarInap
from pasien.models import Pasien
from ralan.models import RegPeriksa

class PasienSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pasien
        fields = ['no_rkm_medis', 'nm_pasien', 'alamat']
        
class RegPeriksaSerializer(serializers.ModelSerializer):
    no_rkm_medis = PasienSerializer()
    class Meta:
        model = RegPeriksa
        fields =  ['no_rawat', 'no_rkm_medis', 'status_bayar']

class KamarInapSerializer(serializers.ModelSerializer):
    no_rawat = RegPeriksaSerializer()
    kd_kamar = serializers.StringRelatedField()
    class Meta:
        model = KamarInap
        fields = ['no_rawat', 'kd_kamar', 'trf_kamar', 'diagnosa_awal', 'diagnosa_akhir', 'tgl_masuk', 'tgl_keluar', 'ttl_biaya', 'stts_pulang']
        
