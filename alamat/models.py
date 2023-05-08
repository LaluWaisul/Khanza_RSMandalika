from django.db import models

# Create your models here.

class Kelurahan(models.Model):
    kd_kel = models.AutoField(primary_key=True)
    kd_kec = models.ForeignKey('Kecamatan', on_delete=models.DO_NOTHING, blank=True, null=True)
    nm_kel = models.CharField(unique=True, max_length=60)

    class Meta:
        managed = True
        db_table = 'kelurahan'
        
class Kecamatan(models.Model):
    kd_kec = models.AutoField(primary_key=True)
    kd_kab = models.ForeignKey('Kabupaten', on_delete=models.DO_NOTHING, blank=True, null=True)
    nm_kec = models.CharField(unique=True, max_length=60)

    class Meta:
        managed = True
        db_table = 'kecamatan'
        
        
class Kabupaten(models.Model):
    kd_kab = models.AutoField(primary_key=True)
    kd_prop = models.ForeignKey('Propinsi', on_delete=models.DO_NOTHING, blank=True, null=True)
    nm_kab = models.CharField(unique=True, max_length=60)

    class Meta:
        managed = True
        db_table = 'kabupaten'


class Propinsi(models.Model):
    kd_prop = models.AutoField(primary_key=True)
    nm_prop = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'propinsi'


class SetAlamatPasien(models.Model):
    kelurahan = models.CharField(max_length=5, blank=True, null=True)
    kecamatan = models.CharField(max_length=5, blank=True, null=True)
    kabupaten = models.CharField(max_length=5, blank=True, null=True)
    propinsi = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'set_alamat_pasien'
        
        
######## DUKCAPIL

class BridgingDukcapil(models.Model):
    no_rkm_medis = models.OneToOneField('pasien.Pasien', on_delete=models.DO_NOTHING, db_column='no_rkm_medis', primary_key=True)
    no_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bridging_dukcapil'
        
        
class LogDukcapil(models.Model):
    no_ktp = models.CharField(primary_key=True, max_length=20)
    tanggal = models.DateTimeField()
    user = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'log_dukcapil_aceh'
        unique_together = (('no_ktp', 'tanggal', 'user'),)


        



