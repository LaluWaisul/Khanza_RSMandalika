from rest_framework import serializers

from .models import Dokter


class DokterSerializer(serializers.Serializer):
    kd_dokter = serializers.CharField()
    nm_dokter = serializers.CharField()
    kd_sps__nm_sps = serializers.CharField()
    jadwal__kd_poli__nm_poli = serializers.CharField()