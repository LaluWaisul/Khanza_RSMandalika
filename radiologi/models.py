from django.db import models

# Create your models here.


class JnsPerawatanRadiologi(models.Model):
    kd_jenis_prw = models.CharField(primary_key=True, max_length=15)
    nm_perawatan = models.CharField(max_length=80, blank=True, null=True)
    bagian_rs = models.FloatField(blank=True, null=True)
    bhp = models.FloatField()
    tarif_perujuk = models.FloatField()
    tarif_tindakan_dokter = models.FloatField()
    tarif_tindakan_petugas = models.FloatField(blank=True, null=True)
    kso = models.FloatField(blank=True, null=True)
    menejemen = models.FloatField(blank=True, null=True)
    total_byr = models.FloatField(blank=True, null=True)
    kd_pj = models.ForeignKey('asuransi.Penjab', on_delete=models.DO_NOTHING, db_column='kd_pj')
    status = models.CharField(max_length=1)
    kelas = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'jns_perawatan_radiologi'


class PermintaanRadiologi(models.Model):
    noorder = models.CharField(primary_key=True, max_length=15)
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat')
    tgl_permintaan = models.DateField()
    jam_permintaan = models.TimeField()
    tgl_sampel = models.DateField()
    jam_sampel = models.TimeField()
    tgl_hasil = models.DateField()
    jam_hasil = models.TimeField()
    dokter_perujuk = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='dokter_perujuk')
    status = models.CharField(max_length=5)
    informasi_tambahan = models.CharField(max_length=60)
    diagnosa_klinis = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'permintaan_radiologi'


class PermintaanPemeriksaanRadiologi(models.Model):
    noorder = models.OneToOneField('PermintaanRadiologi', on_delete=models.DO_NOTHING, db_column='noorder', primary_key=True)
    kd_jenis_prw = models.ForeignKey(JnsPerawatanRadiologi, on_delete=models.DO_NOTHING, db_column='kd_jenis_prw')
    stts_bayar = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permintaan_pemeriksaan_radiologi'
        unique_together = (('noorder', 'kd_jenis_prw'),)


class PeriksaRadiologi(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip')
    kd_jenis_prw = models.ForeignKey(JnsPerawatanRadiologi, on_delete=models.DO_NOTHING, db_column='kd_jenis_prw')
    tgl_periksa = models.DateField()
    jam = models.TimeField()
    dokter_perujuk = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='dokter_perujuk', related_name='dokter_perujuk_periksa_radiologi')
    bagian_rs = models.FloatField()
    bhp = models.FloatField()
    tarif_perujuk = models.FloatField()
    tarif_tindakan_dokter = models.FloatField()
    tarif_tindakan_petugas = models.FloatField()
    kso = models.FloatField(blank=True, null=True)
    menejemen = models.FloatField(blank=True, null=True)
    biaya = models.FloatField()
    kd_dokter = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter', related_name='kd_dokter_periksa_radiologi')
    status = models.CharField(max_length=5, blank=True, null=True)
    proyeksi = models.CharField(max_length=50)
    kv = models.CharField(db_column='kV', max_length=10)  # Field name made lowercase.
    mas = models.CharField(db_column='mAS', max_length=10)  # Field name made lowercase.
    ffd = models.CharField(db_column='FFD', max_length=10)  # Field name made lowercase.
    bsf = models.CharField(db_column='BSF', max_length=10)  # Field name made lowercase.
    inak = models.CharField(max_length=10)
    jml_penyinaran = models.CharField(max_length=10)
    dosis = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'periksa_radiologi'
        unique_together = (('no_rawat', 'kd_jenis_prw', 'tgl_periksa', 'jam'),)


class GambarRadiologi(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    tgl_periksa = models.DateField()
    jam = models.TimeField()
    lokasi_gambar = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'gambar_radiologi'
        unique_together = (('no_rawat', 'tgl_periksa', 'jam', 'lokasi_gambar'),)


class HasilRadiologi(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    tgl_periksa = models.DateField()
    jam = models.TimeField()
    hasil = models.TextField()

    class Meta:
        managed = False
        db_table = 'hasil_radiologi'
        unique_together = (('no_rawat', 'tgl_periksa', 'jam'),)


class TemporaryPermintaanRadiologi(models.Model):
    no = models.AutoField(primary_key=True)
    temp1 = models.CharField(max_length=1000)
    temp2 = models.CharField(max_length=1000)
    temp3 = models.CharField(max_length=1000)
    temp4 = models.CharField(max_length=1000)
    temp5 = models.CharField(max_length=1000)
    temp6 = models.CharField(max_length=1000)
    temp7 = models.CharField(max_length=1000)
    temp8 = models.CharField(max_length=1000)
    temp9 = models.CharField(max_length=1000)
    temp10 = models.CharField(max_length=1000)
    temp11 = models.CharField(max_length=1000)
    temp12 = models.CharField(max_length=1000)
    temp13 = models.CharField(max_length=1000)
    temp14 = models.CharField(max_length=1000)
    temp15 = models.CharField(max_length=1000)
    temp16 = models.CharField(max_length=100)
    temp17 = models.CharField(max_length=100)
    temp18 = models.CharField(max_length=100)
    temp19 = models.CharField(max_length=100)
    temp20 = models.CharField(max_length=100)
    temp21 = models.CharField(max_length=100)
    temp22 = models.CharField(max_length=100)
    temp23 = models.CharField(max_length=100)
    temp24 = models.CharField(max_length=100)
    temp25 = models.CharField(max_length=100)
    temp26 = models.CharField(max_length=100)
    temp27 = models.CharField(max_length=100)
    temp28 = models.CharField(max_length=100)
    temp29 = models.CharField(max_length=100)
    temp30 = models.CharField(max_length=100)
    temp31 = models.CharField(max_length=100)
    temp32 = models.CharField(max_length=100)
    temp33 = models.CharField(max_length=100)
    temp34 = models.CharField(max_length=100)
    temp35 = models.CharField(max_length=100)
    temp36 = models.CharField(max_length=100)
    temp37 = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'temporary_permintaan_radiologi'


class TemporaryRadiologi(models.Model):
    no = models.AutoField(primary_key=True)
    temp1 = models.CharField(max_length=1000)
    temp2 = models.CharField(max_length=1000)
    temp3 = models.CharField(max_length=1000)
    temp4 = models.CharField(max_length=1000)
    temp5 = models.CharField(max_length=1000)
    temp6 = models.CharField(max_length=1000)
    temp7 = models.CharField(max_length=1000)
    temp8 = models.CharField(max_length=1000)
    temp9 = models.CharField(max_length=1000)
    temp10 = models.CharField(max_length=1000)
    temp11 = models.CharField(max_length=1000)
    temp12 = models.CharField(max_length=1000)
    temp13 = models.CharField(max_length=1000)
    temp14 = models.CharField(max_length=1000)
    temp15 = models.CharField(max_length=1000)
    temp16 = models.CharField(max_length=100)
    temp17 = models.CharField(max_length=100)
    temp18 = models.CharField(max_length=100)
    temp19 = models.CharField(max_length=100)
    temp20 = models.CharField(max_length=100)
    temp21 = models.CharField(max_length=100)
    temp22 = models.CharField(max_length=100)
    temp23 = models.CharField(max_length=100)
    temp24 = models.CharField(max_length=100)
    temp25 = models.CharField(max_length=100)
    temp26 = models.CharField(max_length=100)
    temp27 = models.CharField(max_length=100)
    temp28 = models.CharField(max_length=100)
    temp29 = models.CharField(max_length=100)
    temp30 = models.CharField(max_length=100)
    temp31 = models.CharField(max_length=100)
    temp32 = models.CharField(max_length=100)
    temp33 = models.CharField(max_length=100)
    temp34 = models.CharField(max_length=100)
    temp35 = models.CharField(max_length=100)
    temp36 = models.CharField(max_length=100)
    temp37 = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'temporary_radiologi'




class TemporaryLamaPelayananRadiologi(models.Model):
    no = models.AutoField(primary_key=True)
    temp1 = models.CharField(max_length=1000)
    temp2 = models.CharField(max_length=1000)
    temp3 = models.CharField(max_length=1000)
    temp4 = models.CharField(max_length=1000)
    temp5 = models.CharField(max_length=1000)
    temp6 = models.CharField(max_length=1000)
    temp7 = models.CharField(max_length=1000)
    temp8 = models.CharField(max_length=1000)
    temp9 = models.CharField(max_length=1000)
    temp10 = models.CharField(max_length=1000)
    temp11 = models.CharField(max_length=1000)
    temp12 = models.CharField(max_length=1000)
    temp13 = models.CharField(max_length=1000)
    temp14 = models.CharField(max_length=1000)
    temp15 = models.CharField(max_length=1000)
    temp16 = models.CharField(max_length=100)
    temp17 = models.CharField(max_length=100)
    temp18 = models.CharField(max_length=100)
    temp19 = models.CharField(max_length=100)
    temp20 = models.CharField(max_length=100)
    temp21 = models.CharField(max_length=100)
    temp22 = models.CharField(max_length=100)
    temp23 = models.CharField(max_length=100)
    temp24 = models.CharField(max_length=100)
    temp25 = models.CharField(max_length=100)
    temp26 = models.CharField(max_length=100)
    temp27 = models.CharField(max_length=100)
    temp28 = models.CharField(max_length=100)
    temp29 = models.CharField(max_length=100)
    temp30 = models.CharField(max_length=100)
    temp31 = models.CharField(max_length=100)
    temp32 = models.CharField(max_length=100)
    temp33 = models.CharField(max_length=100)
    temp34 = models.CharField(max_length=100)
    temp35 = models.CharField(max_length=100)
    temp36 = models.CharField(max_length=100)
    temp37 = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'temporary_lama_pelayanan_radiologi'


