from django.db import models

# Create your models here.


class ParkirJenis(models.Model):
    kd_parkir = models.CharField(primary_key=True, max_length=5)
    jns_parkir = models.CharField(max_length=50)
    biaya = models.FloatField()
    jenis = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'parkir_jenis'


class Parkir(models.Model):
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    nomer_kartu = models.CharField(max_length=5, blank=True, null=True)
    kd_parkir = models.ForeignKey('ParkirJenis', on_delete=models.DO_NOTHING, db_column='kd_parkir', blank=True, null=True)
    no_kendaraan = models.CharField(primary_key=True, max_length=15)
    tgl_masuk = models.DateField()
    jam_masuk = models.TimeField()
    tgl_keluar = models.DateField(blank=True, null=True)
    jam_keluar = models.TimeField(blank=True, null=True)
    lama_parkir = models.IntegerField(blank=True, null=True)
    ttl_biaya = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parkir'
        unique_together = (('no_kendaraan', 'tgl_masuk', 'jam_masuk'),)


class ParkirBarcode(models.Model):
    kode_barcode = models.CharField(primary_key=True, max_length=15)
    nomer_kartu = models.CharField(unique=True, max_length=5)

    class Meta:
        managed = False
        db_table = 'parkir_barcode'

