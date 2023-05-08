from django.db import models

# Create your models here.

class K3RsBagianTubuh(models.Model):
    kode_bagian = models.CharField(primary_key=True, max_length=5)
    bagian_tubuh = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'k3rs_bagian_tubuh'


class K3RsDampakCidera(models.Model):
    kode_dampak = models.CharField(primary_key=True, max_length=5)
    dampak_cidera = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'k3rs_dampak_cidera'


class K3RsJenisCidera(models.Model):
    kode_cidera = models.CharField(primary_key=True, max_length=5)
    jenis_cidera = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'k3rs_jenis_cidera'


class K3RsJenisLuka(models.Model):
    kode_luka = models.CharField(primary_key=True, max_length=5)
    jenis_luka = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'k3rs_jenis_luka'


class K3RsJenisPekerjaan(models.Model):
    kode_pekerjaan = models.CharField(primary_key=True, max_length=5)
    jenis_pekerjaan = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'k3rs_jenis_pekerjaan'


class K3RsLokasiKejadian(models.Model):
    kode_lokasi = models.CharField(primary_key=True, max_length=5)
    lokasi_kejadian = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'k3rs_lokasi_kejadian'


class K3RsPenyebab(models.Model):
    kode_penyebab = models.CharField(primary_key=True, max_length=5)
    penyebab_kecelakaan = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'k3rs_penyebab'


class K3RsPeristiwa(models.Model):
    no_k3rs = models.CharField(primary_key=True, max_length=20)
    tgl_insiden = models.DateField()
    waktu_insiden = models.TimeField()
    kode_pekerjaan = models.ForeignKey(K3RsJenisPekerjaan, on_delete=models.DO_NOTHING, db_column='kode_pekerjaan')
    tgl_pelaporan = models.DateField()
    waktu_pelaporan = models.TimeField()
    kode_lokasi = models.ForeignKey(K3RsLokasiKejadian, on_delete=models.DO_NOTHING, db_column='kode_lokasi')
    kronologi_kejadian = models.CharField(max_length=300)
    kode_penyebab = models.ForeignKey(K3RsPenyebab, on_delete=models.DO_NOTHING, db_column='kode_penyebab')
    nik = models.ForeignKey('pegawai.Pegawai', on_delete=models.DO_NOTHING, db_column='nik', related_name='nik_k3rs_peristiwa')
    kategori_cidera = models.CharField(max_length=6)
    kode_cidera = models.ForeignKey(K3RsJenisCidera, on_delete=models.DO_NOTHING, db_column='kode_cidera')
    kode_luka = models.ForeignKey(K3RsJenisLuka, on_delete=models.DO_NOTHING, db_column='kode_luka')
    kode_bagian = models.ForeignKey(K3RsBagianTubuh, on_delete=models.DO_NOTHING, db_column='kode_bagian')
    lt = models.IntegerField()
    penyebab_langsung_kondisi = models.CharField(max_length=100)
    penyebab_langsung_tindakan = models.CharField(max_length=100)
    penyebab_tidak_langsung_pribadi = models.CharField(max_length=100)
    penyebab_tidak_langsung_pekerjaan = models.CharField(max_length=100)
    barang_bukti = models.CharField(max_length=5)
    kode_dampak = models.ForeignKey(K3RsDampakCidera, on_delete=models.DO_NOTHING, db_column='kode_dampak')
    nik_pelapor = models.ForeignKey('pegawai.Pegawai', on_delete=models.DO_NOTHING, db_column='nik_pelapor', related_name='nik_pelapor_k3rs_peristiwa')
    perbaikan_jenis_tindakan = models.CharField(max_length=19)
    perbaikan_rencana_tindakan = models.CharField(max_length=200)
    perbaikan_target = models.DateField()
    perbaikan_wewenang = models.CharField(max_length=100)
    nik_timk3 = models.ForeignKey('pegawai.Pegawai', on_delete=models.DO_NOTHING, db_column='nik_timk3', related_name='nik_timk3_k3rs_peristiwa')
    catatan = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'k3rs_peristiwa'


