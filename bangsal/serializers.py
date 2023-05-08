from rest_framework import serializers

from .models import Kamar


class InformasiTempatTidurSerializer(serializers.Serializer):
    kd_bangsal__nm_bangsal = serializers.CharField()
    trf_kamar = serializers.FloatField()
    jlh_total_kamar = serializers.IntegerField()
    jlh_kamar_kosong = serializers.IntegerField()
    jlh_kamar_isi = serializers.IntegerField()
    jlh_kamar_booking = serializers.IntegerField()