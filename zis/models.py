from django.db import models

# Create your models here.

class ZisKeteranganAtapRumahPenerimaDankes(models.Model):
    kode = models.CharField(primary_key=True, max_length=3)
    keterangan = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zis_keterangan_atap_rumah_penerima_dankes'


class ZisKeteranganDapurRumahPenerimaDankes(models.Model):
    kode = models.CharField(primary_key=True, max_length=3)
    keterangan = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zis_keterangan_dapur_rumah_penerima_dankes'


class ZisKeteranganDindingRumahPenerimaDankes(models.Model):
    kode = models.CharField(primary_key=True, max_length=3)
    keterangan = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zis_keterangan_dinding_rumah_penerima_dankes'


class ZisKeteranganElektronikPenerimaDankes(models.Model):
    kode = models.CharField(primary_key=True, max_length=3)
    keterangan = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zis_keterangan_elektronik_penerima_dankes'


class ZisKeteranganJenisSimpananPenerimaDankes(models.Model):
    kode = models.CharField(primary_key=True, max_length=3)
    keterangan = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zis_keterangan_jenis_simpanan_penerima_dankes'


class ZisKeteranganKamarMandiPenerimaDankes(models.Model):
    kode = models.CharField(primary_key=True, max_length=3)
    keterangan = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zis_keterangan_kamar_mandi_penerima_dankes'


class ZisKeteranganKategoriAsnafPenerimaDankes(models.Model):
    kode = models.CharField(primary_key=True, max_length=3)
    keterangan = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zis_keterangan_kategori_asnaf_penerima_dankes'


class ZisKeteranganKategoriPhbsPenerimaDankes(models.Model):
    kode = models.CharField(primary_key=True, max_length=3)
    keterangan = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zis_keterangan_kategori_phbs_penerima_dankes'


class ZisKeteranganKursiRumahPenerimaDankes(models.Model):
    kode = models.CharField(primary_key=True, max_length=3)
    keterangan = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zis_keterangan_kursi_rumah_penerima_dankes'


class ZisKeteranganLantaiRumahPenerimaDankes(models.Model):
    kode = models.CharField(primary_key=True, max_length=3)
    keterangan = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zis_keterangan_lantai_rumah_penerima_dankes'


class ZisKeteranganPatologisPenerimaDankes(models.Model):
    kode = models.CharField(primary_key=True, max_length=3)
    keterangan = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zis_keterangan_patologis_penerima_dankes'


class ZisKeteranganPengeluaranPenerimaDankes(models.Model):
    kode = models.CharField(primary_key=True, max_length=3)
    keterangan = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zis_keterangan_pengeluaran_penerima_dankes'


class ZisKeteranganPenghasilanPenerimaDankes(models.Model):
    kode = models.CharField(primary_key=True, max_length=3)
    keterangan = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zis_keterangan_penghasilan_penerima_dankes'


class ZisKeteranganTernakPenerimaDankes(models.Model):
    kode = models.CharField(primary_key=True, max_length=3)
    keterangan = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zis_keterangan_ternak_penerima_dankes'


class ZisKeteranganUkuranRumahPenerimaDankes(models.Model):
    kode = models.CharField(primary_key=True, max_length=3)
    keterangan = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zis_keterangan_ukuran_rumah_penerima_dankes'
