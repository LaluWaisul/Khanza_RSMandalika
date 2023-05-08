# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AmbilDankes(models.Model):
    id = models.OneToOneField('pegawai.Pegawai', on_delete=models.DO_NOTHING, db_column='id', primary_key=True)
    tanggal = models.DateField()
    ktg = models.CharField(max_length=50)
    dankes = models.FloatField()

    class Meta:
        managed = False
        db_table = 'ambil_dankes'
        unique_together = (('id', 'tanggal'),)


class Antriloket(models.Model):
    loket = models.IntegerField()
    antrian = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'antriloket'


class AplicareKetersediaanKamar(models.Model):
    kode_kelas_aplicare = models.CharField(primary_key=True, max_length=15)
    kd_bangsal = models.ForeignKey('bangsal.Bangsal', on_delete=models.DO_NOTHING, db_column='kd_bangsal')
    kelas = models.CharField(max_length=11)
    kapasitas = models.IntegerField(blank=True, null=True)
    tersedia = models.IntegerField(blank=True, null=True)
    tersediapria = models.IntegerField(blank=True, null=True)
    tersediawanita = models.IntegerField(blank=True, null=True)
    tersediapriawanita = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aplicare_ketersediaan_kamar'
        unique_together = (('kode_kelas_aplicare', 'kd_bangsal', 'kelas'),)


class BalasanPengaduan(models.Model):
    id_pengaduan = models.OneToOneField('Pengaduan', on_delete=models.DO_NOTHING, db_column='id_pengaduan', primary_key=True)
    pesan_balasan = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'balasan_pengaduan'


class BerkasDigitalPerawatan(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    kode = models.ForeignKey('MasterBerkasDigital', on_delete=models.DO_NOTHING, db_column='kode')
    lokasi_file = models.CharField(max_length=600)

    class Meta:
        managed = False
        db_table = 'berkas_digital_perawatan'
        unique_together = (('no_rawat', 'kode', 'lokasi_file'),)


class DataHais(models.Model):
    tanggal = models.DateField(primary_key=True)
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat')
    ett = models.IntegerField(db_column='ETT', blank=True, null=True)  # Field name made lowercase.
    cvl = models.IntegerField(db_column='CVL', blank=True, null=True)  # Field name made lowercase.
    ivl = models.IntegerField(db_column='IVL', blank=True, null=True)  # Field name made lowercase.
    uc = models.IntegerField(db_column='UC', blank=True, null=True)  # Field name made lowercase.
    vap = models.IntegerField(db_column='VAP', blank=True, null=True)  # Field name made lowercase.
    iad = models.IntegerField(db_column='IAD', blank=True, null=True)  # Field name made lowercase.
    pleb = models.IntegerField(db_column='PLEB', blank=True, null=True)  # Field name made lowercase.
    isk = models.IntegerField(db_column='ISK', blank=True, null=True)  # Field name made lowercase.
    ilo = models.IntegerField(db_column='ILO')  # Field name made lowercase.
    hap = models.IntegerField(db_column='HAP', blank=True, null=True)  # Field name made lowercase.
    tinea = models.IntegerField(db_column='Tinea', blank=True, null=True)  # Field name made lowercase.
    scabies = models.IntegerField(db_column='Scabies', blank=True, null=True)  # Field name made lowercase.
    deku = models.CharField(db_column='DEKU', max_length=5, blank=True, null=True)  # Field name made lowercase.
    sputum = models.CharField(db_column='SPUTUM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    darah = models.CharField(db_column='DARAH', max_length=200, blank=True, null=True)  # Field name made lowercase.
    urine = models.CharField(db_column='URINE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    antibiotik = models.CharField(db_column='ANTIBIOTIK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    kd_kamar = models.ForeignKey('bangsal.Kamar', on_delete=models.DO_NOTHING, db_column='kd_kamar', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_hais'
        unique_together = (('tanggal', 'no_rawat'),)


class DataTb(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    id_tb_03 = models.CharField(max_length=30, blank=True, null=True)
    id_periode_laporan = models.CharField(max_length=20, blank=True, null=True)
    tanggal_buat_laporan = models.DateTimeField(blank=True, null=True)
    tahun_buat_laporan = models.TextField(blank=True, null=True)  # This field type is a guess.
    kd_wasor = models.IntegerField(blank=True, null=True)
    noregkab = models.IntegerField(blank=True, null=True)
    id_propinsi = models.CharField(max_length=15, blank=True, null=True)
    kd_kabupaten = models.CharField(max_length=15, blank=True, null=True)
    id_kecamatan = models.CharField(max_length=15, blank=True, null=True)
    id_kelurahan = models.CharField(max_length=15, blank=True, null=True)
    nama_rujukan = models.CharField(max_length=25, blank=True, null=True)
    sebutkan1 = models.CharField(max_length=100, blank=True, null=True)
    tipe_diagnosis = models.CharField(max_length=27, blank=True, null=True)
    klasifikasi_lokasi_anatomi = models.CharField(max_length=10, blank=True, null=True)
    klasifikasi_riwayat_pengobatan = models.CharField(max_length=45, blank=True, null=True)
    klasifikasi_status_hiv = models.CharField(max_length=15, blank=True, null=True)
    total_skoring_anak = models.CharField(max_length=15, blank=True, null=True)
    konfirmasiskoring5 = models.CharField(db_column='konfirmasiSkoring5', max_length=24, blank=True, null=True)  # Field name made lowercase.
    konfirmasiskoring6 = models.CharField(db_column='konfirmasiSkoring6', max_length=26, blank=True, null=True)  # Field name made lowercase.
    tanggal_mulai_pengobatan = models.DateField(blank=True, null=True)
    paduan_oat = models.CharField(max_length=500, blank=True, null=True)
    sumber_obat = models.CharField(max_length=13, blank=True, null=True)
    sebutkan = models.CharField(max_length=500, blank=True, null=True)
    sebelum_pengobatan_hasil_mikroskopis = models.CharField(max_length=15, blank=True, null=True)
    sebelum_pengobatan_hasil_tes_cepat = models.CharField(max_length=18, blank=True, null=True)
    sebelum_pengobatan_hasil_biakan = models.CharField(max_length=15, blank=True, null=True)
    noreglab_bulan_2 = models.CharField(max_length=15, blank=True, null=True)
    hasil_mikroskopis_bulan_2 = models.CharField(max_length=15, blank=True, null=True)
    noreglab_bulan_3 = models.CharField(max_length=15, blank=True, null=True)
    hasil_mikroskopis_bulan_3 = models.CharField(max_length=15, blank=True, null=True)
    noreglab_bulan_5 = models.CharField(max_length=15, blank=True, null=True)
    hasil_mikroskopis_bulan_5 = models.CharField(max_length=15, blank=True, null=True)
    akhir_pengobatan_noreglab = models.CharField(max_length=15, blank=True, null=True)
    akhir_pengobatan_hasil_mikroskopis = models.CharField(max_length=15, blank=True, null=True)
    tanggal_hasil_akhir_pengobatan = models.DateField(blank=True, null=True)
    hasil_akhir_pengobatan = models.CharField(max_length=18, blank=True, null=True)
    tanggal_dianjurkan_tes = models.DateField(blank=True, null=True)
    tanggal_tes_hiv = models.DateField(blank=True, null=True)
    hasil_tes_hiv = models.CharField(max_length=14, blank=True, null=True)
    ppk = models.CharField(max_length=5, blank=True, null=True)
    art = models.CharField(max_length=5, blank=True, null=True)
    tb_dm = models.CharField(max_length=5, blank=True, null=True)
    terapi_dm = models.CharField(max_length=12, blank=True, null=True)
    pindah_ro = models.CharField(max_length=5, blank=True, null=True)
    status_pengobatan = models.CharField(max_length=20, blank=True, null=True)
    foto_toraks = models.CharField(max_length=15, blank=True, null=True)
    toraks_tdk_dilakukan = models.CharField(max_length=112, blank=True, null=True)
    keterangan = models.CharField(max_length=100, blank=True, null=True)
    kode_icd_x = models.ForeignKey('diagnosa.Penyakit', on_delete=models.DO_NOTHING, db_column='kode_icd_x', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_tb'



class Detailjurnal(models.Model):
    no_jurnal = models.ForeignKey('Jurnal', on_delete=models.DO_NOTHING, db_column='no_jurnal', blank=True, null=True)
    kd_rek = models.ForeignKey('keuangan.Rekening', on_delete=models.DO_NOTHING, db_column='kd_rek', blank=True, null=True)
    debet = models.FloatField(blank=True, null=True)
    kredit = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detailjurnal'


class DeteksiDiniCorona(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    tanggal = models.DateField()
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    gejala_demam = models.CharField(max_length=5, blank=True, null=True)
    gejala_batuk = models.CharField(max_length=5, blank=True, null=True)
    gejala_sesak = models.CharField(max_length=5, blank=True, null=True)
    gejala_tanggal_pertama = models.DateField(blank=True, null=True)
    gejala_riwayat_sakit = models.CharField(max_length=50, blank=True, null=True)
    gejala_riwayat_periksa = models.CharField(max_length=50, blank=True, null=True)
    faktor_riwayat_perjalanan = models.CharField(max_length=5)
    faktor_asal_daerah = models.CharField(max_length=50)
    faktor_tanggal_kedatangan = models.DateField()
    faktor_paparan_kontakpositif = models.CharField(max_length=5)
    faktor_paparan_kontakpdp = models.CharField(max_length=5)
    faktor_paparan_faskespositif = models.CharField(max_length=5)
    faktor_paparan_perjalananln = models.CharField(max_length=5)
    faktor_paparan_pasarhewan = models.CharField(max_length=5)
    kesimpulan = models.CharField(max_length=15)
    tindak_lanjut = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'deteksi_dini_corona'


class HarianKurangiBulanan(models.Model):
    harian = models.IntegerField()
    bulanan = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'harian_kurangi_bulanan'



class InsidenKeselamatan(models.Model):
    kode_insiden = models.CharField(primary_key=True, max_length=5)
    nama_insiden = models.CharField(max_length=100)
    jenis_insiden = models.CharField(max_length=8)
    dampak = models.CharField(max_length=19)

    class Meta:
        managed = False
        db_table = 'insiden_keselamatan'


class InsidenKeselamatanPasien(models.Model):
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat')
    tgl_kejadian = models.DateField()
    jam_kejadian = models.TimeField()
    tgl_lapor = models.DateField()
    jam_lapor = models.TimeField()
    kode_insiden = models.ForeignKey(InsidenKeselamatan, on_delete=models.DO_NOTHING, db_column='kode_insiden')
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip')
    lokasi = models.CharField(max_length=60)
    kronologis = models.CharField(max_length=200)
    unit_terkait = models.CharField(max_length=60)
    akibat = models.CharField(max_length=150)
    tindakan_insiden = models.CharField(max_length=150)
    identifikasi_masalah = models.CharField(max_length=150)
    rtl = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'insiden_keselamatan_pasien'


class JasaLain(models.Model):
    thn = models.TextField(primary_key=True)  # This field type is a guess.
    bln = models.IntegerField()
    id = models.ForeignKey('pegawai.Pegawai', on_delete=models.DO_NOTHING, db_column='id')
    bsr_jasa = models.FloatField()
    ktg = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'jasa_lain'
        unique_together = (('thn', 'bln', 'id', 'bsr_jasa', 'ktg'),)


class Jurnal(models.Model):
    no_jurnal = models.CharField(primary_key=True, max_length=20)
    no_bukti = models.CharField(max_length=20, blank=True, null=True)
    tgl_jurnal = models.DateField(blank=True, null=True)
    jam_jurnal = models.TimeField()
    jenis = models.CharField(max_length=1, blank=True, null=True)
    keterangan = models.CharField(max_length=350, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jurnal'


class Kasift(models.Model):
    id = models.OneToOneField('pegawai.Pegawai', on_delete=models.DO_NOTHING, db_column='id', primary_key=True)
    jmlks = models.BigIntegerField()
    bsr = models.FloatField()

    class Meta:
        managed = False
        db_table = 'kasift'


class Kodesatuan(models.Model):
    kode_sat = models.CharField(primary_key=True, max_length=4)
    satuan = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kodesatuan'


class KonverSat(models.Model):
    nilai = models.FloatField(primary_key=True)
    kode_sat = models.ForeignKey(Kodesatuan, on_delete=models.DO_NOTHING, db_column='kode_sat')
    nilai_konversi = models.FloatField()
    sat_konversi = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'konver_sat'
        unique_together = (('nilai', 'kode_sat', 'nilai_konversi', 'sat_konversi'),)


class MasterBerkasDigital(models.Model):
    kode = models.CharField(primary_key=True, max_length=10)
    nama = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_berkas_digital'



class MutasiBerkas(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    status = models.CharField(max_length=14, blank=True, null=True)
    dikirim = models.DateTimeField(blank=True, null=True)
    diterima = models.DateTimeField(blank=True, null=True)
    kembali = models.DateTimeField(blank=True, null=True)
    tidakada = models.DateTimeField(blank=True, null=True)
    ranap = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'mutasi_berkas'



class Pengaduan(models.Model):
    id = models.CharField(primary_key=True, max_length=15)
    tanggal = models.DateTimeField()
    no_rkm_medis = models.ForeignKey('pasien.Pasien', on_delete=models.DO_NOTHING, db_column='no_rkm_medis')
    pesan = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'pengaduan'


class PengumumanEpasien(models.Model):
    nik = models.OneToOneField('pegawai.Pegawai', on_delete=models.DO_NOTHING, db_column='nik', primary_key=True)
    tanggal = models.DateTimeField()
    pengumuman = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pengumuman_epasien'
        unique_together = (('nik', 'tanggal'),)


class SetAkte(models.Model):
    tahun = models.TextField(primary_key=True)  # This field type is a guess.
    bulan = models.IntegerField()
    pendapatan_akte = models.FloatField()
    persen_rs = models.FloatField()
    bagian_rs = models.FloatField()
    persen_kry = models.FloatField()
    bagian_kry = models.FloatField()

    class Meta:
        managed = False
        db_table = 'set_akte'
        unique_together = (('tahun', 'bulan'),)


class SetHadir(models.Model):
    tnj = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'set_hadir'


class SetHariLibur(models.Model):
    tanggal = models.DateField(primary_key=True)
    ktg = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'set_hari_libur'


class SetInputParsial(models.Model):
    kd_pj = models.OneToOneField('asuransi.Penjab', on_delete=models.DO_NOTHING, db_column='kd_pj', primary_key=True)

    class Meta:
        managed = False
        db_table = 'set_input_parsial'


class SetInsentif(models.Model):
    tahun = models.TextField(primary_key=True)  # This field type is a guess.
    bulan = models.IntegerField()
    pendapatan = models.FloatField()
    persen = models.FloatField()
    total_insentif = models.FloatField()

    class Meta:
        managed = False
        db_table = 'set_insentif'
        unique_together = (('tahun', 'bulan'),)


class SetJamMinimal(models.Model):
    lamajam = models.IntegerField()
    hariawal = models.CharField(max_length=3)
    feeperujuk = models.FloatField()
    diagnosaakhir = models.CharField(max_length=3, blank=True, null=True)
    bayi = models.IntegerField(blank=True, null=True)
    aktifkan_hapus_data_salah = models.CharField(max_length=3, blank=True, null=True)
    kamar_inap_kasir_ralan = models.CharField(max_length=3, blank=True, null=True)
    ubah_status_kamar = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'set_jam_minimal'


class SetLokasi(models.Model):
    kd_bangsal = models.ForeignKey('bangsal.Bangsal', on_delete=models.DO_NOTHING, db_column='kd_bangsal')
    asal_stok = models.CharField(max_length=23)

    class Meta:
        managed = False
        db_table = 'set_lokasi'


class SetNoRkmMedis(models.Model):
    no_rkm_medis = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'set_no_rkm_medis'


class SetResume(models.Model):
    tahun = models.TextField(primary_key=True)  # This field type is a guess.
    bulan = models.IntegerField()
    pendapatan_resume = models.FloatField()
    persen_rs = models.FloatField()
    bagian_rs = models.FloatField()
    persen_kry = models.FloatField()
    bagian_kry = models.FloatField()

    class Meta:
        managed = False
        db_table = 'set_resume'
        unique_together = (('tahun', 'bulan'),)



class SetTahun(models.Model):
    tahun = models.TextField(primary_key=True)  # This field type is a guess.
    bulan = models.IntegerField()
    jmlhr = models.IntegerField()
    jmllbr = models.IntegerField()
    normal = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'set_tahun'
        unique_together = (('tahun', 'bulan'),)


class SetTniPolri(models.Model):
    tampilkan_tni_polri = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'set_tni_polri'


class SetTnjanak(models.Model):
    tnj = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'set_tnjanak'


class SetTnjnikah(models.Model):
    tnj = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'set_tnjnikah'



class SetUrutNoRkmMedis(models.Model):
    urutan = models.CharField(primary_key=True, max_length=8)
    tahun = models.CharField(max_length=3)
    bulan = models.CharField(max_length=3)
    posisi_tahun_bulan = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'set_urut_no_rkm_medis'


class SetValidasiCatatan(models.Model):
    tampilkan_catatan = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'set_validasi_catatan'


class SetValidasiRegistrasi(models.Model):
    wajib_closing_kasir = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'set_validasi_registrasi'


class SetWarung(models.Model):
    tahun = models.TextField(primary_key=True)  # This field type is a guess.
    bulan = models.IntegerField()
    pendapatan_warung = models.FloatField()
    persen_rs = models.FloatField()
    bagian_rs = models.FloatField()
    persen_kry = models.FloatField()
    bagian_kry = models.FloatField()

    class Meta:
        managed = False
        db_table = 'set_warung'
        unique_together = (('tahun', 'bulan'),)


class Setpenjualan(models.Model):
    ralan = models.FloatField(blank=True, null=True)
    kelas1 = models.FloatField(blank=True, null=True)
    kelas2 = models.FloatField(blank=True, null=True)
    kelas3 = models.FloatField(blank=True, null=True)
    utama = models.FloatField(blank=True, null=True)
    vip = models.FloatField(blank=True, null=True)
    vvip = models.FloatField(blank=True, null=True)
    beliluar = models.FloatField(blank=True, null=True)
    jualbebas = models.FloatField(blank=True, null=True)
    karyawan = models.FloatField(blank=True, null=True)
    kdjns = models.OneToOneField('farmasi.Jenis', on_delete=models.DO_NOTHING, db_column='kdjns', primary_key=True)

    class Meta:
        managed = False
        db_table = 'setpenjualan'


class Setpenjualanumum(models.Model):
    ralan = models.FloatField(blank=True, null=True)
    kelas1 = models.FloatField(blank=True, null=True)
    kelas2 = models.FloatField(blank=True, null=True)
    kelas3 = models.FloatField(blank=True, null=True)
    utama = models.FloatField(blank=True, null=True)
    vip = models.FloatField(blank=True, null=True)
    vvip = models.FloatField(blank=True, null=True)
    beliluar = models.FloatField(blank=True, null=True)
    jualbebas = models.FloatField(blank=True, null=True)
    karyawan = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'setpenjualanumum'


class Tambahanpotongan(models.Model):
    indexins = models.CharField(max_length=4)
    potongan = models.FloatField()

    class Meta:
        managed = False
        db_table = 'tambahanpotongan'


class Temporary(models.Model):
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
        db_table = 'temporary'


class Temporary2(models.Model):
    no = models.AutoField(primary_key=True)
    temp1 = models.CharField(max_length=100)
    temp2 = models.CharField(max_length=100)
    temp3 = models.CharField(max_length=100)
    temp4 = models.CharField(max_length=100)
    temp5 = models.CharField(max_length=100)
    temp6 = models.CharField(max_length=100)
    temp7 = models.CharField(max_length=100)
    temp8 = models.CharField(max_length=100)
    temp9 = models.CharField(max_length=100)
    temp10 = models.CharField(max_length=100)
    temp11 = models.CharField(max_length=100)
    temp12 = models.CharField(max_length=100)
    temp13 = models.CharField(max_length=100)
    temp14 = models.CharField(max_length=100)
    temp15 = models.CharField(max_length=100)
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
    temp38 = models.CharField(max_length=100)
    temp39 = models.CharField(max_length=100)
    temp40 = models.CharField(max_length=100)
    temp41 = models.CharField(max_length=100)
    temp42 = models.CharField(max_length=100)
    temp43 = models.CharField(max_length=100)
    temp44 = models.CharField(max_length=100)
    temp45 = models.CharField(max_length=100)
    temp46 = models.CharField(max_length=100)
    temp47 = models.CharField(max_length=100)
    temp48 = models.CharField(max_length=100)
    temp49 = models.CharField(max_length=100)
    temp50 = models.CharField(max_length=100)
    temp51 = models.CharField(max_length=100)
    temp52 = models.CharField(max_length=100)
    temp53 = models.CharField(max_length=100)
    temp54 = models.CharField(max_length=100)
    temp55 = models.CharField(max_length=100)
    temp56 = models.CharField(max_length=100)
    temp57 = models.CharField(max_length=100)
    temp58 = models.CharField(max_length=100)
    temp59 = models.CharField(max_length=100)
    temp60 = models.CharField(max_length=100)
    temp61 = models.CharField(max_length=100)
    temp62 = models.CharField(max_length=100)
    temp63 = models.CharField(max_length=100)
    temp64 = models.CharField(max_length=100)
    temp65 = models.CharField(max_length=100)
    temp66 = models.CharField(max_length=100)
    temp67 = models.CharField(max_length=100)
    temp68 = models.CharField(max_length=100)
    temp69 = models.CharField(max_length=100)
    temp70 = models.CharField(max_length=100)
    temp71 = models.CharField(max_length=100)
    temp72 = models.CharField(max_length=100)
    temp73 = models.CharField(max_length=100)
    temp74 = models.CharField(max_length=100)
    temp75 = models.CharField(max_length=100)
    temp76 = models.CharField(max_length=100)
    temp77 = models.CharField(max_length=100)
    temp78 = models.CharField(max_length=100)
    temp79 = models.CharField(max_length=100)
    temp80 = models.CharField(max_length=100)
    temp81 = models.CharField(max_length=100)
    temp82 = models.CharField(max_length=100)
    temp83 = models.CharField(max_length=100)
    temp84 = models.CharField(max_length=100)
    temp85 = models.CharField(max_length=100)
    temp86 = models.CharField(max_length=100)
    temp87 = models.CharField(max_length=100)
    temp88 = models.CharField(max_length=100)
    temp89 = models.CharField(max_length=100)
    temp90 = models.CharField(max_length=100)
    temp91 = models.CharField(max_length=100)
    temp92 = models.CharField(max_length=100)
    temp93 = models.CharField(max_length=100)
    temp94 = models.CharField(max_length=100)
    temp95 = models.CharField(max_length=100)
    temp96 = models.CharField(max_length=100)
    temp97 = models.CharField(max_length=100)
    temp98 = models.CharField(max_length=100)
    temp99 = models.CharField(max_length=100)
    temp100 = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'temporary2'


class TemporaryPayment(models.Model):
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
        db_table = 'temporary_payment'


class TemporaryBayarRalan(models.Model):
    no = models.AutoField(primary_key=True)
    temp1 = models.CharField(max_length=100)
    temp2 = models.CharField(max_length=200)
    temp3 = models.CharField(max_length=100)
    temp4 = models.CharField(max_length=100)
    temp5 = models.CharField(max_length=100)
    temp6 = models.CharField(max_length=100)
    temp7 = models.CharField(max_length=100)
    temp8 = models.CharField(max_length=100)
    temp9 = models.CharField(max_length=100)
    temp10 = models.CharField(max_length=100)
    temp11 = models.CharField(max_length=100)
    temp12 = models.CharField(max_length=100)
    temp13 = models.CharField(max_length=100)
    temp14 = models.CharField(max_length=100)
    temp15 = models.CharField(max_length=100)
    temp16 = models.CharField(max_length=100)
    temp17 = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'temporary_bayar_ralan'

        
class TemporaryBayarRanap(models.Model):
    no = models.AutoField(primary_key=True)
    temp1 = models.CharField(max_length=100)
    temp2 = models.CharField(max_length=200)
    temp3 = models.CharField(max_length=100)
    temp4 = models.CharField(max_length=100)
    temp5 = models.CharField(max_length=100)
    temp6 = models.CharField(max_length=100)
    temp7 = models.CharField(max_length=100)
    temp8 = models.CharField(max_length=100)
    temp9 = models.CharField(max_length=100)
    temp10 = models.CharField(max_length=100)
    temp11 = models.CharField(max_length=100)
    temp12 = models.CharField(max_length=100)
    temp13 = models.CharField(max_length=100)
    temp14 = models.CharField(max_length=100)
    temp15 = models.CharField(max_length=100)
    temp16 = models.CharField(max_length=100)
    temp17 = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'temporary_bayar_ranap'


class TemporaryBookingRegistrasi(models.Model):
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
        db_table = 'temporary_booking_registrasi'


class TemporaryGizi(models.Model):
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
        db_table = 'temporary_gizi'


class TemporaryGrafik(models.Model):
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
        db_table = 'temporary_grafik'


class TemporaryResume(models.Model):
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
        db_table = 'temporary_resume'


class TemporarySensusHarian(models.Model):
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
        db_table = 'temporary_sensus_harian'


class TemporaryTambahanPotongan(models.Model):
    no_rawat = models.CharField(primary_key=True, max_length=17)
    nama_tambahan = models.CharField(max_length=100)
    biaya = models.FloatField()
    status = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'temporary_tambahan_potongan'
        unique_together = (('no_rawat', 'nama_tambahan', 'status'),)


class TemporaryResep(models.Model):
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
        db_table = 'temporary_resep'

class TemporaryToko(models.Model):
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
        db_table = 'temporary_toko'


class Temppanggilnorawat(models.Model):
    no_rawat = models.CharField(max_length=17)

    class Meta:
        managed = False
        db_table = 'temppanggilnorawat'


class Temppanggilrm(models.Model):
    no_rkm_medis = models.CharField(primary_key=True, max_length=15)

    class Meta:
        managed = False
        db_table = 'temppanggilrm'



class Tracker(models.Model):
    nip = models.CharField(primary_key=True, max_length=20)
    tgl_login = models.DateField()
    jam_login = models.TimeField()

    class Meta:
        managed = False
        db_table = 'tracker'
        unique_together = (('nip', 'tgl_login', 'jam_login'),)


class Trackersql(models.Model):
    tanggal = models.DateTimeField()
    sqle = models.TextField()
    usere = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'trackersql'
        
        
class TemporaryLab(models.Model):
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
        db_table = 'temporary_lab'


class TemporaryPermintaanLab(models.Model):
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
        db_table = 'temporary_permintaan_lab'

