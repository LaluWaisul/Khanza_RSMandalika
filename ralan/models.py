from django.db import models

# Create your models here.

class Jadwal(models.Model):
    kd_dokter = models.OneToOneField('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter', primary_key=True)
    hari_kerja = models.CharField(max_length=6)
    jam_mulai = models.TimeField()
    jam_selesai = models.TimeField(blank=True, null=True)
    kd_poli = models.ForeignKey('bangsal.Poliklinik', on_delete=models.DO_NOTHING, db_column='kd_poli', blank=True, null=True)
    kuota = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jadwal'
        unique_together = (('kd_dokter', 'hari_kerja', 'jam_mulai'),)
        
    def __str__(self):
        return f'{self.kd_dokter} - {self.kd_poli}'
    

class BookingPeriksa(models.Model):
    no_booking = models.CharField(primary_key=True, max_length=17)
    tanggal = models.DateField(blank=True, null=True)
    nama = models.CharField(max_length=40, blank=True, null=True)
    alamat = models.CharField(max_length=200, blank=True, null=True)
    no_telp = models.CharField(max_length=40, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    kd_poli = models.ForeignKey('bangsal.Poliklinik', on_delete=models.DO_NOTHING, db_column='kd_poli', blank=True, null=True)
    tambahan_pesan = models.CharField(max_length=400, blank=True, null=True)
    status = models.CharField(max_length=13)
    tanggal_booking = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'booking_periksa'
        unique_together = (('tanggal', 'no_telp'),)
        
    def __str__(self):
        return f'{self.tanggal}{self.no_telp} - {self.nama} - {self.no_booking}'


class BookingPeriksaBalasan(models.Model):
    no_booking = models.OneToOneField(BookingPeriksa, on_delete=models.DO_NOTHING, db_column='no_booking', primary_key=True)
    balasan = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booking_periksa_balasan'


class BookingPeriksaDiterima(models.Model):
    no_booking = models.OneToOneField(BookingPeriksa, on_delete=models.DO_NOTHING, db_column='no_booking', primary_key=True)
    no_rkm_medis = models.ForeignKey('pasien.Pasien', on_delete=models.DO_NOTHING, db_column='no_rkm_medis', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booking_periksa_diterima'


class BookingRegistrasi(models.Model):
    tanggal_booking = models.DateField(blank=True, null=True, auto_created=True)
    jam_booking = models.TimeField(blank=True, null=True, auto_created=True)
    no_rkm_medis = models.OneToOneField('pasien.Pasien', on_delete=models.DO_NOTHING, db_column='no_rkm_medis', primary_key=True)
    tanggal_periksa = models.DateField()
    kd_dokter = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter', to_field='kd_dokter', blank=True, null=True)
    kd_poli = models.ForeignKey('bangsal.Poliklinik', on_delete=models.DO_NOTHING, db_column='kd_poli', blank=True, null=True)
    no_reg = models.CharField(max_length=8, blank=True, null=True)
    kd_pj = models.ForeignKey('asuransi.Penjab', on_delete=models.DO_NOTHING, db_column='kd_pj', blank=True, null=True)
    limit_reg = models.IntegerField(blank=True, null=True)
    waktu_kunjungan = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=18, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booking_registrasi'
        unique_together = (('no_rkm_medis', 'tanggal_periksa'),)


class SkriningRawatJalan(models.Model):
    tanggal = models.DateField(primary_key=True)
    jam = models.TimeField()
    no_rkm_medis = models.ForeignKey('pasien.Pasien', on_delete=models.DO_NOTHING, db_column='no_rkm_medis')
    geriatri = models.CharField(max_length=5, blank=True, null=True)
    kesadaran = models.CharField(max_length=43, blank=True, null=True)
    pernapasan = models.CharField(max_length=14, blank=True, null=True)
    nyeri_dada = models.CharField(max_length=31, blank=True, null=True)
    skala_nyeri = models.CharField(max_length=20, blank=True, null=True)
    keputusan = models.CharField(max_length=14, blank=True, null=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'skrining_rawat_jalan'
        unique_together = (('tanggal', 'jam', 'no_rkm_medis'),)


class RegPeriksa(models.Model):
    no_reg = models.CharField(max_length=8, blank=True, null=True)
    no_rawat = models.CharField(primary_key=True, max_length=17)
    tgl_registrasi = models.DateField(blank=True, null=True)
    jam_reg = models.TimeField(blank=True, null=True)
    kd_dokter = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter', blank=True, null=True)
    no_rkm_medis = models.ForeignKey('pasien.Pasien', on_delete=models.DO_NOTHING, db_column='no_rkm_medis', blank=True, null=True)
    kd_poli = models.ForeignKey('bangsal.Poliklinik', on_delete=models.DO_NOTHING, db_column='kd_poli', blank=True, null=True)
    p_jawab = models.CharField(max_length=100, blank=True, null=True)
    almt_pj = models.CharField(max_length=200, blank=True, null=True)
    hubunganpj = models.CharField(max_length=20, blank=True, null=True)
    biaya_reg = models.FloatField(blank=True, null=True)
    stts = models.CharField(max_length=15, blank=True, null=True)
    stts_daftar = models.CharField(max_length=4)
    status_lanjut = models.CharField(max_length=5)
    kd_pj = models.ForeignKey('asuransi.Penjab', on_delete=models.DO_NOTHING, db_column='kd_pj')
    umurdaftar = models.IntegerField(blank=True, null=True)
    sttsumur = models.CharField(max_length=2, blank=True, null=True)
    status_bayar = models.CharField(max_length=11)
    status_poli = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'reg_periksa'
        ordering = ['-tgl_registrasi']
    
    @property
    def slugify_norawat(self):
        # return slugify(unidecode(self.no_rawat))
        return self.no_rawat.replace('/','-')

    def __str__(self):
        return self.no_rawat

class Rawatjalan(models.Model):
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
        db_table = 'rawatjalan'
        unique_together = (('tgl', 'id', 'tnd'),)


class PermintaanRegistrasi(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    biaya = models.FloatField()

    class Meta:
        managed = False
        db_table = 'permintaan_registrasi'



class ProsedurPasien(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    kode = models.ForeignKey('tindakan.Icd9', on_delete=models.DO_NOTHING, db_column='kode')
    status = models.CharField(max_length=5)
    prioritas = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prosedur_pasien'
        unique_together = (('no_rawat', 'kode', 'status'),)


class PenilaianAwalKeperawatanRalan(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    tanggal = models.DateTimeField()
    informasi = models.CharField(max_length=13)
    td = models.CharField(max_length=8)
    nadi = models.CharField(max_length=5)
    rr = models.CharField(max_length=5)
    suhu = models.CharField(max_length=5)
    gcs = models.CharField(max_length=5)
    bb = models.CharField(max_length=5)
    tb = models.CharField(max_length=5)
    bmi = models.CharField(max_length=10)
    keluhan_utama = models.CharField(max_length=150)
    rpd = models.CharField(max_length=100)
    rpk = models.CharField(max_length=100)
    rpo = models.CharField(max_length=100)
    alergi = models.CharField(max_length=25)
    alat_bantu = models.CharField(max_length=5)
    ket_bantu = models.CharField(max_length=50)
    prothesa = models.CharField(max_length=5)
    ket_pro = models.CharField(max_length=50)
    adl = models.CharField(max_length=7)
    status_psiko = models.CharField(max_length=9)
    ket_psiko = models.CharField(max_length=70)
    hub_keluarga = models.CharField(max_length=10)
    tinggal_dengan = models.CharField(max_length=13)
    ket_tinggal = models.CharField(max_length=40)
    ekonomi = models.CharField(max_length=6)
    budaya = models.CharField(max_length=9)
    ket_budaya = models.CharField(max_length=50)
    edukasi = models.CharField(max_length=8)
    ket_edukasi = models.CharField(max_length=50)
    berjalan_a = models.CharField(max_length=5)
    berjalan_b = models.CharField(max_length=5)
    berjalan_c = models.CharField(max_length=5)
    hasil = models.CharField(max_length=40)
    lapor = models.CharField(max_length=5)
    ket_lapor = models.CharField(max_length=15)
    sg1 = models.CharField(max_length=12)
    nilai1 = models.CharField(max_length=1)
    sg2 = models.CharField(max_length=5)
    nilai2 = models.CharField(max_length=1)
    total_hasil = models.IntegerField()
    nyeri = models.CharField(max_length=15)
    provokes = models.CharField(max_length=15)
    ket_provokes = models.CharField(max_length=40)
    quality = models.CharField(max_length=16)
    ket_quality = models.CharField(max_length=50)
    lokasi = models.CharField(max_length=50)
    menyebar = models.CharField(max_length=5)
    skala_nyeri = models.CharField(max_length=2)
    durasi = models.CharField(max_length=25)
    nyeri_hilang = models.CharField(max_length=14)
    ket_nyeri = models.CharField(max_length=40)
    pada_dokter = models.CharField(max_length=5)
    ket_dokter = models.CharField(max_length=15)
    rencana = models.CharField(max_length=200)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip')

    class Meta:
        managed = False
        db_table = 'penilaian_awal_keperawatan_ralan'


class PenilaianAwalKeperawatanGigi(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    tanggal = models.DateTimeField()
    informasi = models.CharField(max_length=13)
    td = models.CharField(max_length=8)
    nadi = models.CharField(max_length=5)
    rr = models.CharField(max_length=5)
    suhu = models.CharField(max_length=5)
    bb = models.CharField(max_length=5)
    tb = models.CharField(max_length=5)
    bmi = models.CharField(max_length=10)
    keluhan_utama = models.CharField(max_length=150)
    riwayat_penyakit = models.CharField(max_length=16, blank=True, null=True)
    ket_riwayat_penyakit = models.CharField(max_length=30)
    alergi = models.CharField(max_length=25)
    riwayat_perawatan_gigi = models.CharField(max_length=9)
    ket_riwayat_perawatan_gigi = models.CharField(max_length=50)
    kebiasaan_sikat_gigi = models.CharField(max_length=13)
    kebiasaan_lain = models.CharField(max_length=23, blank=True, null=True)
    ket_kebiasaan_lain = models.CharField(max_length=30)
    obat_yang_diminum_saatini = models.CharField(max_length=100, blank=True, null=True)
    alat_bantu = models.CharField(max_length=5)
    ket_alat_bantu = models.CharField(max_length=30)
    prothesa = models.CharField(max_length=5)
    ket_pro = models.CharField(max_length=50)
    status_psiko = models.CharField(max_length=9)
    ket_psiko = models.CharField(max_length=70)
    hub_keluarga = models.CharField(max_length=10)
    tinggal_dengan = models.CharField(max_length=13)
    ket_tinggal = models.CharField(max_length=40)
    ekonomi = models.CharField(max_length=6)
    budaya = models.CharField(max_length=9)
    ket_budaya = models.CharField(max_length=50)
    edukasi = models.CharField(max_length=8)
    ket_edukasi = models.CharField(max_length=50)
    berjalan_a = models.CharField(max_length=5)
    berjalan_b = models.CharField(max_length=5)
    berjalan_c = models.CharField(max_length=5)
    hasil = models.CharField(max_length=40)
    lapor = models.CharField(max_length=5)
    ket_lapor = models.CharField(max_length=15)
    nyeri = models.CharField(max_length=15)
    lokasi = models.CharField(max_length=50)
    skala_nyeri = models.CharField(max_length=2)
    durasi = models.CharField(max_length=25)
    frekuensi = models.CharField(max_length=25)
    nyeri_hilang = models.CharField(max_length=15)
    ket_nyeri = models.CharField(max_length=40)
    pada_dokter = models.CharField(max_length=5)
    ket_dokter = models.CharField(max_length=15)
    kebersihan_mulut = models.CharField(max_length=6)
    mukosa_mulut = models.CharField(max_length=10)
    karies = models.CharField(max_length=5)
    karang_gigi = models.CharField(max_length=5)
    gingiva = models.CharField(max_length=6)
    palatum = models.CharField(max_length=6)
    rencana = models.CharField(max_length=200)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip')

    class Meta:
        managed = False
        db_table = 'penilaian_awal_keperawatan_gigi'


class PenilaianAwalKeperawatanGigiMasalah(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    kode_masalah = models.ForeignKey('diagnosa.MasterMasalahKeperawatanGigi', on_delete=models.DO_NOTHING, db_column='kode_masalah')

    class Meta:
        managed = False
        db_table = 'penilaian_awal_keperawatan_gigi_masalah'
        unique_together = (('no_rawat', 'kode_masalah'),)


class PenilaianAwalKeperawatanMata(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    tanggal = models.DateTimeField()
    informasi = models.CharField(max_length=13)
    td = models.CharField(max_length=8)
    nadi = models.CharField(max_length=5)
    rr = models.CharField(max_length=5)
    suhu = models.CharField(max_length=5)
    gcs = models.CharField(max_length=5)
    bb = models.CharField(max_length=5)
    tb = models.CharField(max_length=5)
    bmi = models.CharField(max_length=10)
    keluhan_utama = models.CharField(max_length=150)
    rpd = models.CharField(max_length=100)
    rps = models.CharField(max_length=100)
    rpk = models.CharField(max_length=100)
    rpo = models.CharField(max_length=100)
    alergi = models.CharField(max_length=25)
    alat_bantu = models.CharField(max_length=5)
    ket_bantu = models.CharField(max_length=50)
    prothesa = models.CharField(max_length=5)
    ket_pro = models.CharField(max_length=50)
    adl = models.CharField(max_length=7)
    status_psiko = models.CharField(max_length=9)
    ket_psiko = models.CharField(max_length=70)
    hub_keluarga = models.CharField(max_length=10)
    tinggal_dengan = models.CharField(max_length=13)
    ket_tinggal = models.CharField(max_length=40)
    ekonomi = models.CharField(max_length=6)
    budaya = models.CharField(max_length=9)
    ket_budaya = models.CharField(max_length=50)
    edukasi = models.CharField(max_length=8)
    ket_edukasi = models.CharField(max_length=50)
    berjalan_a = models.CharField(max_length=5)
    berjalan_b = models.CharField(max_length=5)
    berjalan_c = models.CharField(max_length=5)
    hasil = models.CharField(max_length=40)
    lapor = models.CharField(max_length=5)
    ket_lapor = models.CharField(max_length=15)
    sg1 = models.CharField(max_length=12)
    nilai1 = models.CharField(max_length=1)
    sg2 = models.CharField(max_length=5)
    nilai2 = models.CharField(max_length=1)
    sg3 = models.CharField(max_length=5)
    nilai3 = models.CharField(max_length=1)
    sg4 = models.CharField(max_length=5)
    nilai4 = models.CharField(max_length=1)
    total_hasil = models.IntegerField()
    nyeri = models.CharField(max_length=15)
    provokes = models.CharField(max_length=15)
    ket_provokes = models.CharField(max_length=40)
    quality = models.CharField(max_length=16)
    ket_quality = models.CharField(max_length=50)
    lokasi = models.CharField(max_length=50)
    menyebar = models.CharField(max_length=5)
    skala_nyeri = models.CharField(max_length=2)
    durasi = models.CharField(max_length=25)
    nyeri_hilang = models.CharField(max_length=14)
    ket_nyeri = models.CharField(max_length=40)
    pada_dokter = models.CharField(max_length=5)
    ket_dokter = models.CharField(max_length=15)
    visuskanan = models.CharField(max_length=20)
    visuskiri = models.CharField(max_length=20)
    refraksikanan = models.CharField(max_length=20)
    refraksikiri = models.CharField(max_length=20)
    tiokanan = models.CharField(max_length=20)
    tiokiri = models.CharField(max_length=20)
    palberakanan = models.CharField(max_length=20)
    palberakiri = models.CharField(max_length=20)
    konjungtivakanan = models.CharField(max_length=20)
    konjungtivakiri = models.CharField(max_length=20)
    sklerakanan = models.CharField(max_length=20)
    sklerakiri = models.CharField(max_length=20)
    korneakanan = models.CharField(max_length=20)
    korneakiri = models.CharField(max_length=20)
    bmdkanan = models.CharField(max_length=20)
    bmdkiri = models.CharField(max_length=20)
    iriskanan = models.CharField(max_length=20)
    iriskiri = models.CharField(max_length=20)
    pupilkanan = models.CharField(max_length=20)
    pupilkiri = models.CharField(max_length=20)
    lensakanan = models.CharField(max_length=20)
    lensakiri = models.CharField(max_length=20)
    oftalmoskopikanan = models.CharField(max_length=100)
    oftalmoskopikiri = models.CharField(max_length=100)
    rencana = models.CharField(max_length=100)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip')

    class Meta:
        managed = False
        db_table = 'penilaian_awal_keperawatan_mata'



class PenilaianFisioterapi(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    tanggal = models.DateTimeField()
    informasi = models.CharField(max_length=13)
    keluhan_utama = models.CharField(max_length=150)
    rps = models.CharField(max_length=100)
    rpd = models.CharField(max_length=100)
    td = models.CharField(max_length=8)
    hr = models.CharField(max_length=5)
    rr = models.CharField(max_length=5)
    suhu = models.CharField(max_length=5)
    nyeri_tekan = models.CharField(max_length=5)
    nyeri_gerak = models.CharField(max_length=5)
    nyeri_diam = models.CharField(max_length=5)
    palpasi = models.CharField(max_length=50)
    luas_gerak_sendi = models.CharField(max_length=50)
    kekuatan_otot = models.CharField(max_length=50)
    statis = models.CharField(max_length=50)
    dinamis = models.CharField(max_length=50)
    kognitif = models.CharField(max_length=50)
    auskultasi = models.CharField(max_length=50)
    alat_bantu = models.CharField(max_length=5)
    ket_bantu = models.CharField(max_length=50)
    prothesa = models.CharField(max_length=5)
    ket_pro = models.CharField(max_length=50)
    deformitas = models.CharField(max_length=5)
    ket_deformitas = models.CharField(max_length=50)
    resikojatuh = models.CharField(max_length=5)
    ket_resikojatuh = models.CharField(max_length=50)
    adl = models.CharField(max_length=7)
    lainlain_fungsional = models.CharField(max_length=70)
    ket_fisik = models.TextField()
    pemeriksaan_musculoskeletal = models.CharField(max_length=200)
    pemeriksaan_neuromuscular = models.CharField(max_length=200)
    pemeriksaan_cardiopulmonal = models.CharField(max_length=200)
    pemeriksaan_integument = models.CharField(max_length=200)
    pengukuran_musculoskeletal = models.CharField(max_length=200)
    pengukuran_neuromuscular = models.CharField(max_length=200)
    pengukuran_cardiopulmonal = models.CharField(max_length=200)
    pengukuran_integument = models.CharField(max_length=200)
    penunjang = models.CharField(max_length=500)
    diagnosis_fisio = models.CharField(max_length=100)
    rencana_terapi = models.CharField(max_length=200)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip')

    class Meta:
        managed = False
        db_table = 'penilaian_fisioterapi'


class PenilaianAwalKeperawatanKebidanan(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    tanggal = models.DateTimeField()
    informasi = models.CharField(max_length=13)
    td = models.CharField(max_length=8)
    nadi = models.CharField(max_length=5)
    rr = models.CharField(max_length=5)
    suhu = models.CharField(max_length=5)
    gcs = models.CharField(max_length=10)
    bb = models.CharField(max_length=5)
    tb = models.CharField(max_length=5)
    lila = models.CharField(max_length=5)
    bmi = models.CharField(max_length=10)
    tfu = models.CharField(max_length=10)
    tbj = models.CharField(max_length=10)
    letak = models.CharField(max_length=10)
    presentasi = models.CharField(max_length=10)
    penurunan = models.CharField(max_length=10)
    his = models.CharField(max_length=10)
    kekuatan = models.CharField(max_length=10)
    lamanya = models.CharField(max_length=10)
    bjj = models.CharField(max_length=10)
    ket_bjj = models.CharField(max_length=13)
    portio = models.CharField(max_length=10)
    serviks = models.CharField(max_length=10)
    ketuban = models.CharField(max_length=10)
    hodge = models.CharField(max_length=10)
    inspekulo = models.CharField(max_length=9)
    ket_inspekulo = models.CharField(max_length=50)
    ctg = models.CharField(max_length=9)
    ket_ctg = models.CharField(max_length=50)
    usg = models.CharField(max_length=9)
    ket_usg = models.CharField(max_length=50)
    lab = models.CharField(max_length=9)
    ket_lab = models.CharField(max_length=50)
    lakmus = models.CharField(max_length=9)
    ket_lakmus = models.CharField(max_length=50)
    panggul = models.CharField(max_length=27)
    keluhan_utama = models.CharField(max_length=1000)
    umur = models.CharField(max_length=10)
    lama = models.CharField(max_length=10)
    banyaknya = models.CharField(max_length=10)
    haid = models.CharField(max_length=20)
    siklus = models.CharField(max_length=10)
    ket_siklus = models.CharField(max_length=13)
    ket_siklus1 = models.CharField(max_length=17)
    status = models.CharField(max_length=21)
    kali = models.CharField(max_length=5)
    usia1 = models.CharField(max_length=5)
    ket1 = models.CharField(max_length=13)
    usia2 = models.CharField(max_length=5, blank=True, null=True)
    ket2 = models.CharField(max_length=13, blank=True, null=True)
    usia3 = models.CharField(max_length=5, blank=True, null=True)
    ket3 = models.CharField(max_length=13, blank=True, null=True)
    hpht = models.DateField(blank=True, null=True)
    usia_kehamilan = models.CharField(max_length=10)
    tp = models.DateField(blank=True, null=True)
    imunisasi = models.CharField(max_length=5)
    ket_imunisasi = models.CharField(max_length=10)
    g = models.CharField(max_length=10)
    p = models.CharField(max_length=10)
    a = models.CharField(max_length=10)
    hidup = models.CharField(max_length=10)
    ginekologi = models.CharField(max_length=17)
    kebiasaan = models.CharField(max_length=11)
    ket_kebiasaan = models.CharField(max_length=50)
    kebiasaan1 = models.CharField(max_length=5)
    ket_kebiasaan1 = models.CharField(max_length=5)
    kebiasaan2 = models.CharField(max_length=5)
    ket_kebiasaan2 = models.CharField(max_length=5)
    kebiasaan3 = models.CharField(max_length=5)
    kb = models.CharField(max_length=12)
    ket_kb = models.CharField(max_length=10)
    komplikasi = models.CharField(max_length=9)
    ket_komplikasi = models.CharField(max_length=50)
    berhenti = models.CharField(max_length=20)
    alasan = models.CharField(max_length=50)
    alat_bantu = models.CharField(max_length=5)
    ket_bantu = models.CharField(max_length=50)
    prothesa = models.CharField(max_length=5)
    ket_pro = models.CharField(max_length=50)
    adl = models.CharField(max_length=7)
    status_psiko = models.CharField(max_length=9)
    ket_psiko = models.CharField(max_length=50)
    hub_keluarga = models.CharField(max_length=10)
    tinggal_dengan = models.CharField(max_length=13)
    ket_tinggal = models.CharField(max_length=50)
    ekonomi = models.CharField(max_length=6)
    budaya = models.CharField(max_length=9)
    ket_budaya = models.CharField(max_length=50)
    edukasi = models.CharField(max_length=8)
    ket_edukasi = models.CharField(max_length=50)
    berjalan_a = models.CharField(max_length=5)
    berjalan_b = models.CharField(max_length=5)
    berjalan_c = models.CharField(max_length=5)
    hasil = models.CharField(max_length=40)
    lapor = models.CharField(max_length=5)
    ket_lapor = models.CharField(max_length=10)
    sg1 = models.CharField(max_length=11)
    nilai1 = models.CharField(max_length=1)
    sg2 = models.CharField(max_length=5)
    nilai2 = models.CharField(max_length=1)
    total_hasil = models.CharField(max_length=5)
    nyeri = models.CharField(max_length=15)
    provokes = models.CharField(max_length=15)
    ket_provokes = models.CharField(max_length=40)
    quality = models.CharField(max_length=16)
    ket_quality = models.CharField(max_length=40)
    lokasi = models.CharField(max_length=40)
    menyebar = models.CharField(max_length=5)
    skala_nyeri = models.CharField(max_length=2)
    durasi = models.CharField(max_length=5)
    nyeri_hilang = models.CharField(max_length=15)
    ket_nyeri = models.CharField(max_length=40)
    pada_dokter = models.CharField(max_length=5)
    ket_dokter = models.CharField(max_length=10)
    masalah = models.CharField(max_length=1000)
    tindakan = models.CharField(max_length=1000)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip')

    class Meta:
        managed = False
        db_table = 'penilaian_awal_keperawatan_kebidanan'


class PenilaianAwalKeperawatanRalanBayi(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    tanggal = models.DateTimeField()
    informasi = models.CharField(max_length=13)
    td = models.CharField(max_length=8)
    nadi = models.CharField(max_length=5)
    rr = models.CharField(max_length=5)
    suhu = models.CharField(max_length=5)
    gcs = models.CharField(max_length=5)
    bb = models.CharField(max_length=5)
    tb = models.CharField(max_length=5)
    lp = models.CharField(max_length=5)
    lk = models.CharField(max_length=5)
    ld = models.CharField(max_length=5)
    keluhan_utama = models.CharField(max_length=150)
    rpd = models.CharField(max_length=100)
    rpk = models.CharField(max_length=100)
    rpo = models.CharField(max_length=100)
    alergi = models.CharField(max_length=25)
    anakke = models.CharField(max_length=4)
    darisaudara = models.CharField(max_length=4)
    caralahir = models.CharField(max_length=15)
    ket_caralahir = models.CharField(max_length=30)
    umurkelahiran = models.CharField(max_length=12)
    kelainanbawaan = models.CharField(max_length=9)
    ket_kelainan_bawaan = models.CharField(max_length=30)
    usiatengkurap = models.CharField(max_length=15)
    usiaduduk = models.CharField(max_length=15)
    usiaberdiri = models.CharField(max_length=15)
    usiagigipertama = models.CharField(max_length=15)
    usiaberjalan = models.CharField(max_length=15)
    usiabicara = models.CharField(max_length=15)
    usiamembaca = models.CharField(max_length=15)
    usiamenulis = models.CharField(max_length=15)
    gangguanemosi = models.CharField(max_length=50)
    alat_bantu = models.CharField(max_length=5)
    ket_bantu = models.CharField(max_length=50)
    prothesa = models.CharField(max_length=5)
    ket_pro = models.CharField(max_length=50)
    adl = models.CharField(max_length=7)
    status_psiko = models.CharField(max_length=13)
    ket_psiko = models.CharField(max_length=70)
    hub_keluarga = models.CharField(max_length=10)
    pengasuh = models.CharField(max_length=16)
    ket_pengasuh = models.CharField(max_length=40)
    ekonomi = models.CharField(max_length=6)
    budaya = models.CharField(max_length=9)
    ket_budaya = models.CharField(max_length=50)
    edukasi = models.CharField(max_length=9)
    ket_edukasi = models.CharField(max_length=50)
    berjalan_a = models.CharField(max_length=5)
    berjalan_b = models.CharField(max_length=5)
    berjalan_c = models.CharField(max_length=5)
    hasil = models.CharField(max_length=40)
    lapor = models.CharField(max_length=5)
    ket_lapor = models.CharField(max_length=15)
    sg1 = models.CharField(max_length=5)
    nilai1 = models.CharField(max_length=1)
    sg2 = models.CharField(max_length=5)
    nilai2 = models.CharField(max_length=1)
    sg3 = models.CharField(max_length=5)
    nilai3 = models.CharField(max_length=1)
    sg4 = models.CharField(max_length=5)
    nilai4 = models.CharField(max_length=1)
    total_hasil = models.IntegerField()
    wajah = models.CharField(max_length=47)
    nilaiwajah = models.CharField(max_length=1)
    kaki = models.CharField(max_length=29)
    nilaikaki = models.CharField(max_length=1)
    aktifitas = models.CharField(max_length=38)
    nilaiaktifitas = models.CharField(max_length=1)
    menangis = models.CharField(max_length=41)
    nilaimenangis = models.CharField(max_length=1)
    bersuara = models.CharField(max_length=44)
    nilaibersuara = models.CharField(max_length=1)
    hasilnyeri = models.IntegerField()
    nyeri = models.CharField(max_length=15)
    lokasi = models.CharField(max_length=50)
    durasi = models.CharField(max_length=25)
    frekuensi = models.CharField(max_length=25)
    nyeri_hilang = models.CharField(max_length=20)
    ket_nyeri = models.CharField(max_length=40)
    pada_dokter = models.CharField(max_length=5)
    ket_dokter = models.CharField(max_length=15)
    rencana = models.CharField(max_length=200)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip')

    class Meta:
        managed = False
        db_table = 'penilaian_awal_keperawatan_ralan_bayi'


class PenilaianAwalKeperawatanRalanBayiMasalah(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    kode_masalah = models.ForeignKey('diagnosa.MasterMasalahKeperawatanAnak', on_delete=models.DO_NOTHING, db_column='kode_masalah')

    class Meta:
        managed = False
        db_table = 'penilaian_awal_keperawatan_ralan_bayi_masalah'
        unique_together = (('no_rawat', 'kode_masalah'),)


class PenilaianAwalKeperawatanRalanMasalah(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    kode_masalah = models.ForeignKey('diagnosa.MasterMasalahKeperawatan', on_delete=models.DO_NOTHING, db_column='kode_masalah')

    class Meta:
        managed = False
        db_table = 'penilaian_awal_keperawatan_ralan_masalah'
        unique_together = (('no_rawat', 'kode_masalah'),)


class PenilaianMedisRalan(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    tanggal = models.DateTimeField()
    kd_dokter = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter')
    anamnesis = models.CharField(max_length=13)
    hubungan = models.CharField(max_length=30)
    keluhan_utama = models.CharField(max_length=2000)
    rps = models.CharField(max_length=2000)
    rpd = models.CharField(max_length=1000)
    rpk = models.CharField(max_length=1000)
    rpo = models.CharField(max_length=1000)
    alergi = models.CharField(max_length=50)
    keadaan = models.CharField(max_length=12)
    gcs = models.CharField(max_length=10)
    kesadaran = models.CharField(max_length=13)
    td = models.CharField(max_length=8)
    nadi = models.CharField(max_length=5)
    rr = models.CharField(max_length=5)
    suhu = models.CharField(max_length=5)
    spo = models.CharField(max_length=5)
    bb = models.CharField(max_length=5)
    tb = models.CharField(max_length=5)
    kepala = models.CharField(max_length=15)
    gigi = models.CharField(max_length=15)
    tht = models.CharField(max_length=15)
    thoraks = models.CharField(max_length=15)
    abdomen = models.CharField(max_length=15)
    genital = models.CharField(max_length=15)
    ekstremitas = models.CharField(max_length=15)
    kulit = models.CharField(max_length=15)
    ket_fisik = models.TextField()
    ket_lokalis = models.TextField()
    penunjang = models.TextField()
    diagnosis = models.CharField(max_length=500)
    tata = models.TextField()
    konsulrujuk = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'penilaian_medis_ralan'


class PenilaianMedisRalanAnak(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    tanggal = models.DateTimeField()
    kd_dokter = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter')
    anamnesis = models.CharField(max_length=13)
    hubungan = models.CharField(max_length=100)
    keluhan_utama = models.CharField(max_length=2000)
    rps = models.CharField(max_length=2000)
    rpd = models.CharField(max_length=1000)
    rpk = models.CharField(max_length=1000)
    rpo = models.CharField(max_length=1000)
    alergi = models.CharField(max_length=100)
    keadaan = models.CharField(max_length=12)
    gcs = models.CharField(max_length=10)
    kesadaran = models.CharField(max_length=13)
    td = models.CharField(max_length=8)
    nadi = models.CharField(max_length=5)
    rr = models.CharField(max_length=5)
    suhu = models.CharField(max_length=5)
    spo = models.CharField(max_length=5)
    bb = models.CharField(max_length=5)
    tb = models.CharField(max_length=5)
    kepala = models.CharField(max_length=15)
    mata = models.CharField(max_length=15)
    gigi = models.CharField(max_length=15)
    tht = models.CharField(max_length=15)
    thoraks = models.CharField(max_length=15)
    abdomen = models.CharField(max_length=15)
    genital = models.CharField(max_length=15)
    ekstremitas = models.CharField(max_length=15)
    kulit = models.CharField(max_length=15)
    ket_fisik = models.TextField()
    ket_lokalis = models.TextField()
    penunjang = models.TextField()
    diagnosis = models.CharField(max_length=500)
    tata = models.TextField()
    konsul = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'penilaian_medis_ralan_anak'


class PenilaianMedisRalanKandungan(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    tanggal = models.DateTimeField()
    kd_dokter = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter')
    anamnesis = models.CharField(max_length=13)
    hubungan = models.CharField(max_length=100)
    keluhan_utama = models.CharField(max_length=2000)
    rps = models.CharField(max_length=2000)
    rpd = models.CharField(max_length=1000)
    rpk = models.CharField(max_length=1000)
    rpo = models.CharField(max_length=1000)
    alergi = models.CharField(max_length=100)
    keadaan = models.CharField(max_length=12)
    gcs = models.CharField(max_length=10)
    kesadaran = models.CharField(max_length=13)
    td = models.CharField(max_length=8)
    nadi = models.CharField(max_length=5)
    rr = models.CharField(max_length=5)
    suhu = models.CharField(max_length=5)
    spo = models.CharField(max_length=5)
    bb = models.CharField(max_length=5)
    tb = models.CharField(max_length=5)
    kepala = models.CharField(max_length=15)
    mata = models.CharField(max_length=15)
    gigi = models.CharField(max_length=15)
    tht = models.CharField(max_length=15)
    thoraks = models.CharField(max_length=15)
    abdomen = models.CharField(max_length=15)
    genital = models.CharField(max_length=15)
    ekstremitas = models.CharField(max_length=15)
    kulit = models.CharField(max_length=15)
    ket_fisik = models.TextField()
    tfu = models.CharField(max_length=10)
    tbj = models.CharField(max_length=10)
    his = models.CharField(max_length=10)
    kontraksi = models.CharField(max_length=5)
    djj = models.CharField(max_length=10)
    inspeksi = models.TextField()
    inspekulo = models.TextField()
    vt = models.TextField()
    rt = models.TextField()
    ultra = models.TextField()
    kardio = models.TextField()
    lab = models.TextField()
    diagnosis = models.CharField(max_length=500)
    tata = models.TextField()
    konsul = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'penilaian_medis_ralan_kandungan'


class PemeriksaanRalan(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    tgl_perawatan = models.DateField()
    jam_rawat = models.TimeField()
    suhu_tubuh = models.CharField(max_length=5, blank=True, null=True)
    tensi = models.CharField(max_length=8)
    nadi = models.CharField(max_length=3, blank=True, null=True)
    respirasi = models.CharField(max_length=3, blank=True, null=True)
    tinggi = models.CharField(max_length=5, blank=True, null=True)
    berat = models.CharField(max_length=5, blank=True, null=True)
    gcs = models.CharField(max_length=10, blank=True, null=True)
    kesadaran = models.CharField(max_length=13)
    keluhan = models.CharField(max_length=400, blank=True, null=True)
    pemeriksaan = models.CharField(max_length=400, blank=True, null=True)
    alergi = models.CharField(max_length=50, blank=True, null=True)
    imun_ke = models.CharField(max_length=2, blank=True, null=True)
    rtl = models.CharField(max_length=400)
    penilaian = models.CharField(max_length=400)
    instruksi = models.CharField(max_length=400)
    nip = models.ForeignKey('pegawai.Pegawai', on_delete=models.DO_NOTHING, db_column='nip')

    class Meta:
        managed = False
        db_table = 'pemeriksaan_ralan'
        unique_together = (('no_rawat', 'tgl_perawatan', 'jam_rawat'),)


class PemeriksaanGinekologiRalan(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    tgl_perawatan = models.DateField()
    jam_rawat = models.TimeField()
    inspeksi = models.CharField(max_length=50, blank=True, null=True)
    inspeksi_vulva = models.CharField(max_length=50, blank=True, null=True)
    inspekulo_gine = models.CharField(max_length=50, blank=True, null=True)
    fluxus_gine = models.CharField(max_length=1, blank=True, null=True)
    fluor_gine = models.CharField(max_length=1, blank=True, null=True)
    vulva_inspekulo = models.CharField(max_length=50)
    portio_inspekulo = models.CharField(max_length=50, blank=True, null=True)
    sondage = models.CharField(max_length=50, blank=True, null=True)
    portio_dalam = models.CharField(max_length=50, blank=True, null=True)
    bentuk = models.CharField(max_length=50, blank=True, null=True)
    cavum_uteri = models.CharField(max_length=50, blank=True, null=True)
    mobilitas = models.CharField(max_length=1, blank=True, null=True)
    ukuran = models.CharField(max_length=50, blank=True, null=True)
    nyeri_tekan = models.CharField(max_length=1, blank=True, null=True)
    adnexa_kanan = models.CharField(max_length=50, blank=True, null=True)
    adnexa_kiri = models.CharField(max_length=50)
    cavum_douglas = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'pemeriksaan_ginekologi_ralan'
        unique_together = (('no_rawat', 'tgl_perawatan', 'jam_rawat'),)


class PemeriksaanObstetriRalan(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    tgl_perawatan = models.DateField()
    jam_rawat = models.TimeField()
    tinggi_uteri = models.CharField(max_length=5, blank=True, null=True)
    janin = models.CharField(max_length=7, blank=True, null=True)
    letak = models.CharField(max_length=50, blank=True, null=True)
    panggul = models.CharField(max_length=3, blank=True, null=True)
    denyut = models.CharField(max_length=5, blank=True, null=True)
    kontraksi = models.CharField(max_length=1, blank=True, null=True)
    kualitas_mnt = models.CharField(max_length=5, blank=True, null=True)
    kualitas_dtk = models.CharField(max_length=5, blank=True, null=True)
    fluksus = models.CharField(max_length=1, blank=True, null=True)
    albus = models.CharField(max_length=1, blank=True, null=True)
    vulva = models.CharField(max_length=50, blank=True, null=True)
    portio = models.CharField(max_length=50, blank=True, null=True)
    dalam = models.CharField(max_length=6, blank=True, null=True)
    tebal = models.CharField(max_length=5, blank=True, null=True)
    arah = models.CharField(max_length=8, blank=True, null=True)
    pembukaan = models.CharField(max_length=50, blank=True, null=True)
    penurunan = models.CharField(max_length=50, blank=True, null=True)
    denominator = models.CharField(max_length=50)
    ketuban = models.CharField(max_length=1, blank=True, null=True)
    feto = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pemeriksaan_obstetri_ralan'
        unique_together = (('no_rawat', 'tgl_perawatan', 'jam_rawat'),)


class PcareKunjunganUmum(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    nokunjungan = models.CharField(db_column='noKunjungan', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tgldaftar = models.DateField(db_column='tglDaftar', blank=True, null=True)  # Field name made lowercase.
    no_rkm_medis = models.CharField(max_length=15, blank=True, null=True)
    nm_pasien = models.CharField(max_length=40, blank=True, null=True)
    nokartu = models.CharField(db_column='noKartu', max_length=25, blank=True, null=True)  # Field name made lowercase.
    kdpoli = models.CharField(db_column='kdPoli', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nmpoli = models.CharField(db_column='nmPoli', max_length=50, blank=True, null=True)  # Field name made lowercase.
    keluhan = models.CharField(max_length=400, blank=True, null=True)
    kdsadar = models.CharField(db_column='kdSadar', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nmsadar = models.CharField(db_column='nmSadar', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sistole = models.CharField(max_length=3, blank=True, null=True)
    diastole = models.CharField(max_length=3, blank=True, null=True)
    beratbadan = models.CharField(db_column='beratBadan', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tinggibadan = models.CharField(db_column='tinggiBadan', max_length=5, blank=True, null=True)  # Field name made lowercase.
    resprate = models.CharField(db_column='respRate', max_length=3, blank=True, null=True)  # Field name made lowercase.
    heartrate = models.CharField(db_column='heartRate', max_length=3, blank=True, null=True)  # Field name made lowercase.
    terapi = models.CharField(max_length=400, blank=True, null=True)
    kdstatuspulang = models.CharField(db_column='kdStatusPulang', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nmstatuspulang = models.CharField(db_column='nmStatusPulang', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tglpulang = models.DateField(db_column='tglPulang', blank=True, null=True)  # Field name made lowercase.
    kddokter = models.CharField(db_column='kdDokter', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nmdokter = models.CharField(db_column='nmDokter', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kddiag1 = models.CharField(db_column='kdDiag1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nmdiag1 = models.CharField(db_column='nmDiag1', max_length=400, blank=True, null=True)  # Field name made lowercase.
    kddiag2 = models.CharField(db_column='kdDiag2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nmdiag2 = models.CharField(db_column='nmDiag2', max_length=400, blank=True, null=True)  # Field name made lowercase.
    kddiag3 = models.CharField(db_column='kdDiag3', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nmdiag3 = models.CharField(db_column='nmDiag3', max_length=400, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'pcare_kunjungan_umum'


class PcarePendaftaran(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    tgldaftar = models.DateField(db_column='tglDaftar')  # Field name made lowercase.
    no_rkm_medis = models.CharField(max_length=15)
    nm_pasien = models.CharField(max_length=40)
    kdproviderpeserta = models.CharField(db_column='kdProviderPeserta', max_length=15)  # Field name made lowercase.
    nokartu = models.CharField(db_column='noKartu', max_length=25)  # Field name made lowercase.
    kdpoli = models.CharField(db_column='kdPoli', max_length=5)  # Field name made lowercase.
    nmpoli = models.CharField(db_column='nmPoli', max_length=50)  # Field name made lowercase.
    keluhan = models.CharField(max_length=400)
    kunjsakit = models.CharField(db_column='kunjSakit', max_length=15)  # Field name made lowercase.
    sistole = models.CharField(max_length=3)
    diastole = models.CharField(max_length=3)
    beratbadan = models.CharField(db_column='beratBadan', max_length=5)  # Field name made lowercase.
    tinggibadan = models.CharField(db_column='tinggiBadan', max_length=5)  # Field name made lowercase.
    resprate = models.CharField(db_column='respRate', max_length=3)  # Field name made lowercase.
    heartrate = models.CharField(db_column='heartRate', max_length=3)  # Field name made lowercase.
    rujukbalik = models.CharField(db_column='rujukBalik', max_length=3)  # Field name made lowercase.
    kdtkp = models.CharField(db_column='kdTkp', max_length=21)  # Field name made lowercase.
    nourut = models.CharField(db_column='noUrut', max_length=5)  # Field name made lowercase.
    status = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'pcare_pendaftaran'


class PcareTindakanRalanDiberikan(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    nokunjungan = models.CharField(db_column='noKunjungan', max_length=40)  # Field name made lowercase.
    kdtindakansk = models.CharField(db_column='kdTindakanSK', max_length=15, blank=True, null=True)  # Field name made lowercase.
    tgl_perawatan = models.DateField()
    jam = models.TimeField()
    kd_jenis_prw = models.ForeignKey('asuransi.MapingTindakanPcare', on_delete=models.DO_NOTHING, db_column='kd_jenis_prw')
    material = models.FloatField()
    bhp = models.FloatField()
    tarif_tindakandr = models.FloatField()
    tarif_tindakanpr = models.FloatField()
    kso = models.FloatField()
    menejemen = models.FloatField()
    biaya_rawat = models.FloatField()

    class Meta:
        managed = False
        db_table = 'pcare_tindakan_ralan_diberikan'
        unique_together = (('no_rawat', 'nokunjungan', 'tgl_perawatan', 'jam', 'kd_jenis_prw'),)


class PcareKegiatanKelompok(models.Model):
    eduid = models.CharField(db_column='eduId', primary_key=True, max_length=15)  # Field name made lowercase.
    clubid = models.CharField(db_column='clubId', max_length=5, blank=True, null=True)  # Field name made lowercase.
    namaclub = models.CharField(db_column='namaClub', max_length=100)  # Field name made lowercase.
    tglpelayanan = models.DateField(db_column='tglPelayanan', blank=True, null=True)  # Field name made lowercase.
    nmkegiatan = models.CharField(db_column='nmKegiatan', max_length=30, blank=True, null=True)  # Field name made lowercase.
    nmkelompok = models.CharField(db_column='nmKelompok', max_length=30, blank=True, null=True)  # Field name made lowercase.
    materi = models.CharField(max_length=100, blank=True, null=True)
    pembicara = models.CharField(max_length=50, blank=True, null=True)
    lokasi = models.CharField(max_length=50, blank=True, null=True)
    keterangan = models.CharField(max_length=100, blank=True, null=True)
    biaya = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pcare_kegiatan_kelompok'


class PcarePesertaKegiatanKelompok(models.Model):
    eduid = models.OneToOneField(PcareKegiatanKelompok, on_delete=models.DO_NOTHING, db_column='eduId', primary_key=True)  # Field name made lowercase.
    no_rkm_medis = models.ForeignKey('pasien.Pasien', on_delete=models.DO_NOTHING, db_column='no_rkm_medis')

    class Meta:
        managed = False
        db_table = 'pcare_peserta_kegiatan_kelompok'
        unique_together = (('eduid', 'no_rkm_medis'),)


class PcareRujukInternal(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    nokunjungan = models.CharField(db_column='noKunjungan', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tgldaftar = models.DateField(db_column='tglDaftar', blank=True, null=True)  # Field name made lowercase.
    no_rkm_medis = models.CharField(max_length=15, blank=True, null=True)
    nm_pasien = models.CharField(max_length=40, blank=True, null=True)
    nokartu = models.CharField(db_column='noKartu', max_length=25, blank=True, null=True)  # Field name made lowercase.
    kdpoli = models.CharField(db_column='kdPoli', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nmpoli = models.CharField(db_column='nmPoli', max_length=50, blank=True, null=True)  # Field name made lowercase.
    keluhan = models.CharField(max_length=400, blank=True, null=True)
    kdsadar = models.CharField(db_column='kdSadar', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nmsadar = models.CharField(db_column='nmSadar', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sistole = models.CharField(max_length=3, blank=True, null=True)
    diastole = models.CharField(max_length=3, blank=True, null=True)
    beratbadan = models.CharField(db_column='beratBadan', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tinggibadan = models.CharField(db_column='tinggiBadan', max_length=5, blank=True, null=True)  # Field name made lowercase.
    resprate = models.CharField(db_column='respRate', max_length=3, blank=True, null=True)  # Field name made lowercase.
    heartrate = models.CharField(db_column='heartRate', max_length=3, blank=True, null=True)  # Field name made lowercase.
    terapi = models.CharField(max_length=400, blank=True, null=True)
    kdstatuspulang = models.CharField(db_column='kdStatusPulang', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nmstatuspulang = models.CharField(db_column='nmStatusPulang', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tglpulang = models.DateField(db_column='tglPulang', blank=True, null=True)  # Field name made lowercase.
    kddokter = models.CharField(db_column='kdDokter', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nmdokter = models.CharField(db_column='nmDokter', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kddiag1 = models.CharField(db_column='kdDiag1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nmdiag1 = models.CharField(db_column='nmDiag1', max_length=400, blank=True, null=True)  # Field name made lowercase.
    kddiag2 = models.CharField(db_column='kdDiag2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nmdiag2 = models.CharField(db_column='nmDiag2', max_length=400, blank=True, null=True)  # Field name made lowercase.
    kddiag3 = models.CharField(db_column='kdDiag3', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nmdiag3 = models.CharField(db_column='nmDiag3', max_length=400, blank=True, null=True)  # Field name made lowercase.
    kdpolirujukinternal = models.CharField(db_column='kdPoliRujukInternal', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nmpolirujukinternal = models.CharField(db_column='nmPoliRujukInternal', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kdtacc = models.CharField(db_column='kdTACC', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nmtacc = models.CharField(db_column='nmTACC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    alasantacc = models.CharField(db_column='alasanTACC', max_length=400, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pcare_rujuk_internal'


class PcareRujukKhusus(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    nokunjungan = models.CharField(db_column='noKunjungan', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tgldaftar = models.DateField(db_column='tglDaftar', blank=True, null=True)  # Field name made lowercase.
    no_rkm_medis = models.CharField(max_length=15, blank=True, null=True)
    nm_pasien = models.CharField(max_length=40, blank=True, null=True)
    nokartu = models.CharField(db_column='noKartu', max_length=25, blank=True, null=True)  # Field name made lowercase.
    kdpoli = models.CharField(db_column='kdPoli', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nmpoli = models.CharField(db_column='nmPoli', max_length=50, blank=True, null=True)  # Field name made lowercase.
    keluhan = models.CharField(max_length=400, blank=True, null=True)
    kdsadar = models.CharField(db_column='kdSadar', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nmsadar = models.CharField(db_column='nmSadar', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sistole = models.CharField(max_length=3, blank=True, null=True)
    diastole = models.CharField(max_length=3, blank=True, null=True)
    beratbadan = models.CharField(db_column='beratBadan', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tinggibadan = models.CharField(db_column='tinggiBadan', max_length=5, blank=True, null=True)  # Field name made lowercase.
    resprate = models.CharField(db_column='respRate', max_length=3, blank=True, null=True)  # Field name made lowercase.
    heartrate = models.CharField(db_column='heartRate', max_length=3, blank=True, null=True)  # Field name made lowercase.
    terapi = models.CharField(max_length=400, blank=True, null=True)
    kdstatuspulang = models.CharField(db_column='kdStatusPulang', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nmstatuspulang = models.CharField(db_column='nmStatusPulang', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tglpulang = models.DateField(db_column='tglPulang', blank=True, null=True)  # Field name made lowercase.
    kddokter = models.CharField(db_column='kdDokter', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nmdokter = models.CharField(db_column='nmDokter', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kddiag1 = models.CharField(db_column='kdDiag1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nmdiag1 = models.CharField(db_column='nmDiag1', max_length=400, blank=True, null=True)  # Field name made lowercase.
    kddiag2 = models.CharField(db_column='kdDiag2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nmdiag2 = models.CharField(db_column='nmDiag2', max_length=400, blank=True, null=True)  # Field name made lowercase.
    kddiag3 = models.CharField(db_column='kdDiag3', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nmdiag3 = models.CharField(db_column='nmDiag3', max_length=400, blank=True, null=True)  # Field name made lowercase.
    tglestrujuk = models.DateField(db_column='tglEstRujuk', blank=True, null=True)  # Field name made lowercase.
    kdppk = models.CharField(db_column='kdPPK', max_length=15, blank=True, null=True)  # Field name made lowercase.
    kdkhusus = models.CharField(db_column='kdKhusus', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nmkhusus = models.CharField(db_column='nmKhusus', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kdsubspesialis = models.CharField(db_column='kdSubSpesialis', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nmsubspesialis = models.CharField(db_column='nmSubSpesialis', max_length=50, blank=True, null=True)  # Field name made lowercase.
    catatan = models.CharField(max_length=150, blank=True, null=True)
    kdtacc = models.CharField(db_column='kdTACC', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nmtacc = models.CharField(db_column='nmTACC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    alasantacc = models.CharField(db_column='alasanTACC', max_length=400, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pcare_rujuk_khusus'


class PcareRujukSubspesialis(models.Model):
    no_rawat = models.OneToOneField('RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    nokunjungan = models.CharField(db_column='noKunjungan', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tgldaftar = models.DateField(db_column='tglDaftar', blank=True, null=True)  # Field name made lowercase.
    no_rkm_medis = models.CharField(max_length=15, blank=True, null=True)
    nm_pasien = models.CharField(max_length=40, blank=True, null=True)
    nokartu = models.CharField(db_column='noKartu', max_length=25, blank=True, null=True)  # Field name made lowercase.
    kdpoli = models.CharField(db_column='kdPoli', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nmpoli = models.CharField(db_column='nmPoli', max_length=50, blank=True, null=True)  # Field name made lowercase.
    keluhan = models.CharField(max_length=400, blank=True, null=True)
    kdsadar = models.CharField(db_column='kdSadar', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nmsadar = models.CharField(db_column='nmSadar', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sistole = models.CharField(max_length=3, blank=True, null=True)
    diastole = models.CharField(max_length=3, blank=True, null=True)
    beratbadan = models.CharField(db_column='beratBadan', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tinggibadan = models.CharField(db_column='tinggiBadan', max_length=5, blank=True, null=True)  # Field name made lowercase.
    resprate = models.CharField(db_column='respRate', max_length=3, blank=True, null=True)  # Field name made lowercase.
    heartrate = models.CharField(db_column='heartRate', max_length=3, blank=True, null=True)  # Field name made lowercase.
    terapi = models.CharField(max_length=400, blank=True, null=True)
    kdstatuspulang = models.CharField(db_column='kdStatusPulang', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nmstatuspulang = models.CharField(db_column='nmStatusPulang', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tglpulang = models.DateField(db_column='tglPulang', blank=True, null=True)  # Field name made lowercase.
    kddokter = models.CharField(db_column='kdDokter', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nmdokter = models.CharField(db_column='nmDokter', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kddiag1 = models.CharField(db_column='kdDiag1', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nmdiag1 = models.CharField(db_column='nmDiag1', max_length=400, blank=True, null=True)  # Field name made lowercase.
    kddiag2 = models.CharField(db_column='kdDiag2', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nmdiag2 = models.CharField(db_column='nmDiag2', max_length=400, blank=True, null=True)  # Field name made lowercase.
    kddiag3 = models.CharField(db_column='kdDiag3', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nmdiag3 = models.CharField(db_column='nmDiag3', max_length=400, blank=True, null=True)  # Field name made lowercase.
    tglestrujuk = models.DateField(db_column='tglEstRujuk', blank=True, null=True)  # Field name made lowercase.
    kdppk = models.CharField(db_column='kdPPK', max_length=15, blank=True, null=True)  # Field name made lowercase.
    nmppk = models.CharField(db_column='nmPPK', max_length=100)  # Field name made lowercase.
    kdsubspesialis = models.CharField(db_column='kdSubSpesialis', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nmsubspesialis = models.CharField(db_column='nmSubSpesialis', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kdsarana = models.CharField(db_column='kdSarana', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nmsarana = models.CharField(db_column='nmSarana', max_length=50, blank=True, null=True)  # Field name made lowercase.
    kdtacc = models.CharField(db_column='kdTACC', max_length=5, blank=True, null=True)  # Field name made lowercase.
    nmtacc = models.CharField(db_column='nmTACC', max_length=50, blank=True, null=True)  # Field name made lowercase.
    alasantacc = models.CharField(db_column='alasanTACC', max_length=400, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pcare_rujuk_subspesialis'
        
        
class KategoriPerawatan(models.Model):
    kd_kategori = models.CharField(primary_key=True, max_length=5)
    nm_kategori = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kategori_perawatan'
        
        
class JnsPerawatan(models.Model):
    kd_jenis_prw = models.CharField(primary_key=True, max_length=15)
    nm_perawatan = models.CharField(max_length=80, blank=True, null=True)
    kd_kategori = models.ForeignKey('KategoriPerawatan', on_delete=models.DO_NOTHING, db_column='kd_kategori', blank=True, null=True)
    material = models.FloatField(blank=True, null=True)
    bhp = models.FloatField()
    tarif_tindakandr = models.FloatField(blank=True, null=True)
    tarif_tindakanpr = models.FloatField(blank=True, null=True)
    kso = models.FloatField(blank=True, null=True)
    menejemen = models.FloatField(blank=True, null=True)
    total_byrdr = models.FloatField(blank=True, null=True)
    total_byrpr = models.FloatField(blank=True, null=True)
    total_byrdrpr = models.FloatField()
    kd_pj = models.ForeignKey('asuransi.Penjab', on_delete=models.DO_NOTHING, db_column='kd_pj')
    kd_poli = models.ForeignKey('bangsal.Poliklinik', on_delete=models.DO_NOTHING, db_column='kd_poli')
    status = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'jns_perawatan'


class SetOtomatisTindakanRalan(models.Model):
    kd_dokter = models.OneToOneField('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter', primary_key=True)
    kd_jenis_prw = models.ForeignKey(JnsPerawatan, on_delete=models.DO_NOTHING, db_column='kd_jenis_prw')
    kd_pj = models.ForeignKey('asuransi.Penjab', on_delete=models.DO_NOTHING, db_column='kd_pj')

    class Meta:
        managed = False
        db_table = 'set_otomatis_tindakan_ralan'
        unique_together = (('kd_dokter', 'kd_jenis_prw', 'kd_pj'),)


class SetOtomatisTindakanRalanDokterpetugas(models.Model):
    kd_dokter = models.OneToOneField('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter', primary_key=True)
    kd_jenis_prw = models.ForeignKey(JnsPerawatan, on_delete=models.DO_NOTHING, db_column='kd_jenis_prw')
    kd_pj = models.ForeignKey('asuransi.Penjab', on_delete=models.DO_NOTHING, db_column='kd_pj')

    class Meta:
        managed = False
        db_table = 'set_otomatis_tindakan_ralan_dokterpetugas'
        unique_together = (('kd_dokter', 'kd_jenis_prw', 'kd_pj'),)


class SetOtomatisTindakanRalanPetugas(models.Model):
    kd_jenis_prw = models.OneToOneField(JnsPerawatan, on_delete=models.DO_NOTHING, db_column='kd_jenis_prw', primary_key=True)
    kd_pj = models.ForeignKey('asuransi.Penjab', on_delete=models.DO_NOTHING, db_column='kd_pj')

    class Meta:
        managed = False
        db_table = 'set_otomatis_tindakan_ralan_petugas'
        unique_together = (('kd_jenis_prw', 'kd_pj'),)


class RawatJlDr(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    kd_jenis_prw = models.ForeignKey(JnsPerawatan, on_delete=models.DO_NOTHING, db_column='kd_jenis_prw')
    kd_dokter = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter')
    tgl_perawatan = models.DateField()
    jam_rawat = models.TimeField()
    material = models.FloatField()
    bhp = models.FloatField()
    tarif_tindakandr = models.FloatField()
    kso = models.FloatField(blank=True, null=True)
    menejemen = models.FloatField(blank=True, null=True)
    biaya_rawat = models.FloatField(blank=True, null=True)
    stts_bayar = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rawat_jl_dr'
        unique_together = (('no_rawat', 'kd_jenis_prw', 'kd_dokter', 'tgl_perawatan', 'jam_rawat'),)


class RawatJlDrpr(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    kd_jenis_prw = models.ForeignKey(JnsPerawatan, on_delete=models.DO_NOTHING, db_column='kd_jenis_prw')
    kd_dokter = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter')
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip')
    tgl_perawatan = models.DateField()
    jam_rawat = models.TimeField()
    material = models.FloatField(blank=True, null=True)
    bhp = models.FloatField()
    tarif_tindakandr = models.FloatField(blank=True, null=True)
    tarif_tindakanpr = models.FloatField(blank=True, null=True)
    kso = models.FloatField(blank=True, null=True)
    menejemen = models.FloatField(blank=True, null=True)
    biaya_rawat = models.FloatField(blank=True, null=True)
    stts_bayar = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rawat_jl_drpr'
        unique_together = (('no_rawat', 'kd_jenis_prw', 'kd_dokter', 'nip', 'tgl_perawatan', 'jam_rawat'),)


class RawatJlPr(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    kd_jenis_prw = models.ForeignKey(JnsPerawatan, on_delete=models.DO_NOTHING, db_column='kd_jenis_prw')
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip')
    tgl_perawatan = models.DateField()
    jam_rawat = models.TimeField()
    material = models.FloatField()
    bhp = models.FloatField()
    tarif_tindakanpr = models.FloatField()
    kso = models.FloatField(blank=True, null=True)
    menejemen = models.FloatField(blank=True, null=True)
    biaya_rawat = models.FloatField(blank=True, null=True)
    stts_bayar = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rawat_jl_pr'
        unique_together = (('no_rawat', 'kd_jenis_prw', 'nip', 'tgl_perawatan', 'jam_rawat'),)


class Hemodialisa(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    tanggal = models.DateTimeField()
    kd_dokter = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter', blank=True, null=True)
    lama = models.CharField(max_length=5, blank=True, null=True)
    akses = models.CharField(max_length=30, blank=True, null=True)
    dialist = models.CharField(max_length=30, blank=True, null=True)
    transfusi = models.CharField(max_length=5, blank=True, null=True)
    penarikan = models.CharField(max_length=5, blank=True, null=True)
    qb = models.CharField(max_length=5, blank=True, null=True)
    qd = models.CharField(max_length=5, blank=True, null=True)
    ureum = models.CharField(max_length=10, blank=True, null=True)
    hb = models.CharField(max_length=10, blank=True, null=True)
    hbsag = models.CharField(max_length=10, blank=True, null=True)
    creatinin = models.CharField(max_length=10, blank=True, null=True)
    hiv = models.CharField(max_length=10, blank=True, null=True)
    hcv = models.CharField(max_length=10, blank=True, null=True)
    lain = models.CharField(max_length=200, blank=True, null=True)
    kd_penyakit = models.ForeignKey('diagnosa.Penyakit', on_delete=models.DO_NOTHING, db_column='kd_penyakit', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hemodialisa'
        unique_together = (('no_rawat', 'tanggal'),)


