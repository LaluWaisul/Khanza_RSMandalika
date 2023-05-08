from django.db import models

# Create your models here.

class Departemen(models.Model):
    dep_id = models.CharField(primary_key=True, max_length=4)
    nama = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'departemen'

    def __str__(self):
        return f'{self.dep_id} - {self.nama}'

class Bidang(models.Model):
    nama = models.CharField(primary_key=True, max_length=15)

    class Meta:
        managed = False
        db_table = 'bidang'
        
    def __str__(self):
        return self.nama


class Bangsal(models.Model):
    kd_bangsal = models.CharField(primary_key=True, max_length=5)
    nm_bangsal = models.CharField(max_length=30, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bangsal'

    def __str__(self):
        return f'{self.kd_bangsal} - {self.nm_bangsal}'

class Poliklinik(models.Model):
    kd_poli = models.CharField(primary_key=True, max_length=5)
    nm_poli = models.CharField(max_length=50, blank=True, null=True)
    registrasi = models.FloatField()
    registrasilama = models.FloatField()
    status = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'poliklinik'
        
    def __str__(self):
        return self.nm_poli

        
class Kamar(models.Model):
    kd_kamar = models.CharField(primary_key=True, max_length=15)
    kd_bangsal = models.ForeignKey(Bangsal, on_delete=models.DO_NOTHING, db_column='kd_bangsal', blank=True, null=True)
    trf_kamar = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=11, blank=True, null=True)
    kelas = models.CharField(max_length=11, blank=True, null=True)
    statusdata = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kamar'
        
    def __str__(self):
        return self.kd_bangsal.nm_bangsal


class SiranapKetersediaanKamar(models.Model):
    kode_ruang_siranap = models.CharField(primary_key=True, max_length=29)
    kelas_ruang_siranap = models.CharField(max_length=21)
    kd_bangsal = models.ForeignKey(Bangsal, on_delete=models.DO_NOTHING, db_column='kd_bangsal')
    kelas = models.CharField(max_length=11)
    kapasitas = models.IntegerField(blank=True, null=True)
    tersedia = models.IntegerField(blank=True, null=True)
    tersediapria = models.IntegerField(blank=True, null=True)
    tersediawanita = models.IntegerField(blank=True, null=True)
    menunggu = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'siranap_ketersediaan_kamar'
        unique_together = (('kode_ruang_siranap', 'kelas_ruang_siranap', 'kd_bangsal', 'kelas'),)


class Indekref(models.Model):
    kdindex = models.ForeignKey(Departemen, on_delete=models.DO_NOTHING, db_column='kdindex')
    n = models.FloatField()
    ttl = models.FloatField()

    class Meta:
        managed = False
        db_table = 'indekref'


class Indexins(models.Model):
    dep = models.OneToOneField(Departemen, on_delete=models.DO_NOTHING, primary_key=True)
    persen = models.FloatField()

    class Meta:
        managed = False
        db_table = 'indexins'


class Indextotal(models.Model):
    kdindex = models.ForeignKey(Departemen, on_delete=models.DO_NOTHING, db_column='kdindex')
    ttl = models.FloatField()

    class Meta:
        managed = False
        db_table = 'indextotal'

