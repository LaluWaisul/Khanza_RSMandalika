from django.db import models

# Create your models here.

class KeslingLimbahB3Medis(models.Model):
    nip = models.OneToOneField('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', primary_key=True)
    tanggal = models.DateTimeField()
    jmllimbah = models.FloatField(blank=True, null=True)
    tujuan_penyerahan = models.CharField(max_length=50, blank=True, null=True)
    bukti_dokumen = models.CharField(max_length=20, blank=True, null=True)
    sisa_di_tps = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kesling_limbah_b3medis'
        unique_together = (('nip', 'tanggal'),)


class KeslingLimbahDomestik(models.Model):
    nip = models.OneToOneField('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', primary_key=True)
    tanggal = models.DateTimeField()
    jumlahlimbah = models.FloatField(blank=True, null=True)
    tanggalangkut = models.DateTimeField(blank=True, null=True)
    keterangan = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kesling_limbah_domestik'
        unique_together = (('nip', 'tanggal'),)


class KeslingMutuAirLimbah(models.Model):
    nip = models.OneToOneField('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', primary_key=True)
    tanggal = models.DateTimeField()
    meteran = models.FloatField(blank=True, null=True)
    jumlahharian = models.FloatField(blank=True, null=True)
    ph = models.FloatField(blank=True, null=True)
    suhu = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kesling_mutu_air_limbah'
        unique_together = (('nip', 'tanggal'),)


class KeslingPemakaianAirPdam(models.Model):
    nip = models.OneToOneField('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', primary_key=True)
    tanggal = models.DateTimeField()
    meteran = models.FloatField(blank=True, null=True)
    jumlahharian = models.FloatField(blank=True, null=True)
    keterangan = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kesling_pemakaian_air_pdam'
        unique_together = (('nip', 'tanggal'),)


class KeslingPemakaianAirTanah(models.Model):
    nip = models.OneToOneField('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', primary_key=True)
    tanggal = models.DateTimeField()
    meteran = models.FloatField(blank=True, null=True)
    jumlahharian = models.FloatField(blank=True, null=True)
    keterangan = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kesling_pemakaian_air_tanah'
        unique_together = (('nip', 'tanggal'),)


class KeslingPestControl(models.Model):
    nip = models.OneToOneField('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', primary_key=True)
    tanggal = models.DateTimeField()
    rincian_kegiatan = models.TextField(blank=True, null=True)
    rekomendasi = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kesling_pest_control'
        unique_together = (('nip', 'tanggal'),)


