from django.db import models

# Create your models here.


class SkriningGizi(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    tanggal = models.DateTimeField()
    skrining_bb = models.CharField(max_length=5, blank=True, null=True)
    skrining_tb = models.CharField(max_length=5, blank=True, null=True)
    alergi = models.CharField(max_length=25, blank=True, null=True)
    parameter_imt = models.CharField(max_length=30, blank=True, null=True)
    skor_imt = models.CharField(max_length=5, blank=True, null=True)
    parameter_bb = models.CharField(max_length=18, blank=True, null=True)
    skor_bb = models.CharField(max_length=5, blank=True, null=True)
    parameter_penyakit = models.CharField(max_length=33, blank=True, null=True)
    skor_penyakit = models.CharField(max_length=5, blank=True, null=True)
    skor_total = models.CharField(max_length=5, blank=True, null=True)
    parameter_total = models.CharField(max_length=200, blank=True, null=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skrining_gizi'
        unique_together = (('no_rawat', 'tanggal'),)


class AsuhanGizi(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    tanggal = models.DateField()
    antropometri_bb = models.CharField(max_length=5, blank=True, null=True)
    antropometri_tb = models.CharField(max_length=5, blank=True, null=True)
    antropometri_imt = models.CharField(max_length=5, blank=True, null=True)
    antropometri_lla = models.CharField(max_length=5, blank=True, null=True)
    antropometri_tl = models.CharField(max_length=5, blank=True, null=True)
    antropometri_ulna = models.CharField(max_length=5)
    antropometri_bbideal = models.CharField(max_length=5)
    antropometri_bbperu = models.CharField(max_length=5)
    antropometri_tbperu = models.CharField(max_length=5)
    antropometri_bbpertb = models.CharField(max_length=5)
    antropometri_llaperu = models.CharField(max_length=5)
    biokimia = models.CharField(max_length=100, blank=True, null=True)
    fisik_klinis = models.CharField(max_length=100, blank=True, null=True)
    alergi_telur = models.CharField(max_length=5, blank=True, null=True)
    alergi_susu_sapi = models.CharField(max_length=5, blank=True, null=True)
    alergi_kacang = models.CharField(max_length=5, blank=True, null=True)
    alergi_gluten = models.CharField(max_length=5, blank=True, null=True)
    alergi_udang = models.CharField(max_length=5, blank=True, null=True)
    alergi_ikan = models.CharField(max_length=5, blank=True, null=True)
    alergi_hazelnut = models.CharField(max_length=5, blank=True, null=True)
    pola_makan = models.CharField(max_length=100, blank=True, null=True)
    riwayat_personal = models.CharField(max_length=100, blank=True, null=True)
    diagnosis = models.CharField(max_length=100, blank=True, null=True)
    intervensi_gizi = models.CharField(max_length=100, blank=True, null=True)
    monitoring_evaluasi = models.CharField(max_length=100, blank=True, null=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip')

    class Meta:
        managed = False
        db_table = 'asuhan_gizi'
        unique_together = (('no_rawat', 'tanggal'),)


class Diet(models.Model):
    kd_diet = models.CharField(primary_key=True, max_length=3)
    nama_diet = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'diet'


class JamDietPasien(models.Model):
    waktu = models.CharField(primary_key=True, max_length=6)
    jam = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jam_diet_pasien'

        
class DetailBeriDiet(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    kd_kamar = models.ForeignKey('bangsal.Kamar', on_delete=models.DO_NOTHING, db_column='kd_kamar')
    tanggal = models.DateField()
    waktu = models.ForeignKey('JamDietPasien', on_delete=models.DO_NOTHING, db_column='waktu')
    kd_diet = models.ForeignKey('Diet', on_delete=models.DO_NOTHING, db_column='kd_diet')

    class Meta:
        managed = False
        db_table = 'detail_beri_diet'
        unique_together = (('no_rawat', 'kd_kamar', 'tanggal', 'waktu', 'kd_diet'),)


class MonitoringAsuhanGizi(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    tanggal = models.DateTimeField()
    monitoring = models.CharField(max_length=200, blank=True, null=True)
    evaluasi = models.CharField(max_length=200, blank=True, null=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monitoring_asuhan_gizi'
        unique_together = (('no_rawat', 'tanggal'),)
