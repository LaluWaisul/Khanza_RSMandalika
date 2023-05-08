from django.db import models

# Create your models here.


class MasterTindakan(models.Model):
    nama = models.CharField(unique=True, max_length=50)
    jm = models.FloatField()
    jns = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'master_tindakan'


class Tindakan(models.Model):
    tgl = models.DateTimeField(primary_key=True)
    id = models.ForeignKey('pegawai.Pegawai', on_delete=models.DO_NOTHING, db_column='id')
    tnd = models.IntegerField()
    jm = models.FloatField()
    nm_pasien = models.CharField(max_length=30)
    kamar = models.CharField(max_length=20)
    diagnosa = models.CharField(max_length=50)
    jmlh = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tindakan'
        unique_together = (('tgl', 'id', 'tnd', 'nm_pasien'),)
        
        
class Icd9(models.Model):
    kode = models.CharField(primary_key=True, max_length=8)
    deskripsi_panjang = models.CharField(max_length=250, blank=True, null=True)
    deskripsi_pendek = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'icd9'

