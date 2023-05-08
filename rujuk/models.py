from django.db import models

# Create your models here.

class ResumePasien(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    kd_dokter = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter')
    keluhan_utama = models.TextField()
    jalannya_penyakit = models.TextField()
    pemeriksaan_penunjang = models.TextField()
    hasil_laborat = models.TextField()
    diagnosa_utama = models.CharField(max_length=80)
    kd_diagnosa_utama = models.CharField(max_length=10)
    diagnosa_sekunder = models.CharField(max_length=80)
    kd_diagnosa_sekunder = models.CharField(max_length=10)
    diagnosa_sekunder2 = models.CharField(max_length=80)
    kd_diagnosa_sekunder2 = models.CharField(max_length=10)
    diagnosa_sekunder3 = models.CharField(max_length=80)
    kd_diagnosa_sekunder3 = models.CharField(max_length=10)
    diagnosa_sekunder4 = models.CharField(max_length=80)
    kd_diagnosa_sekunder4 = models.CharField(max_length=10)
    prosedur_utama = models.CharField(max_length=80)
    kd_prosedur_utama = models.CharField(max_length=8)
    prosedur_sekunder = models.CharField(max_length=80)
    kd_prosedur_sekunder = models.CharField(max_length=8)
    prosedur_sekunder2 = models.CharField(max_length=80)
    kd_prosedur_sekunder2 = models.CharField(max_length=8)
    prosedur_sekunder3 = models.CharField(max_length=80)
    kd_prosedur_sekunder3 = models.CharField(max_length=8)
    kondisi_pulang = models.CharField(max_length=9)
    obat_pulang = models.TextField()

    class Meta:
        managed = False
        db_table = 'resume_pasien'


class Rujuk(models.Model):
    no_rujuk = models.CharField(max_length=40)
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', blank=True, null=True)
    rujuk_ke = models.CharField(max_length=150, blank=True, null=True)
    tgl_rujuk = models.DateField(blank=True, null=True)
    keterangan_diagnosa = models.TextField(blank=True, null=True)
    kd_dokter = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter', blank=True, null=True)
    kat_rujuk = models.CharField(max_length=9, blank=True, null=True)
    ambulance = models.CharField(max_length=7, blank=True, null=True)
    keterangan = models.TextField(blank=True, null=True)
    jam = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rujuk'


class RujukMasuk(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    perujuk = models.CharField(max_length=60, blank=True, null=True)
    alamat = models.CharField(max_length=70)
    no_rujuk = models.CharField(max_length=40)
    jm_perujuk = models.FloatField()
    dokter_perujuk = models.CharField(max_length=50, blank=True, null=True)
    kd_penyakit = models.ForeignKey('diagnosa.Penyakit', on_delete=models.DO_NOTHING, db_column='kd_penyakit', blank=True, null=True)
    kategori_rujuk = models.CharField(max_length=9, blank=True, null=True)
    keterangan = models.CharField(max_length=200, blank=True, null=True)
    no_balasan = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rujuk_masuk'


class RujukanInternalPoli(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    kd_dokter = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter')
    kd_poli = models.ForeignKey('bangsal.Poliklinik', on_delete=models.DO_NOTHING, db_column='kd_poli', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rujukan_internal_poli'
        unique_together = (('no_rawat', 'kd_dokter'),)


class RujukanranapDokterRs(models.Model):
    tanggal = models.DateField(primary_key=True)
    kd_dokter = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter')
    no_rkm_medis = models.ForeignKey('pasien.Pasien', on_delete=models.DO_NOTHING, db_column='no_rkm_medis')
    kd_kamar = models.ForeignKey('bangsal.Kamar', on_delete=models.DO_NOTHING, db_column='kd_kamar')
    jasarujuk = models.FloatField()

    class Meta:
        managed = False
        db_table = 'rujukanranap_dokter_rs'
        unique_together = (('tanggal', 'kd_dokter', 'no_rkm_medis', 'kd_kamar'),)


class SisruteRujukanKeluar(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    no_rujuk = models.CharField(max_length=40)
    no_rkm_medis = models.CharField(max_length=15)
    nm_pasien = models.CharField(max_length=40)
    no_ktp = models.CharField(max_length=20)
    no_peserta = models.CharField(max_length=25)
    jk = models.CharField(max_length=1)
    tgl_lahir = models.DateField()
    tmp_lahir = models.CharField(max_length=15)
    alamat = models.CharField(max_length=200)
    no_tlp = models.CharField(max_length=40)
    jns_rujukan = models.CharField(max_length=21)
    tgl_rujuk = models.DateTimeField()
    kd_faskes_tujuan = models.CharField(max_length=12)
    nm_faskes_tujuan = models.CharField(max_length=200)
    kd_alasan = models.CharField(max_length=5)
    alasan_rujuk = models.CharField(max_length=150)
    alasan_lainnya = models.CharField(max_length=50)
    kd_diagnosa = models.CharField(max_length=10)
    diagnosa_rujuk = models.TextField()
    nik_dokter = models.CharField(max_length=20)
    dokter_perujuk = models.CharField(max_length=50)
    nik_petugas = models.CharField(max_length=20)
    petugas_entry = models.CharField(max_length=50)
    anamnesis_pemeriksaan = models.TextField()
    kesadaran = models.CharField(max_length=14)
    tekanan_darah = models.CharField(max_length=7)
    nadi = models.CharField(max_length=3)
    suhu = models.CharField(max_length=5)
    respirasi = models.CharField(max_length=3)
    keadaan_umum = models.TextField()
    tingkat_nyeri = models.CharField(max_length=14)
    alergi = models.CharField(max_length=50)
    laboratorium = models.TextField()
    radiologi = models.TextField()
    terapitindakan = models.TextField()

    class Meta:
        managed = False
        db_table = 'sisrute_rujukan_keluar'

