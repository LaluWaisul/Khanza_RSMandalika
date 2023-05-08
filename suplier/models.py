from django.db import models

# Create your models here.
class Datasuplier(models.Model):
    kode_suplier = models.CharField(primary_key=True, max_length=5)
    nama_suplier = models.CharField(max_length=50, blank=True, null=True)
    alamat = models.CharField(max_length=50, blank=True, null=True)
    kota = models.CharField(max_length=20, blank=True, null=True)
    no_telp = models.CharField(max_length=13, blank=True, null=True)
    nama_bank = models.CharField(max_length=30, blank=True, null=True)
    rekening = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datasuplier'

class InventarisSuplier(models.Model):
    kode_suplier = models.CharField(primary_key=True, max_length=5)
    nama_suplier = models.CharField(max_length=50, blank=True, null=True)
    alamat = models.CharField(max_length=50, blank=True, null=True)
    kota = models.CharField(max_length=20, blank=True, null=True)
    no_telp = models.CharField(max_length=13, blank=True, null=True)
    nama_bank = models.CharField(max_length=30, blank=True, null=True)
    rekening = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventaris_suplier'
        
        
class InventarisProdusen(models.Model):
    kode_produsen = models.CharField(primary_key=True, max_length=10)
    nama_produsen = models.CharField(max_length=40, blank=True, null=True)
    alamat_produsen = models.CharField(max_length=70, blank=True, null=True)
    no_telp = models.CharField(max_length=13, blank=True, null=True)
    email = models.CharField(max_length=25, blank=True, null=True)
    website_produsen = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventaris_produsen'


class Ipsrssuplier(models.Model):
    kode_suplier = models.CharField(primary_key=True, max_length=5)
    nama_suplier = models.CharField(max_length=50, blank=True, null=True)
    alamat = models.CharField(max_length=50, blank=True, null=True)
    kota = models.CharField(max_length=20, blank=True, null=True)
    no_telp = models.CharField(max_length=13, blank=True, null=True)
    nama_bank = models.CharField(max_length=30, blank=True, null=True)
    rekening = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ipsrssuplier'
        
        
class Pemberihibah(models.Model):
    kode_pemberi = models.CharField(primary_key=True, max_length=5)
    nama_pemberi = models.CharField(max_length=50, blank=True, null=True)
    alamat = models.CharField(max_length=50, blank=True, null=True)
    kota = models.CharField(max_length=20, blank=True, null=True)
    no_telp = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pemberihibah'


class Industrifarmasi(models.Model):
    kode_industri = models.CharField(primary_key=True, max_length=5)
    nama_industri = models.CharField(max_length=50, blank=True, null=True)
    alamat = models.CharField(max_length=50, blank=True, null=True)
    kota = models.CharField(max_length=20, blank=True, null=True)
    no_telp = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'industrifarmasi'

