from django.db import models

# Create your models here.

class KelompokJabatan(models.Model):
    kode_kelompok = models.CharField(primary_key=True, max_length=3)
    nama_kelompok = models.CharField(max_length=100, blank=True, null=True)
    indek = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kelompok_jabatan'
        
        
class Pendidikan(models.Model):
    tingkat = models.CharField(primary_key=True, max_length=80)
    indek = models.IntegerField()
    gapok1 = models.FloatField()
    kenaikan = models.FloatField()
    maksimal = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'pendidikan'


class JnjJabatan(models.Model):
    kode = models.CharField(primary_key=True, max_length=10)
    nama = models.CharField(max_length=50)
    tnj = models.FloatField()
    indek = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jnj_jabatan'
        
        
class Jabatan(models.Model):
    kd_jbtn = models.CharField(primary_key=True, max_length=4)
    nm_jbtn = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jabatan'
        

class ResikoKerja(models.Model):
    kode_resiko = models.CharField(primary_key=True, max_length=3)
    nama_resiko = models.CharField(max_length=200, blank=True, null=True)
    indek = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resiko_kerja'
        
        
class SttsKerja(models.Model):
    stts = models.CharField(primary_key=True, max_length=3)
    ktg = models.CharField(max_length=20)
    indek = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stts_kerja'


class SttsWp(models.Model):
    stts = models.CharField(primary_key=True, max_length=5)
    ktg = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'stts_wp'


class Pegawai(models.Model):
    nik = models.CharField(unique=True, max_length=20)
    nama = models.CharField(max_length=50)
    jk = models.CharField(max_length=6)
    jbtn = models.CharField(max_length=25)
    jnj_jabatan = models.ForeignKey(JnjJabatan, on_delete=models.DO_NOTHING, db_column='jnj_jabatan', null=True)
    kode_kelompok = models.ForeignKey(KelompokJabatan, on_delete=models.DO_NOTHING, db_column='kode_kelompok', null=True)
    kode_resiko = models.ForeignKey('ResikoKerja', on_delete=models.DO_NOTHING, db_column='kode_resiko', null=True)
    kode_emergency = models.ForeignKey('igd.EmergencyIndex', on_delete=models.DO_NOTHING, db_column='kode_emergency', null=True)
    departemen = models.ForeignKey('bangsal.Departemen', on_delete=models.DO_NOTHING, db_column='departemen', related_name='departemen_pegawai', null=True)
    bidang = models.ForeignKey('bangsal.Bidang', on_delete=models.DO_NOTHING, db_column='bidang', null=True)
    stts_wp = models.ForeignKey('SttsWp', on_delete=models.DO_NOTHING, db_column='stts_wp', null=True)
    stts_kerja = models.ForeignKey('SttsKerja', on_delete=models.DO_NOTHING, db_column='stts_kerja', null=True)
    npwp = models.CharField(max_length=15)
    pendidikan = models.ForeignKey('Pendidikan', on_delete=models.DO_NOTHING, db_column='pendidikan', null=True)
    gapok = models.FloatField()
    tmp_lahir = models.CharField(max_length=20)
    tgl_lahir = models.DateField()
    alamat = models.CharField(max_length=60)
    kota = models.CharField(max_length=20)
    mulai_kerja = models.DateField()
    ms_kerja = models.CharField(max_length=4)
    indexins = models.ForeignKey('bangsal.Departemen', on_delete=models.DO_NOTHING, db_column='indexins', related_name='indexians_pegawai', null=True)
    bpd = models.ForeignKey('keuangan.Bank', on_delete=models.DO_NOTHING, db_column='bpd', null=True)
    rekening = models.CharField(max_length=25)
    stts_aktif = models.CharField(max_length=11)
    wajibmasuk = models.IntegerField()
    pengurang = models.FloatField()
    indek = models.IntegerField()
    mulai_kontrak = models.DateField(blank=True, null=True)
    cuti_diambil = models.IntegerField()
    dankes = models.FloatField()
    photo = models.CharField(max_length=500, blank=True, null=True)
    no_ktp = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'pegawai'
        
    def __str__(self):
        return f'{self.nik} - {self.nama}'
        
        
class Tambahjaga(models.Model):
    tgl = models.DateField(primary_key=True)
    id = models.ForeignKey(Pegawai, on_delete=models.DO_NOTHING, db_column='id')
    jml = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tambahjaga'
        unique_together = (('tgl', 'id'),)


class Spesialis(models.Model):
    kd_sps = models.CharField(primary_key=True, max_length=5)
    nm_sps = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spesialis'
    
    def __str__(self):
        return self.nm_sps
        

class Dokter(models.Model):
    kd_dokter = models.OneToOneField(Pegawai, on_delete=models.DO_NOTHING, primary_key=True, db_column='kd_dokter', to_field='nik')
    nm_dokter = models.CharField(max_length=50, blank=True, null=True)
    jk = models.CharField(max_length=1, blank=True, null=True)
    tmp_lahir = models.CharField(max_length=20, blank=True, null=True)
    tgl_lahir = models.DateField(blank=True, null=True)
    gol_drh = models.CharField(max_length=2, blank=True, null=True)
    agama = models.CharField(max_length=12, blank=True, null=True)
    almt_tgl = models.CharField(max_length=60, blank=True, null=True)
    no_telp = models.CharField(max_length=13, blank=True, null=True)
    stts_nikah = models.CharField(max_length=13, blank=True, null=True)
    kd_sps = models.ForeignKey('Spesialis', on_delete=models.DO_NOTHING, db_column='kd_sps', blank=True, null=True)
    alumni = models.CharField(max_length=60, blank=True, null=True)
    no_ijn_praktek = models.CharField(max_length=120, blank=True, null=True)
    status = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'dokter'
        
    def __str__(self):
        return self.nm_dokter

class Petugas(models.Model):
    nip = models.OneToOneField(Pegawai, on_delete=models.DO_NOTHING, db_column='nip', primary_key=True)
    nama = models.CharField(max_length=50, blank=True, null=True)
    jk = models.CharField(max_length=1, blank=True, null=True)
    tmp_lahir = models.CharField(max_length=20, blank=True, null=True)
    tgl_lahir = models.DateField(blank=True, null=True)
    gol_darah = models.CharField(max_length=2, blank=True, null=True)
    agama = models.CharField(max_length=12, blank=True, null=True)
    stts_nikah = models.CharField(max_length=13, blank=True, null=True)
    alamat = models.CharField(max_length=60, blank=True, null=True)
    kd_jbtn = models.ForeignKey(Jabatan, on_delete=models.DO_NOTHING, db_column='kd_jbtn', blank=True, null=True)
    no_telp = models.CharField(max_length=13, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'petugas'
        
        
class RiwayatJabatan(models.Model):
    id = models.OneToOneField(Pegawai, on_delete=models.DO_NOTHING, db_column='id', primary_key=True)
    jabatan = models.CharField(max_length=50)
    tmt_pangkat = models.DateField()
    tmt_pangkat_yad = models.DateField()
    pejabat_penetap = models.CharField(max_length=50)
    nomor_sk = models.CharField(max_length=25)
    tgl_sk = models.DateField()
    dasar_peraturan = models.CharField(max_length=50)
    masa_kerja = models.IntegerField()
    bln_kerja = models.IntegerField()
    berkas = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'riwayat_jabatan'
        unique_together = (('id', 'jabatan'),)

class RiwayatPendidikan(models.Model):
    id = models.OneToOneField(Pegawai, on_delete=models.DO_NOTHING, db_column='id', primary_key=True)
    pendidikan = models.CharField(max_length=11)
    sekolah = models.CharField(max_length=50)
    jurusan = models.CharField(max_length=40)
    thn_lulus = models.TextField()  # This field type is a guess.
    kepala = models.CharField(max_length=50)
    pendanaan = models.CharField(max_length=28)
    keterangan = models.CharField(max_length=50)
    status = models.CharField(max_length=40)
    berkas = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'riwayat_pendidikan'
        unique_together = (('id', 'pendidikan', 'sekolah'),)


class RiwayatPenelitian(models.Model):
    id = models.OneToOneField(Pegawai, on_delete=models.DO_NOTHING, db_column='id', primary_key=True)
    jenis_penelitian = models.CharField(max_length=30)
    peranan = models.CharField(max_length=30)
    judul_penelitian = models.CharField(max_length=60)
    judul_jurnal = models.CharField(max_length=60)
    tahun = models.TextField()  # This field type is a guess.
    biaya_penelitian = models.FloatField(blank=True, null=True)
    asal_dana = models.CharField(max_length=30)
    berkas = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'riwayat_penelitian'
        unique_together = (('id', 'judul_penelitian', 'tahun'),)


class RiwayatPenghargaan(models.Model):
    id = models.OneToOneField(Pegawai, on_delete=models.DO_NOTHING, db_column='id', primary_key=True)
    jenis = models.CharField(max_length=30)
    nama_penghargaan = models.CharField(max_length=60)
    tanggal = models.DateField()
    instansi = models.CharField(max_length=40)
    pejabat_pemberi = models.CharField(max_length=40)
    berkas = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'riwayat_penghargaan'
        unique_together = (('id', 'nama_penghargaan', 'tanggal'),)


class RiwayatSeminar(models.Model):
    id = models.OneToOneField(Pegawai, on_delete=models.DO_NOTHING, db_column='id', primary_key=True)
    tingkat = models.CharField(max_length=13)
    jenis = models.CharField(max_length=9)
    nama_seminar = models.CharField(max_length=50)
    peranan = models.CharField(max_length=40)
    mulai = models.DateField()
    selesai = models.DateField()
    penyelengara = models.CharField(max_length=50)
    tempat = models.CharField(max_length=50)
    berkas = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'riwayat_seminar'
        unique_together = (('id', 'nama_seminar', 'mulai'),)


class MasterBerkasPegawai(models.Model):
    kode = models.CharField(primary_key=True, max_length=10)
    kategori = models.CharField(max_length=31)
    nama_berkas = models.CharField(max_length=300)
    no_urut = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'master_berkas_pegawai'


class PembagianAkte(models.Model):
    id = models.OneToOneField(Pegawai, on_delete=models.DO_NOTHING, db_column='id', primary_key=True)
    persen = models.FloatField()

    class Meta:
        managed = False
        db_table = 'pembagian_akte'


class PembagianResume(models.Model):
    id = models.OneToOneField(Pegawai, on_delete=models.DO_NOTHING, db_column='id', primary_key=True)
    persen = models.FloatField()

    class Meta:
        managed = False
        db_table = 'pembagian_resume'


class PembagianWarung(models.Model):
    id = models.OneToOneField(Pegawai, on_delete=models.DO_NOTHING, db_column='id', primary_key=True)
    persen = models.FloatField()

    class Meta:
        managed = False
        db_table = 'pembagian_warung'
        
        
class Jgmlm(models.Model):
    tgl = models.DateField(primary_key=True)
    id = models.ForeignKey('Pegawai', on_delete=models.DO_NOTHING, db_column='id')
    jml = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jgmlm'
        unique_together = (('tgl', 'id'),)


class AngsuranKoperasi(models.Model):
    id = models.OneToOneField('Pegawai', on_delete=models.DO_NOTHING, db_column='id', primary_key=True)
    tanggal_pinjam = models.DateField()
    tanggal_angsur = models.DateField()
    pokok = models.FloatField()
    jasa = models.FloatField()

    class Meta:
        managed = False
        db_table = 'angsuran_koperasi'
        unique_together = (('id', 'tanggal_pinjam', 'tanggal_angsur'),)
        
        
class Potongan(models.Model):
    tahun = models.TextField(primary_key=True)  # This field type is a guess.
    bulan = models.IntegerField()
    id = models.ForeignKey(Pegawai, on_delete=models.DO_NOTHING, db_column='id')
    bpjs = models.FloatField()
    jamsostek = models.FloatField()
    dansos = models.FloatField()
    simwajib = models.FloatField()
    angkop = models.FloatField()
    angla = models.FloatField()
    telpri = models.FloatField()
    pajak = models.FloatField()
    pribadi = models.FloatField()
    lain = models.FloatField()
    ktg = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'potongan'
        unique_together = (('tahun', 'bulan', 'id'),)
        
        
class Barcode(models.Model):
    id = models.OneToOneField('Pegawai', on_delete=models.DO_NOTHING, db_column='id', primary_key=True)
    barcode = models.CharField(unique=True, max_length=25)

    class Meta:
        managed = False
        db_table = 'barcode'
        
        
class BerkasPegawai(models.Model):
    nik = models.ForeignKey('Pegawai', on_delete=models.DO_NOTHING, db_column='nik')
    tgl_uploud = models.DateField()
    kode_berkas = models.ForeignKey('MasterBerkasPegawai', on_delete=models.DO_NOTHING, db_column='kode_berkas')
    berkas = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'berkas_pegawai'


class EvaluasiKinerja(models.Model):
    kode_evaluasi = models.CharField(primary_key=True, max_length=3)
    nama_evaluasi = models.CharField(max_length=200, blank=True, null=True)
    indek = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaluasi_kinerja'


class EvaluasiKinerjaPegawai(models.Model):
    id = models.OneToOneField('Pegawai', on_delete=models.DO_NOTHING, db_column='id', primary_key=True)
    kode_evaluasi = models.ForeignKey(EvaluasiKinerja, on_delete=models.DO_NOTHING, db_column='kode_evaluasi')
    tahun = models.TextField()  # This field type is a guess.
    bulan = models.IntegerField()
    keterangan = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaluasi_kinerja_pegawai'
        unique_together = (('id', 'kode_evaluasi', 'tahun', 'bulan'),)


class Sidikjari(models.Model):
    id = models.OneToOneField(Pegawai, on_delete=models.DO_NOTHING, db_column='id', primary_key=True)
    sidikjari = models.TextField()

    class Meta:
        managed = False
        db_table = 'sidikjari'


class TemporaryPresensi(models.Model):
    id = models.OneToOneField(Pegawai, on_delete=models.DO_NOTHING, db_column='id', primary_key=True)
    shift = models.CharField(max_length=13)
    jam_datang = models.DateTimeField(blank=True, null=True)
    jam_pulang = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=25)
    keterlambatan = models.CharField(max_length=20)
    durasi = models.CharField(max_length=20, blank=True, null=True)
    photo = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'temporary_presensi'


class Presensi(models.Model):
    tgl = models.DateField(primary_key=True)
    id = models.ForeignKey(Pegawai, on_delete=models.DO_NOTHING, db_column='id')
    jns = models.CharField(max_length=2)
    lembur = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'presensi'
        unique_together = (('tgl', 'id'),)


class RekapPresensi(models.Model):
    id = models.OneToOneField(Pegawai, on_delete=models.DO_NOTHING, db_column='id', primary_key=True)
    shift = models.CharField(max_length=13)
    jam_datang = models.DateTimeField()
    jam_pulang = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=25)
    keterlambatan = models.CharField(max_length=20)
    durasi = models.CharField(max_length=20, blank=True, null=True)
    keterangan = models.CharField(max_length=100)
    photo = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'rekap_presensi'
        unique_together = (('id', 'jam_datang'),)



class JadwalPegawai(models.Model):
    id = models.OneToOneField('Pegawai', on_delete=models.DO_NOTHING, db_column='id', primary_key=True)
    tahun = models.TextField()  # This field type is a guess.
    bulan = models.CharField(max_length=2)
    h1 = models.CharField(max_length=13)
    h2 = models.CharField(max_length=13)
    h3 = models.CharField(max_length=13)
    h4 = models.CharField(max_length=13)
    h5 = models.CharField(max_length=13)
    h6 = models.CharField(max_length=13)
    h7 = models.CharField(max_length=13)
    h8 = models.CharField(max_length=13)
    h9 = models.CharField(max_length=13)
    h10 = models.CharField(max_length=13)
    h11 = models.CharField(max_length=13)
    h12 = models.CharField(max_length=13)
    h13 = models.CharField(max_length=13)
    h14 = models.CharField(max_length=13)
    h15 = models.CharField(max_length=13)
    h16 = models.CharField(max_length=13)
    h17 = models.CharField(max_length=13)
    h18 = models.CharField(max_length=13)
    h19 = models.CharField(max_length=13)
    h20 = models.CharField(max_length=13)
    h21 = models.CharField(max_length=13)
    h22 = models.CharField(max_length=13)
    h23 = models.CharField(max_length=13)
    h24 = models.CharField(max_length=13)
    h25 = models.CharField(max_length=13)
    h26 = models.CharField(max_length=13)
    h27 = models.CharField(max_length=13)
    h28 = models.CharField(max_length=13)
    h29 = models.CharField(max_length=13)
    h30 = models.CharField(max_length=13)
    h31 = models.CharField(max_length=13)

    class Meta:
        managed = False
        db_table = 'jadwal_pegawai'
        unique_together = (('id', 'tahun', 'bulan'),)


class JadwalTambahan(models.Model):
    id = models.OneToOneField('Pegawai', on_delete=models.DO_NOTHING, db_column='id', primary_key=True)
    tahun = models.TextField()  # This field type is a guess.
    bulan = models.CharField(max_length=2)
    h1 = models.CharField(max_length=13)
    h2 = models.CharField(max_length=13)
    h3 = models.CharField(max_length=13)
    h4 = models.CharField(max_length=13)
    h5 = models.CharField(max_length=13)
    h6 = models.CharField(max_length=13)
    h7 = models.CharField(max_length=13)
    h8 = models.CharField(max_length=13)
    h9 = models.CharField(max_length=13)
    h10 = models.CharField(max_length=13)
    h11 = models.CharField(max_length=13)
    h12 = models.CharField(max_length=13)
    h13 = models.CharField(max_length=13)
    h14 = models.CharField(max_length=13)
    h15 = models.CharField(max_length=13)
    h16 = models.CharField(max_length=13)
    h17 = models.CharField(max_length=13)
    h18 = models.CharField(max_length=13)
    h19 = models.CharField(max_length=13)
    h20 = models.CharField(max_length=13)
    h21 = models.CharField(max_length=13)
    h22 = models.CharField(max_length=13)
    h23 = models.CharField(max_length=13)
    h24 = models.CharField(max_length=13)
    h25 = models.CharField(max_length=13)
    h26 = models.CharField(max_length=13)
    h27 = models.CharField(max_length=13)
    h28 = models.CharField(max_length=13)
    h29 = models.CharField(max_length=13)
    h30 = models.CharField(max_length=13)
    h31 = models.CharField(max_length=13)

    class Meta:
        managed = False
        db_table = 'jadwal_tambahan'
        unique_together = (('id', 'tahun', 'bulan'),)
        
        
class JamJaga(models.Model):
    no_id = models.AutoField(primary_key=True)
    dep = models.ForeignKey('bangsal.Departemen', on_delete=models.DO_NOTHING)
    shift = models.CharField(max_length=13)
    jam_masuk = models.TimeField()
    jam_pulang = models.TimeField()

    class Meta:
        managed = False
        db_table = 'jam_jaga'
        unique_together = (('dep', 'shift'),)


class JamMasuk(models.Model):
    shift = models.CharField(primary_key=True, max_length=13)
    jam_masuk = models.TimeField()
    jam_pulang = models.TimeField()

    class Meta:
        managed = False
        db_table = 'jam_masuk'


class Koperasi(models.Model):
    stts = models.CharField(primary_key=True, max_length=5)
    wajib = models.FloatField()

    class Meta:
        managed = False
        db_table = 'koperasi'


class Keanggotaan(models.Model):
    id = models.OneToOneField('Pegawai', on_delete=models.DO_NOTHING, db_column='id', primary_key=True)
    koperasi = models.ForeignKey('Koperasi', on_delete=models.DO_NOTHING, db_column='koperasi')
    jamsostek = models.ForeignKey('asuransi.Jamsostek', on_delete=models.DO_NOTHING, db_column='jamsostek')
    bpjs = models.ForeignKey('asuransi.Bpjs', on_delete=models.DO_NOTHING, db_column='bpjs')

    class Meta:
        managed = False
        db_table = 'keanggotaan'


class Ketidakhadiran(models.Model):
    tgl = models.DateField(primary_key=True)
    id = models.ForeignKey('Pegawai', on_delete=models.DO_NOTHING, db_column='id')
    jns = models.CharField(max_length=1)
    ktg = models.CharField(max_length=40)
    jml = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ketidakhadiran'
        unique_together = (('tgl', 'id', 'jns'),)


class PeminjamanKoperasi(models.Model):
    id = models.OneToOneField(Pegawai, on_delete=models.DO_NOTHING, db_column='id', primary_key=True)
    tanggal = models.DateField()
    pinjaman = models.FloatField()
    banyak_angsur = models.IntegerField()
    pokok = models.FloatField()
    jasa = models.FloatField()
    status = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'peminjaman_koperasi'
        unique_together = (('id', 'tanggal'),)


class PencapaianKinerja(models.Model):
    kode_pencapaian = models.CharField(primary_key=True, max_length=3)
    nama_pencapaian = models.CharField(max_length=200, blank=True, null=True)
    indek = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pencapaian_kinerja'


class PencapaianKinerjaPegawai(models.Model):
    id = models.OneToOneField(Pegawai, on_delete=models.DO_NOTHING, db_column='id', primary_key=True)
    kode_pencapaian = models.ForeignKey(PencapaianKinerja, on_delete=models.DO_NOTHING, db_column='kode_pencapaian')
    tahun = models.TextField()  # This field type is a guess.
    bulan = models.IntegerField()
    keterangan = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pencapaian_kinerja_pegawai'
        unique_together = (('id', 'kode_pencapaian', 'tahun', 'bulan'),)


class PengajuanCuti(models.Model):
    no_pengajuan = models.CharField(primary_key=True, max_length=17)
    tanggal = models.DateField()
    tanggal_awal = models.DateField()
    tanggal_akhir = models.DateField()
    nik = models.ForeignKey(Pegawai, on_delete=models.DO_NOTHING, db_column='nik', related_name='nik_pegawai')
    urgensi = models.CharField(max_length=18)
    alamat = models.CharField(max_length=100)
    jumlah = models.IntegerField()
    kepentingan = models.CharField(max_length=70)
    nik_pj = models.ForeignKey(Pegawai, on_delete=models.DO_NOTHING, db_column='nik_pj', related_name='nik_pj_pegawai')
    status = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'pengajuan_cuti'
        
        
class SetJgmlm(models.Model):
    tnj = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'set_jgmlm'


class SetJgtambah(models.Model):
    tnj = models.FloatField()
    pendidikan = models.OneToOneField('pegawai.Pendidikan', on_delete=models.DO_NOTHING, db_column='pendidikan', primary_key=True)

    class Meta:
        managed = False
        db_table = 'set_jgtambah'


class SetKeterlambatan(models.Model):
    toleransi = models.IntegerField(blank=True, null=True)
    terlambat1 = models.IntegerField(blank=True, null=True)
    terlambat2 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'set_keterlambatan'


class SetLemburhb(models.Model):
    tnj = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'set_lemburhb'


class SetLemburhr(models.Model):
    tnj = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'set_lemburhr'

