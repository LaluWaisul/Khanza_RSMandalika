from django.db import models
from datetime import datetime
from .daftarpilihan import *

# Create your models here.

############### MASTER TRIAGE

class EmergencyIndex(models.Model):
    kode_emergency = models.CharField(primary_key=True, max_length=3)
    nama_emergency = models.CharField(max_length=200, blank=True, null=True)
    indek = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emergency_index'


class MasterTriaseMacamKasus(models.Model):
    kode_kasus = models.CharField(primary_key=True, max_length=3)
    macam_kasus = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'master_triase_macam_kasus'


class MasterTriasePemeriksaan(models.Model):
    kode_pemeriksaan = models.CharField(primary_key=True, max_length=3)
    nama_pemeriksaan = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_triase_pemeriksaan'


class MasterTriaseSkala1(models.Model):
    kode_pemeriksaan = models.ForeignKey(MasterTriasePemeriksaan, on_delete=models.DO_NOTHING, db_column='kode_pemeriksaan')
    kode_skala1 = models.CharField(primary_key=True, max_length=3)
    pengkajian_skala1 = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'master_triase_skala1'


class MasterTriaseSkala2(models.Model):
    kode_pemeriksaan = models.ForeignKey(MasterTriasePemeriksaan, on_delete=models.DO_NOTHING, db_column='kode_pemeriksaan')
    kode_skala2 = models.CharField(primary_key=True, max_length=3)
    pengkajian_skala2 = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'master_triase_skala2'


class MasterTriaseSkala3(models.Model):
    kode_pemeriksaan = models.ForeignKey(MasterTriasePemeriksaan, on_delete=models.DO_NOTHING, db_column='kode_pemeriksaan')
    kode_skala3 = models.CharField(primary_key=True, max_length=3)
    pengkajian_skala3 = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'master_triase_skala3'


class MasterTriaseSkala4(models.Model):
    kode_pemeriksaan = models.ForeignKey(MasterTriasePemeriksaan, on_delete=models.DO_NOTHING, db_column='kode_pemeriksaan')
    kode_skala4 = models.CharField(primary_key=True, max_length=3)
    pengkajian_skala4 = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'master_triase_skala4'


class MasterTriaseSkala5(models.Model):
    kode_pemeriksaan = models.ForeignKey(MasterTriasePemeriksaan, on_delete=models.DO_NOTHING, db_column='kode_pemeriksaan')
    kode_skala5 = models.CharField(primary_key=True, max_length=3)
    pengkajian_skala5 = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'master_triase_skala5'


#########################


class DataTriaseIgd(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    tgl_kunjungan = models.DateTimeField()
    cara_masuk = models.CharField(max_length=10)
    alat_transportasi = models.CharField(max_length=7)
    alasan_kedatangan = models.CharField(max_length=14)
    keterangan_kedatangan = models.CharField(max_length=100)
    kode_kasus = models.ForeignKey('MasterTriaseMacamKasus', on_delete=models.DO_NOTHING, db_column='kode_kasus')
    tekanan_darah = models.CharField(max_length=8)
    nadi = models.CharField(max_length=3)
    pernapasan = models.CharField(max_length=3)
    suhu = models.CharField(max_length=5)
    saturasi_o2 = models.CharField(max_length=3)
    nyeri = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'data_triase_igd'


class DataTriaseIgddetailSkala1(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    kode_skala1 = models.ForeignKey('MasterTriaseSkala1', on_delete=models.DO_NOTHING, db_column='kode_skala1')

    class Meta:
        managed = False
        db_table = 'data_triase_igddetail_skala1'
        unique_together = (('no_rawat', 'kode_skala1'),)


class DataTriaseIgddetailSkala2(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    kode_skala2 = models.ForeignKey('MasterTriaseSkala2', on_delete=models.DO_NOTHING, db_column='kode_skala2')

    class Meta:
        managed = False
        db_table = 'data_triase_igddetail_skala2'
        unique_together = (('no_rawat', 'kode_skala2'),)


class DataTriaseIgddetailSkala3(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    kode_skala3 = models.ForeignKey('MasterTriaseSkala3', on_delete=models.DO_NOTHING, db_column='kode_skala3')

    class Meta:
        managed = False
        db_table = 'data_triase_igddetail_skala3'
        unique_together = (('no_rawat', 'kode_skala3'),)


class DataTriaseIgddetailSkala4(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    kode_skala4 = models.ForeignKey('MasterTriaseSkala4', on_delete=models.DO_NOTHING, db_column='kode_skala4')

    class Meta:
        managed = False
        db_table = 'data_triase_igddetail_skala4'
        unique_together = (('no_rawat', 'kode_skala4'),)


class DataTriaseIgddetailSkala5(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    kode_skala5 = models.ForeignKey('MasterTriaseSkala5', on_delete=models.DO_NOTHING, db_column='kode_skala5')

    class Meta:
        managed = False
        db_table = 'data_triase_igddetail_skala5'
        unique_together = (('no_rawat', 'kode_skala5'),)


class DataTriaseIgdprimer(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    keluhan_utama = models.CharField(max_length=400)
    kebutuhan_khusus = models.CharField(max_length=12)
    catatan = models.CharField(max_length=100)
    plan = models.CharField(max_length=16)
    tanggaltriase = models.DateTimeField()
    nik = models.ForeignKey('pegawai.Pegawai', on_delete=models.DO_NOTHING, db_column='nik')

    class Meta:
        managed = False
        db_table = 'data_triase_igdprimer'


class DataTriaseIgdsekunder(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    anamnesa_singkat = models.CharField(max_length=400)
    catatan = models.CharField(max_length=100)
    plan = models.CharField(max_length=11)
    tanggaltriase = models.DateTimeField()
    nik = models.ForeignKey('pegawai.Pegawai', on_delete=models.DO_NOTHING, db_column='nik')

    class Meta:
        managed = False
        db_table = 'data_triase_igdsekunder'


class PenilaianAwalKeperawatanIgd(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    tanggal = models.DateTimeField(default=datetime.now, blank=True)
    informasi = models.CharField(max_length=13, choices=INFORMASI)
    keluhan_utama = models.TextField()
    rpd = models.TextField()
    rpo = models.TextField()
    status_kehamilan = models.CharField(max_length=11, default='Tidak Hamil', choices=STATUSHAMIL)
    gravida = models.CharField(max_length=20, blank=True, null=True)
    para = models.CharField(max_length=20, blank=True, null=True)
    abortus = models.CharField(max_length=20, blank=True, null=True)
    hpht = models.CharField(max_length=20, blank=True, null=True)
    tekanan = models.CharField(max_length=12, choices=TEKANAN)
    pupil = models.CharField(max_length=8, choices=PUPIL)
    neurosensorik = models.CharField(max_length=28, choices=NEUROSENSORIK)
    integumen = models.CharField(max_length=14, choices=INTEGUMEN)
    turgor = models.CharField(max_length=7, choices=TURGOR)
    edema = models.CharField(max_length=13, choices=EDEMA)
    mukosa = models.CharField(max_length=6, choices=MUKOSA)
    perdarahan = models.CharField(max_length=9, choices=PERDARAHAN)
    jumlah_perdarahan = models.CharField(max_length=5, blank=True, null=True)
    warna_perdarahan = models.CharField(max_length=40, blank=True, null=True)
    intoksikasi = models.CharField(max_length=16, choices=INTOKSIKASI)
    bab = models.CharField(max_length=2, blank=True, null=True)
    xbab = models.CharField(max_length=10, blank=True, null=True)
    kbab = models.CharField(max_length=40, blank=True, null=True)
    wbab = models.CharField(max_length=40, blank=True, null=True)
    bak = models.CharField(max_length=2, blank=True, null=True)
    xbak = models.CharField(max_length=10, blank=True, null=True)
    wbak = models.CharField(max_length=40, blank=True, null=True)
    lbak = models.CharField(max_length=40, blank=True, null=True)
    psikologis = models.CharField(max_length=17, choices=PSIKOLOGIS)
    jiwa = models.CharField(max_length=5, choices=BOOLEAN)
    perilaku = models.CharField(max_length=34, choices=PERILAKU)
    dilaporkan = models.CharField(max_length=50, blank=True, null=True, )
    sebutkan = models.CharField(max_length=50, blank=True, null=True)
    hubungan = models.CharField(max_length=15, choices=HUBUNGAN)
    tinggal_dengan = models.CharField(max_length=13, choices=TINGGAL_DENGAN)
    ket_tinggal = models.CharField(max_length=50, blank=True, null=True)
    budaya = models.CharField(max_length=9, choices=BUDAYA)
    ket_budaya = models.CharField(max_length=50)
    pendidikan_pj = models.CharField(max_length=14, choices=PENDIDIKAN_PJ)
    ket_pendidikan_pj = models.CharField(max_length=50, blank=True, null=True)
    edukasi = models.CharField(max_length=8, choices=EDUKASI)
    ket_edukasi = models.CharField(max_length=50)
    kemampuan = models.CharField(max_length=20, choices=KEMAMPUAN)
    aktifitas = models.CharField(max_length=12, choices=AKTIFITAS)
    alat_bantu = models.CharField(max_length=5, choices=BOOLEAN)
    ket_bantu = models.CharField(max_length=50, blank=True, null=True)
    nyeri = models.CharField(max_length=15, choices=NYERI)
    provokes = models.CharField(max_length=15, choices=PROVOKES)
    ket_provokes = models.CharField(max_length=40)
    quality = models.CharField(max_length=16, choices=QUALITY)
    ket_quality = models.CharField(max_length=50)
    lokasi = models.CharField(max_length=50)
    menyebar = models.CharField(max_length=5, choices=BOOLEAN)
    skala_nyeri = models.CharField(max_length=2, choices=SKALA_NYERI)
    durasi = models.CharField(max_length=25)
    nyeri_hilang = models.CharField(max_length=14, choices=NYERI_HILANG)
    ket_nyeri = models.CharField(max_length=40, blank=True, null=True)
    pada_dokter = models.CharField(max_length=5, choices=BOOLEAN)
    ket_dokter = models.CharField(max_length=15, blank=True, null=True)
    berjalan_a = models.CharField(max_length=5, choices=BOOLEAN)
    berjalan_b = models.CharField(max_length=5, choices=BOOLEAN)
    berjalan_c = models.CharField(max_length=5, choices=BOOLEAN)
    hasil = models.CharField(max_length=40, choices=HASIL)
    lapor = models.CharField(max_length=5, choices=BOOLEAN)
    ket_lapor = models.CharField(max_length=15, blank=True, null=True)
    rencana = models.TextField()
    nip = models.ForeignKey('pegawai.Petugas', models.DO_NOTHING, db_column='nip')

    class Meta:
        managed = False
        db_table = 'penilaian_awal_keperawatan_igd'


class PenilaianAwalKeperawatanIgdMasalah(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    kode_masalah = models.ForeignKey('diagnosa.MasterMasalahKeperawatan', models.DO_NOTHING, db_column='kode_masalah')

    class Meta:
        managed = False
        db_table = 'penilaian_awal_keperawatan_igd_masalah'
        unique_together = (('no_rawat', 'kode_masalah'),)

