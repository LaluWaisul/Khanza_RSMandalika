from django.db import models

# Create your models here.

class Setting(models.Model):
    nama_instansi = models.CharField(primary_key=True, max_length=60)
    alamat_instansi = models.CharField(max_length=150, blank=True, null=True)
    kabupaten = models.CharField(max_length=30, blank=True, null=True)
    propinsi = models.CharField(max_length=30, blank=True, null=True)
    kontak = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    aktifkan = models.CharField(max_length=3)
    kode_ppk = models.CharField(max_length=15, blank=True, null=True)
    kode_ppkinhealth = models.CharField(max_length=15, blank=True, null=True)
    kode_ppkkemenkes = models.CharField(max_length=15, blank=True, null=True)
    wallpaper = models.TextField(blank=True, null=True)
    logo = models.TextField()

    class Meta:
        managed = False
        db_table = 'setting'


class Admin(models.Model):
    usere = models.TextField(blank=True, null=True)
    passworde = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'
        
        
class SuratBalas(models.Model):
    kd = models.CharField(primary_key=True, max_length=5)
    balas = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'surat_balas'


class SuratBebasTato(models.Model):
    no_surat = models.CharField(primary_key=True, max_length=20)
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat')
    tanggalperiksa = models.DateField()
    hasilperiksa = models.CharField(max_length=10)
    keperluan = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'surat_bebas_tato'


class SuratBebasTbc(models.Model):
    no_surat = models.CharField(primary_key=True, max_length=25)
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', blank=True, null=True)
    tanggalsurat = models.DateField(blank=True, null=True)
    kd_dokter = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter', blank=True, null=True)
    keperluan = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'surat_bebas_tbc'


class SuratButaWarna(models.Model):
    no_surat = models.CharField(primary_key=True, max_length=20)
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat')
    tanggalperiksa = models.DateField()
    hasilperiksa = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'surat_buta_warna'


class SuratCutiHamil(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    keterangan_hamil = models.CharField(max_length=25, blank=True, null=True)
    terhitung_mulai = models.DateField(blank=True, null=True)
    perkiraan_lahir = models.DateField(blank=True, null=True)
    no_surat = models.CharField(unique=True, max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'surat_cuti_hamil'


class SuratHamil(models.Model):
    no_surat = models.CharField(primary_key=True, max_length=20)
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat')
    tanggalperiksa = models.DateField()
    hasilperiksa = models.CharField(max_length=37)

    class Meta:
        managed = False
        db_table = 'surat_hamil'


class SuratIndeks(models.Model):
    kd = models.CharField(primary_key=True, max_length=5)
    indeks = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'surat_indeks'
        

class SuratKeteranganCovid(models.Model):
    no_surat = models.CharField(primary_key=True, max_length=17)
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', blank=True, null=True)
    kd_dokter = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter', blank=True, null=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    igm = models.CharField(max_length=11, blank=True, null=True)
    igg = models.CharField(max_length=11, blank=True, null=True)
    sehat = models.CharField(max_length=1, blank=True, null=True)
    tidaksehat = models.CharField(max_length=1, blank=True, null=True)
    berlakumulai = models.DateField(blank=True, null=True)
    berlakuselsai = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'surat_keterangan_covid'


class SuratKeteranganRawatInap(models.Model):
    no_surat = models.CharField(primary_key=True, max_length=17)
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', blank=True, null=True)
    tanggalawal = models.DateField(blank=True, null=True)
    tanggalakhir = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'surat_keterangan_rawat_inap'


class SuratKeteranganSehat(models.Model):
    no_surat = models.CharField(primary_key=True, max_length=17)
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', blank=True, null=True)
    tanggalsurat = models.DateField()
    berat = models.CharField(max_length=3)
    tinggi = models.CharField(max_length=3)
    tensi = models.CharField(max_length=8)
    suhu = models.CharField(max_length=4)
    butawarna = models.CharField(max_length=5)
    keperluan = models.CharField(max_length=100)
    kesimpulan = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'surat_keterangan_sehat'


class SuratKewaspadaanKesehatan(models.Model):
    no_surat = models.CharField(primary_key=True, max_length=20)
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat')
    tanggalperiksa = models.DateField()
    keluhan_saat_ini = models.CharField(max_length=50, blank=True, null=True)
    keperluan = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'surat_kewaspadaan_kesehatan'


class SuratKlasifikasi(models.Model):
    kd = models.CharField(primary_key=True, max_length=5)
    klasifikasi = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'surat_klasifikasi'


class SuratLemari(models.Model):
    kd = models.CharField(primary_key=True, max_length=5)
    lemari = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'surat_lemari'


class SuratMap(models.Model):
    kd = models.CharField(primary_key=True, max_length=5)
    map = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'surat_map'


class SuratPemesananMedis(models.Model):
    no_pemesanan = models.CharField(primary_key=True, max_length=20)
    kode_suplier = models.ForeignKey('suplier.Datasuplier', on_delete=models.DO_NOTHING, db_column='kode_suplier', blank=True, null=True)
    nip = models.ForeignKey('pegawai.Pegawai', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    tanggal = models.DateField(blank=True, null=True)
    total1 = models.FloatField()
    potongan = models.FloatField()
    total2 = models.FloatField()
    ppn = models.FloatField(blank=True, null=True)
    meterai = models.FloatField(blank=True, null=True)
    tagihan = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'surat_pemesanan_medis'


class SuratPemesananNonMedis(models.Model):
    no_pemesanan = models.CharField(primary_key=True, max_length=20)
    kode_suplier = models.ForeignKey('suplier.Ipsrssuplier', on_delete=models.DO_NOTHING, db_column='kode_suplier', blank=True, null=True)
    nip = models.ForeignKey('pegawai.Pegawai', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    tanggal = models.DateField(blank=True, null=True)
    subtotal = models.FloatField()
    potongan = models.FloatField()
    total = models.FloatField()
    ppn = models.FloatField(blank=True, null=True)
    meterai = models.FloatField(blank=True, null=True)
    tagihan = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'surat_pemesanan_non_medis'


class SuratRak(models.Model):
    kd = models.CharField(primary_key=True, max_length=5)
    rak = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'surat_rak'


class SuratRuang(models.Model):
    kd = models.CharField(primary_key=True, max_length=5)
    ruang = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'surat_ruang'


class SuratSifat(models.Model):
    kd = models.CharField(primary_key=True, max_length=5)
    sifat = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'surat_sifat'


class SuratSkbn(models.Model):
    no_surat = models.CharField(primary_key=True, max_length=25)
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', blank=True, null=True)
    tanggalsurat = models.DateField(blank=True, null=True)
    kategori = models.CharField(max_length=5, blank=True, null=True)
    kd_dokter = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter', blank=True, null=True)
    keperluan = models.CharField(max_length=50, blank=True, null=True)
    opiat = models.CharField(max_length=7, blank=True, null=True)
    ganja = models.CharField(max_length=7, blank=True, null=True)
    amphetamin = models.CharField(max_length=7, blank=True, null=True)
    methamphetamin = models.CharField(max_length=7, blank=True, null=True)
    benzodiazepin = models.CharField(max_length=7, blank=True, null=True)
    cocain = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'surat_skbn'


class SuratStatus(models.Model):
    kd = models.CharField(primary_key=True, max_length=5)
    status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'surat_status'


class SuratSubKlasifikasi(models.Model):
    kd = models.CharField(primary_key=True, max_length=10)
    kd_klasifikasi = models.ForeignKey(SuratKlasifikasi, on_delete=models.DO_NOTHING, db_column='kd_klasifikasi')
    sub_klasifikasi = models.CharField(max_length=50)
    no_bulanan = models.IntegerField(blank=True, null=True)
    no_tahunan = models.IntegerField(blank=True, null=True)
    bulan = models.IntegerField()
    tahun = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'surat_sub_klasifikasi'


class Suratsakit(models.Model):
    no_surat = models.CharField(primary_key=True, max_length=17)
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', blank=True, null=True)
    tanggalawal = models.DateField(blank=True, null=True)
    tanggalakhir = models.DateField(blank=True, null=True)
    lamasakit = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'suratsakit'


class Suratsakitpihak2(models.Model):
    no_surat = models.CharField(max_length=17)
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', blank=True, null=True)
    tanggalawal = models.DateField(blank=True, null=True)
    tanggalakhir = models.DateField(blank=True, null=True)
    lamasakit = models.CharField(max_length=20, blank=True, null=True)
    nama2 = models.CharField(max_length=50)
    tgl_lahir = models.DateField()
    umur = models.CharField(max_length=20)
    jk = models.CharField(max_length=9)
    alamat = models.CharField(max_length=200)
    hubungan = models.CharField(max_length=9)
    pekerjaan = models.CharField(max_length=15)
    instansi = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'suratsakitpihak2'


class SuratKeluar(models.Model):
    no_urut = models.CharField(primary_key=True, max_length=15)
    no_surat = models.CharField(max_length=50)
    tujuan = models.CharField(max_length=300)
    tgl_surat = models.DateField()
    perihal = models.CharField(max_length=300)
    tgl_kirim = models.DateField()
    kd_lemari = models.ForeignKey('SuratLemari', on_delete=models.DO_NOTHING, db_column='kd_lemari')
    kd_rak = models.ForeignKey('SuratRak', on_delete=models.DO_NOTHING, db_column='kd_rak')
    kd_map = models.ForeignKey('SuratMap', on_delete=models.DO_NOTHING, db_column='kd_map')
    kd_ruang = models.ForeignKey('SuratRuang', on_delete=models.DO_NOTHING, db_column='kd_ruang')
    kd_sifat = models.ForeignKey('SuratSifat', on_delete=models.DO_NOTHING, db_column='kd_sifat')
    lampiran = models.CharField(max_length=300)
    tembusan = models.CharField(max_length=300)
    tgl_deadline_balas = models.DateField()
    kd_balas = models.ForeignKey(SuratBalas, on_delete=models.DO_NOTHING, db_column='kd_balas')
    keterangan = models.CharField(max_length=300)
    kd_status = models.ForeignKey('SuratStatus', on_delete=models.DO_NOTHING, db_column='kd_status')
    kd_klasifikasi = models.ForeignKey('SuratKlasifikasi', on_delete=models.DO_NOTHING, db_column='kd_klasifikasi')
    file_url = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'surat_keluar'


class SuratKeluarDisposisi(models.Model):
    no_disposisi = models.CharField(primary_key=True, max_length=15)
    kd_indeks = models.ForeignKey(SuratIndeks, on_delete=models.DO_NOTHING, db_column='kd_indeks')
    no_urut = models.ForeignKey(SuratKeluar, on_delete=models.DO_NOTHING, db_column='no_urut')
    tgl_selesai = models.DateField()
    isi = models.CharField(max_length=300)
    diteruskan = models.CharField(max_length=300)
    tgl_kembali = models.DateField()
    kepada = models.CharField(max_length=100)
    pengesahan = models.CharField(max_length=5)
    harap = models.CharField(max_length=300)
    catatan = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'surat_keluar_disposisi'


class SuratKeluarKendali(models.Model):
    no_kendali = models.CharField(primary_key=True, max_length=15)
    kd_indeks = models.ForeignKey(SuratIndeks, on_delete=models.DO_NOTHING, db_column='kd_indeks')
    no_urut = models.ForeignKey(SuratKeluar, on_delete=models.DO_NOTHING, db_column='no_urut')
    tgl_selesai = models.DateField()
    tgl_kembali = models.DateField()
    kepada = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'surat_keluar_kendali'


class SuratKeluarSetNomor(models.Model):
    id_no_surat = models.AutoField(primary_key=True)
    jenis_surat = models.CharField(max_length=100)
    digit_1 = models.CharField(max_length=26, blank=True, null=True)
    digit_2 = models.CharField(max_length=26, blank=True, null=True)
    digit_3 = models.CharField(max_length=26, blank=True, null=True)
    digit_4 = models.CharField(max_length=26, blank=True, null=True)
    digit_5 = models.CharField(max_length=26, blank=True, null=True)
    digit_6 = models.CharField(max_length=26, blank=True, null=True)
    digit_7 = models.CharField(max_length=26, blank=True, null=True)
    digit_8 = models.CharField(max_length=26, blank=True, null=True)
    digit_9 = models.CharField(max_length=26, blank=True, null=True)
    digit_10 = models.CharField(max_length=26, blank=True, null=True)
    digit_11 = models.CharField(max_length=26, blank=True, null=True)
    digit_12 = models.CharField(max_length=26, blank=True, null=True)
    digit_13 = models.CharField(max_length=26, blank=True, null=True)
    digit_14 = models.CharField(max_length=26, blank=True, null=True)
    digit_15 = models.CharField(max_length=26, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'surat_keluar_set_nomor'


class SuratMasuk(models.Model):
    no_urut = models.CharField(primary_key=True, max_length=15)
    no_surat = models.CharField(max_length=50)
    asal = models.CharField(max_length=300)
    tujuan = models.CharField(max_length=300)
    tgl_surat = models.DateField()
    perihal = models.CharField(max_length=300)
    tgl_terima = models.DateField()
    kd_lemari = models.ForeignKey(SuratLemari, on_delete=models.DO_NOTHING, db_column='kd_lemari')
    kd_rak = models.ForeignKey('SuratRak', on_delete=models.DO_NOTHING, db_column='kd_rak')
    kd_map = models.ForeignKey(SuratMap, on_delete=models.DO_NOTHING, db_column='kd_map')
    kd_ruang = models.ForeignKey('SuratRuang', on_delete=models.DO_NOTHING, db_column='kd_ruang')
    kd_sifat = models.ForeignKey('SuratSifat', on_delete=models.DO_NOTHING, db_column='kd_sifat')
    lampiran = models.CharField(max_length=300)
    tembusan = models.CharField(max_length=300)
    tgl_deadline_balas = models.DateField()
    kd_balas = models.ForeignKey(SuratBalas, on_delete=models.DO_NOTHING, db_column='kd_balas')
    keterangan = models.CharField(max_length=300)
    kd_status = models.ForeignKey('SuratStatus', on_delete=models.DO_NOTHING, db_column='kd_status')
    kd_klasifikasi = models.ForeignKey(SuratKlasifikasi, on_delete=models.DO_NOTHING, db_column='kd_klasifikasi')
    file_url = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'surat_masuk'


class SuratMasukDisposisi(models.Model):
    no_disposisi = models.CharField(primary_key=True, max_length=15)
    kd_indeks = models.ForeignKey(SuratIndeks, on_delete=models.DO_NOTHING, db_column='kd_indeks')
    no_urut = models.ForeignKey(SuratMasuk, on_delete=models.DO_NOTHING, db_column='no_urut')
    tgl_selesai = models.DateField()
    isi = models.CharField(max_length=300)
    diteruskan = models.CharField(max_length=300)
    tgl_kembali = models.DateField()
    kepada = models.CharField(max_length=100)
    pengesahan = models.CharField(max_length=5)
    harap = models.CharField(max_length=300)
    catatan = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'surat_masuk_disposisi'


class SuratMasukKendali(models.Model):
    no_kendali = models.CharField(primary_key=True, max_length=15)
    kd_indeks = models.ForeignKey(SuratIndeks, on_delete=models.DO_NOTHING, db_column='kd_indeks')
    no_urut = models.ForeignKey(SuratMasuk, on_delete=models.DO_NOTHING, db_column='no_urut')
    tgl_selesai = models.DateField()
    tgl_kembali = models.DateField()
    kepada = models.CharField(max_length=100)
    pengesahan = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'surat_masuk_kendali'


class Setsms(models.Model):
    kode_sms = models.CharField(primary_key=True, max_length=200)
    sintax_balasan = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'setsms'


class Sms(models.Model):
    id_pesan = models.AutoField(primary_key=True)
    sms_masuk = models.CharField(max_length=255, blank=True, null=True)
    no_hp = models.CharField(max_length=15, blank=True, null=True)
    pdu_pesan = models.CharField(max_length=255, blank=True, null=True)
    encoding = models.CharField(max_length=20, blank=True, null=True)
    id_gateway = models.CharField(max_length=20, blank=True, null=True)
    tgl_sms = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms'


class User(models.Model):
    id_user = models.CharField(primary_key=True, max_length=700)
    password = models.TextField()
    penyakit = models.CharField(max_length=5)
    obat_penyakit = models.CharField(max_length=5)
    dokter = models.CharField(max_length=5)
    jadwal_praktek = models.CharField(max_length=5)
    petugas = models.CharField(max_length=5)
    pasien = models.CharField(max_length=5)
    registrasi = models.CharField(max_length=5)
    tindakan_ralan = models.CharField(max_length=5)
    kamar_inap = models.CharField(max_length=5)
    tindakan_ranap = models.CharField(max_length=5)
    operasi = models.CharField(max_length=5)
    rujukan_keluar = models.CharField(max_length=5)
    rujukan_masuk = models.CharField(max_length=5)
    beri_obat = models.CharField(max_length=5)
    resep_pulang = models.CharField(max_length=5)
    pasien_meninggal = models.CharField(max_length=5)
    diet_pasien = models.CharField(max_length=5)
    kelahiran_bayi = models.CharField(max_length=5)
    periksa_lab = models.CharField(max_length=5)
    periksa_radiologi = models.CharField(max_length=5)
    kasir_ralan = models.CharField(max_length=5)
    deposit_pasien = models.CharField(max_length=5)
    piutang_pasien = models.CharField(max_length=5)
    peminjaman_berkas = models.CharField(max_length=5)
    barcode = models.CharField(max_length=5)
    presensi_harian = models.CharField(max_length=5)
    presensi_bulanan = models.CharField(max_length=5)
    pegawai_admin = models.CharField(max_length=5)
    pegawai_user = models.CharField(max_length=5)
    suplier = models.CharField(max_length=5)
    satuan_barang = models.CharField(max_length=5)
    konversi_satuan = models.CharField(max_length=5)
    jenis_barang = models.CharField(max_length=5)
    obat = models.CharField(max_length=5)
    stok_opname_obat = models.CharField(max_length=5)
    stok_obat_pasien = models.CharField(max_length=5)
    pengadaan_obat = models.CharField(max_length=5)
    pemesanan_obat = models.CharField(max_length=5)
    penjualan_obat = models.CharField(max_length=5)
    piutang_obat = models.CharField(max_length=5)
    retur_ke_suplier = models.CharField(max_length=5)
    retur_dari_pembeli = models.CharField(max_length=5)
    retur_obat_ranap = models.CharField(max_length=5)
    retur_piutang_pasien = models.CharField(max_length=5)
    keuntungan_penjualan = models.CharField(max_length=5)
    keuntungan_beri_obat = models.CharField(max_length=5)
    sirkulasi_obat = models.CharField(max_length=5)
    ipsrs_barang = models.CharField(max_length=5)
    ipsrs_pengadaan_barang = models.CharField(max_length=5)
    ipsrs_stok_keluar = models.CharField(max_length=5)
    ipsrs_rekap_pengadaan = models.CharField(max_length=5)
    ipsrs_rekap_stok_keluar = models.CharField(max_length=5)
    ipsrs_pengeluaran_harian = models.CharField(max_length=5)
    inventaris_jenis = models.CharField(max_length=5)
    inventaris_kategori = models.CharField(max_length=5)
    inventaris_merk = models.CharField(max_length=5)
    inventaris_ruang = models.CharField(max_length=5)
    inventaris_produsen = models.CharField(max_length=5)
    inventaris_koleksi = models.CharField(max_length=5)
    inventaris_inventaris = models.CharField(max_length=5)
    inventaris_sirkulasi = models.CharField(max_length=5)
    parkir_jenis = models.CharField(max_length=5)
    parkir_in = models.CharField(max_length=5)
    parkir_out = models.CharField(max_length=5)
    parkir_rekap_harian = models.CharField(max_length=5)
    parkir_rekap_bulanan = models.CharField(max_length=5)
    informasi_kamar = models.CharField(max_length=5)
    harian_tindakan_poli = models.CharField(max_length=5)
    obat_per_poli = models.CharField(max_length=5)
    obat_per_kamar = models.CharField(max_length=5)
    obat_per_dokter_ralan = models.CharField(max_length=5)
    obat_per_dokter_ranap = models.CharField(max_length=5)
    harian_dokter = models.CharField(max_length=5)
    bulanan_dokter = models.CharField(max_length=5)
    harian_paramedis = models.CharField(max_length=5)
    bulanan_paramedis = models.CharField(max_length=5)
    pembayaran_ralan = models.CharField(max_length=5)
    pembayaran_ranap = models.CharField(max_length=5)
    rekap_pembayaran_ralan = models.CharField(max_length=5)
    rekap_pembayaran_ranap = models.CharField(max_length=5)
    tagihan_masuk = models.CharField(max_length=5)
    tambahan_biaya = models.CharField(max_length=5)
    potongan_biaya = models.CharField(max_length=5)
    resep_obat = models.CharField(max_length=5)
    resume_pasien = models.CharField(max_length=5)
    penyakit_ralan = models.CharField(max_length=5)
    penyakit_ranap = models.CharField(max_length=5)
    kamar = models.CharField(max_length=5)
    tarif_ralan = models.CharField(max_length=5)
    tarif_ranap = models.CharField(max_length=5)
    tarif_lab = models.CharField(max_length=5)
    tarif_radiologi = models.CharField(max_length=5)
    tarif_operasi = models.CharField(max_length=5)
    akun_rekening = models.CharField(max_length=5)
    rekening_tahun = models.CharField(max_length=5)
    posting_jurnal = models.CharField(max_length=5)
    buku_besar = models.CharField(max_length=5)
    cashflow = models.CharField(max_length=5)
    keuangan = models.CharField(max_length=5)
    pengeluaran = models.CharField(max_length=5)
    setup_pjlab = models.CharField(max_length=5)
    setup_otolokasi = models.CharField(max_length=5)
    setup_jam_kamin = models.CharField(max_length=5)
    setup_embalase = models.CharField(max_length=5)
    tracer_login = models.CharField(max_length=5)
    display = models.CharField(max_length=5)
    set_harga_obat = models.CharField(max_length=5)
    set_penggunaan_tarif = models.CharField(max_length=5)
    set_oto_ralan = models.CharField(max_length=5)
    biaya_harian = models.CharField(max_length=5)
    biaya_masuk_sekali = models.CharField(max_length=5)
    set_no_rm = models.CharField(max_length=5)
    billing_ralan = models.CharField(max_length=5)
    billing_ranap = models.CharField(max_length=5)
    jm_ranap_dokter = models.CharField(max_length=5)
    igd = models.CharField(max_length=5)
    barcoderalan = models.CharField(max_length=5)
    barcoderanap = models.CharField(max_length=5)
    set_harga_obat_ralan = models.CharField(max_length=5)
    set_harga_obat_ranap = models.CharField(max_length=5)
    penyakit_pd3i = models.CharField(max_length=5)
    surveilans_pd3i = models.CharField(max_length=5)
    surveilans_ralan = models.CharField(max_length=5)
    diagnosa_pasien = models.CharField(max_length=5)
    surveilans_ranap = models.CharField(max_length=5)
    pny_takmenular_ranap = models.CharField(max_length=5)
    pny_takmenular_ralan = models.CharField(max_length=5)
    kunjungan_ralan = models.CharField(max_length=5)
    rl32 = models.CharField(max_length=5)
    rl33 = models.CharField(max_length=5)
    rl37 = models.CharField(max_length=5)
    rl38 = models.CharField(max_length=5)
    harian_tindakan_dokter = models.CharField(max_length=5)
    sms = models.CharField(max_length=5)
    sidikjari = models.CharField(max_length=5)
    jam_masuk = models.CharField(max_length=5)
    jadwal_pegawai = models.CharField(max_length=5)
    parkir_barcode = models.CharField(max_length=5)
    set_nota = models.CharField(max_length=5)
    dpjp_ranap = models.CharField(max_length=5)
    mutasi_barang = models.CharField(max_length=5)
    rl34 = models.CharField(max_length=5, blank=True, null=True)
    rl36 = models.CharField(max_length=5)
    fee_visit_dokter = models.CharField(max_length=5, blank=True, null=True)
    fee_bacaan_ekg = models.CharField(max_length=5, blank=True, null=True)
    fee_rujukan_rontgen = models.CharField(max_length=5, blank=True, null=True)
    fee_rujukan_ranap = models.CharField(max_length=5, blank=True, null=True)
    fee_ralan = models.CharField(max_length=5, blank=True, null=True)
    akun_bayar = models.CharField(max_length=5, blank=True, null=True)
    bayar_pemesanan_obat = models.CharField(max_length=5, blank=True, null=True)
    obat_per_dokter_peresep = models.CharField(max_length=5, blank=True, null=True)
    ipsrs_jenis_barang = models.CharField(max_length=5, blank=True, null=True)
    pemasukan_lain = models.CharField(max_length=5, blank=True, null=True)
    pengaturan_rekening = models.CharField(max_length=5, blank=True, null=True)
    closing_kasir = models.CharField(max_length=5, blank=True, null=True)
    keterlambatan_presensi = models.CharField(max_length=5, blank=True, null=True)
    set_harga_kamar = models.CharField(max_length=5, blank=True, null=True)
    rekap_per_shift = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_nik = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_kartu = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_riwayat = models.CharField(max_length=5, blank=True, null=True)
    obat_per_cara_bayar = models.CharField(max_length=5, blank=True, null=True)
    kunjungan_ranap = models.CharField(max_length=5, blank=True, null=True)
    bayar_piutang = models.CharField(max_length=5, blank=True, null=True)
    payment_point = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_nomor_rujukan = models.CharField(max_length=5, blank=True, null=True)
    icd9 = models.CharField(max_length=5, blank=True, null=True)
    darurat_stok = models.CharField(max_length=5, blank=True, null=True)
    retensi_rm = models.CharField(max_length=5, blank=True, null=True)
    temporary_presensi = models.CharField(max_length=5, blank=True, null=True)
    jurnal_harian = models.CharField(max_length=5, blank=True, null=True)
    sirkulasi_obat2 = models.CharField(max_length=5, blank=True, null=True)
    edit_registrasi = models.CharField(max_length=5, blank=True, null=True)
    bpjs_referensi_diagnosa = models.CharField(max_length=5, blank=True, null=True)
    bpjs_referensi_poli = models.CharField(max_length=5, blank=True, null=True)
    industrifarmasi = models.CharField(max_length=5, blank=True, null=True)
    harian_js = models.CharField(max_length=5, blank=True, null=True)
    bulanan_js = models.CharField(max_length=5, blank=True, null=True)
    harian_paket_bhp = models.CharField(max_length=5, blank=True, null=True)
    bulanan_paket_bhp = models.CharField(max_length=5, blank=True, null=True)
    piutang_pasien2 = models.CharField(max_length=5, blank=True, null=True)
    bpjs_referensi_faskes = models.CharField(max_length=5, blank=True, null=True)
    bpjs_sep = models.CharField(max_length=5, blank=True, null=True)
    pengambilan_utd = models.CharField(max_length=5, blank=True, null=True)
    tarif_utd = models.CharField(max_length=5, blank=True, null=True)
    pengambilan_utd2 = models.CharField(max_length=5, blank=True, null=True)
    utd_medis_rusak = models.CharField(max_length=5, blank=True, null=True)
    pengambilan_penunjang_utd = models.CharField(max_length=5, blank=True, null=True)
    pengambilan_penunjang_utd2 = models.CharField(max_length=5, blank=True, null=True)
    utd_penunjang_rusak = models.CharField(max_length=5, blank=True, null=True)
    suplier_penunjang = models.CharField(max_length=5, blank=True, null=True)
    utd_donor = models.CharField(max_length=5, blank=True, null=True)
    bpjs_monitoring_klaim = models.CharField(max_length=5, blank=True, null=True)
    utd_cekal_darah = models.CharField(max_length=5, blank=True, null=True)
    utd_komponen_darah = models.CharField(max_length=5, blank=True, null=True)
    utd_stok_darah = models.CharField(max_length=5, blank=True, null=True)
    utd_pemisahan_darah = models.CharField(max_length=5, blank=True, null=True)
    harian_kamar = models.CharField(max_length=5, blank=True, null=True)
    rincian_piutang_pasien = models.CharField(max_length=5, blank=True, null=True)
    keuntungan_beri_obat_nonpiutang = models.CharField(max_length=5, blank=True, null=True)
    reklasifikasi_ralan = models.CharField(max_length=5, blank=True, null=True)
    reklasifikasi_ranap = models.CharField(max_length=5, blank=True, null=True)
    utd_penyerahan_darah = models.CharField(max_length=5, blank=True, null=True)
    hutang_obat = models.CharField(max_length=5, blank=True, null=True)
    riwayat_obat_alkes_bhp = models.CharField(max_length=5, blank=True, null=True)
    sensus_harian_poli = models.CharField(max_length=5, blank=True, null=True)
    rl4a = models.CharField(max_length=5, blank=True, null=True)
    aplicare_referensi_kamar = models.CharField(max_length=5, blank=True, null=True)
    aplicare_ketersediaan_kamar = models.CharField(max_length=5, blank=True, null=True)
    inacbg_klaim_baru_otomatis = models.CharField(max_length=5, blank=True, null=True)
    inacbg_klaim_baru_manual = models.CharField(max_length=5, blank=True, null=True)
    inacbg_coder_nik = models.CharField(max_length=5, blank=True, null=True)
    mutasi_berkas = models.CharField(max_length=5, blank=True, null=True)
    akun_piutang = models.CharField(max_length=5, blank=True, null=True)
    harian_kso = models.CharField(max_length=5, blank=True, null=True)
    bulanan_kso = models.CharField(max_length=5, blank=True, null=True)
    harian_menejemen = models.CharField(max_length=5, blank=True, null=True)
    bulanan_menejemen = models.CharField(max_length=5, blank=True, null=True)
    inhealth_cek_eligibilitas = models.CharField(max_length=5, blank=True, null=True)
    inhealth_referensi_jenpel_ruang_rawat = models.CharField(max_length=5, blank=True, null=True)
    inhealth_referensi_poli = models.CharField(max_length=5, blank=True, null=True)
    inhealth_referensi_faskes = models.CharField(max_length=5, blank=True, null=True)
    inhealth_sjp = models.CharField(max_length=5, blank=True, null=True)
    piutang_ralan = models.CharField(max_length=5, blank=True, null=True)
    piutang_ranap = models.CharField(max_length=5, blank=True, null=True)
    detail_piutang_penjab = models.CharField(max_length=5, blank=True, null=True)
    lama_pelayanan_ralan = models.CharField(max_length=5, blank=True, null=True)
    catatan_pasien = models.CharField(max_length=5, blank=True, null=True)
    rl4b = models.CharField(max_length=5, blank=True, null=True)
    rl4asebab = models.CharField(max_length=5, blank=True, null=True)
    rl4bsebab = models.CharField(max_length=5, blank=True, null=True)
    data_hais = models.CharField(db_column='data_HAIs', max_length=5, blank=True, null=True)  # Field name made lowercase.
    harian_hais = models.CharField(db_column='harian_HAIs', max_length=5, blank=True, null=True)  # Field name made lowercase.
    bulanan_hais = models.CharField(db_column='bulanan_HAIs', max_length=5, blank=True, null=True)  # Field name made lowercase.
    hitung_bor = models.CharField(max_length=5, blank=True, null=True)
    perusahaan_pasien = models.CharField(max_length=5, blank=True, null=True)
    resep_dokter = models.CharField(max_length=5, blank=True, null=True)
    lama_pelayanan_apotek = models.CharField(max_length=5, blank=True, null=True)
    hitung_alos = models.CharField(max_length=5, blank=True, null=True)
    detail_tindakan = models.CharField(max_length=5, blank=True, null=True)
    rujukan_poli_internal = models.CharField(max_length=5, blank=True, null=True)
    rekap_poli_anak = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_poli = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_perdokter = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_perpekerjaan = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_perpendidikan = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_pertahun = models.CharField(max_length=5, blank=True, null=True)
    berkas_digital_perawatan = models.CharField(max_length=5, blank=True, null=True)
    penyakit_menular_ranap = models.CharField(max_length=5, blank=True, null=True)
    penyakit_menular_ralan = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_perbulan = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_pertanggal = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_demografi = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_statusdaftartahun = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_statusdaftartahun2 = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_statusdaftarbulan = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_statusdaftarbulan2 = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_statusdaftartanggal = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_statusdaftartanggal2 = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_statusbataltahun = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_statusbatalbulan = models.CharField(max_length=5, blank=True, null=True)
    pcare_cek_penyakit = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_statusbataltanggal = models.CharField(max_length=5, blank=True, null=True)
    kategori_barang = models.CharField(max_length=5, blank=True, null=True)
    golongan_barang = models.CharField(max_length=5, blank=True, null=True)
    pemberian_obat_pertanggal = models.CharField(max_length=5, blank=True, null=True)
    penjualan_obat_pertanggal = models.CharField(max_length=5, blank=True, null=True)
    pcare_cek_kesadaran = models.CharField(max_length=5, blank=True, null=True)
    pembatalan_periksa_dokter = models.CharField(max_length=5, blank=True, null=True)
    pembayaran_per_unit = models.CharField(max_length=5, blank=True, null=True)
    rekap_pembayaran_per_unit = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_percarabayar = models.CharField(max_length=5, blank=True, null=True)
    ipsrs_pengadaan_pertanggal = models.CharField(max_length=5, blank=True, null=True)
    ipsrs_stokkeluar_pertanggal = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_ranaptahun = models.CharField(max_length=5, blank=True, null=True)
    pcare_cek_rujukan = models.CharField(max_length=5, blank=True, null=True)
    grafik_lab_ralantahun = models.CharField(max_length=5, blank=True, null=True)
    grafik_rad_ralantahun = models.CharField(max_length=5, blank=True, null=True)
    cek_entry_ralan = models.CharField(max_length=5, blank=True, null=True)
    inacbg_klaim_baru_manual2 = models.CharField(max_length=5, blank=True, null=True)
    permintaan_medis = models.CharField(max_length=5, blank=True, null=True)
    rekap_permintaan_medis = models.CharField(max_length=5, blank=True, null=True)
    surat_pemesanan_medis = models.CharField(max_length=5, blank=True, null=True)
    permintaan_non_medis = models.CharField(max_length=5, blank=True, null=True)
    rekap_permintaan_non_medis = models.CharField(max_length=5, blank=True, null=True)
    surat_pemesanan_non_medis = models.CharField(max_length=5, blank=True, null=True)
    grafik_per_perujuk = models.CharField(max_length=5)
    bpjs_cek_prosedur = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_kelas_rawat = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_dokter = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_spesialistik = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_ruangrawat = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_carakeluar = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_pasca_pulang = models.CharField(max_length=5, blank=True, null=True)
    detail_tindakan_okvk = models.CharField(max_length=5, blank=True, null=True)
    billing_parsial = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_nomor_rujukan_rs = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_rujukan_kartu_pcare = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_rujukan_kartu_rs = models.CharField(max_length=5, blank=True, null=True)
    akses_depo_obat = models.CharField(max_length=5, blank=True, null=True)
    bpjs_rujukan_keluar = models.CharField(max_length=5, blank=True, null=True)
    grafik_lab_ralanbulan = models.CharField(max_length=5, blank=True, null=True)
    pengeluaran_stok_apotek = models.CharField(max_length=5, blank=True, null=True)
    grafik_rad_ralanbulan = models.CharField(max_length=5, blank=True, null=True)
    detailjmdokter2 = models.CharField(max_length=5, blank=True, null=True)
    pengaduan_pasien = models.CharField(max_length=5, blank=True, null=True)
    grafik_lab_ralanhari = models.CharField(max_length=5, blank=True, null=True)
    grafik_rad_ralanhari = models.CharField(max_length=5, blank=True, null=True)
    sensus_harian_ralan = models.CharField(max_length=5, blank=True, null=True)
    metode_racik = models.CharField(max_length=5, blank=True, null=True)
    pembayaran_akun_bayar = models.CharField(max_length=5, blank=True, null=True)
    pengguna_obat_resep = models.CharField(max_length=5, blank=True, null=True)
    rekap_pemesanan = models.CharField(max_length=5, blank=True, null=True)
    master_berkas_pegawai = models.CharField(max_length=5, blank=True, null=True)
    berkas_kepegawaian = models.CharField(max_length=5, blank=True, null=True)
    riwayat_jabatan = models.CharField(max_length=5, blank=True, null=True)
    riwayat_pendidikan = models.CharField(max_length=5, blank=True, null=True)
    riwayat_naik_gaji = models.CharField(max_length=5, blank=True, null=True)
    kegiatan_ilmiah = models.CharField(max_length=5, blank=True, null=True)
    riwayat_penghargaan = models.CharField(max_length=5, blank=True, null=True)
    riwayat_penelitian = models.CharField(max_length=5, blank=True, null=True)
    penerimaan_non_medis = models.CharField(max_length=5, blank=True, null=True)
    bayar_pesan_non_medis = models.CharField(max_length=5, blank=True, null=True)
    hutang_barang_non_medis = models.CharField(max_length=5, blank=True, null=True)
    rekap_pemesanan_non_medis = models.CharField(max_length=5, blank=True, null=True)
    insiden_keselamatan = models.CharField(max_length=5, blank=True, null=True)
    insiden_keselamatan_pasien = models.CharField(max_length=5, blank=True, null=True)
    grafik_ikp_pertahun = models.CharField(max_length=5, blank=True, null=True)
    grafik_ikp_perbulan = models.CharField(max_length=5, blank=True, null=True)
    grafik_ikp_pertanggal = models.CharField(max_length=5, blank=True, null=True)
    riwayat_data_batch = models.CharField(max_length=5, blank=True, null=True)
    grafik_ikp_jenis = models.CharField(max_length=5, blank=True, null=True)
    grafik_ikp_dampak = models.CharField(max_length=5, blank=True, null=True)
    piutang_akun_piutang = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_per_agama = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_per_umur = models.CharField(max_length=5, blank=True, null=True)
    suku_bangsa = models.CharField(max_length=5, blank=True, null=True)
    bahasa_pasien = models.CharField(max_length=5, blank=True, null=True)
    golongan_tni = models.CharField(max_length=5, blank=True, null=True)
    satuan_tni = models.CharField(max_length=5, blank=True, null=True)
    jabatan_tni = models.CharField(max_length=5, blank=True, null=True)
    pangkat_tni = models.CharField(max_length=5, blank=True, null=True)
    golongan_polri = models.CharField(max_length=5, blank=True, null=True)
    satuan_polri = models.CharField(max_length=5, blank=True, null=True)
    jabatan_polri = models.CharField(max_length=5, blank=True, null=True)
    pangkat_polri = models.CharField(max_length=5, blank=True, null=True)
    cacat_fisik = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_suku = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_bahasa = models.CharField(max_length=5, blank=True, null=True)
    booking_operasi = models.CharField(max_length=5, blank=True, null=True)
    mapping_poli_bpjs = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_per_cacat = models.CharField(max_length=5, blank=True, null=True)
    barang_cssd = models.CharField(max_length=5, blank=True, null=True)
    skdp_bpjs = models.CharField(max_length=5, blank=True, null=True)
    booking_registrasi = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_propinsi = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_kabupaten = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_kecamatan = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_dokterdpjp = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_riwayat_rujukanrs = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_tanggal_rujukan = models.CharField(max_length=5, blank=True, null=True)
    permintaan_lab = models.CharField(max_length=5, blank=True, null=True)
    permintaan_radiologi = models.CharField(max_length=5, blank=True, null=True)
    surat_indeks = models.CharField(max_length=5, blank=True, null=True)
    surat_map = models.CharField(max_length=5, blank=True, null=True)
    surat_almari = models.CharField(max_length=5, blank=True, null=True)
    surat_rak = models.CharField(max_length=5, blank=True, null=True)
    surat_ruang = models.CharField(max_length=5, blank=True, null=True)
    surat_klasifikasi = models.CharField(max_length=5, blank=True, null=True)
    surat_status = models.CharField(max_length=5, blank=True, null=True)
    surat_sifat = models.CharField(max_length=5, blank=True, null=True)
    surat_balas = models.CharField(max_length=5)
    surat_masuk = models.CharField(max_length=5, blank=True, null=True)
    pcare_cek_dokter = models.CharField(max_length=5, blank=True, null=True)
    pcare_cek_poli = models.CharField(max_length=5, blank=True, null=True)
    pcare_cek_provider = models.CharField(max_length=5, blank=True, null=True)
    pcare_cek_statuspulang = models.CharField(max_length=5, blank=True, null=True)
    pcare_cek_spesialis = models.CharField(max_length=5, blank=True, null=True)
    pcare_cek_subspesialis = models.CharField(max_length=5, blank=True, null=True)
    pcare_cek_sarana = models.CharField(max_length=5, blank=True, null=True)
    pcare_cek_khusus = models.CharField(max_length=5, blank=True, null=True)
    pcare_cek_obat = models.CharField(max_length=5, blank=True, null=True)
    pcare_cek_tindakan = models.CharField(max_length=5, blank=True, null=True)
    pcare_cek_faskessubspesialis = models.CharField(max_length=5, blank=True, null=True)
    pcare_cek_faskesalihrawat = models.CharField(max_length=5, blank=True, null=True)
    pcare_cek_faskesthalasemia = models.CharField(max_length=5, blank=True, null=True)
    pcare_mapping_obat = models.CharField(max_length=5, blank=True, null=True)
    pcare_mapping_tindakan = models.CharField(max_length=5, blank=True, null=True)
    pcare_club_prolanis = models.CharField(max_length=5, blank=True, null=True)
    pcare_mapping_poli = models.CharField(max_length=5, blank=True, null=True)
    pcare_kegiatan_kelompok = models.CharField(max_length=5, blank=True, null=True)
    pcare_mapping_tindakan_ranap = models.CharField(max_length=5, blank=True, null=True)
    pcare_peserta_kegiatan_kelompok = models.CharField(max_length=5, blank=True, null=True)
    sirkulasi_obat3 = models.CharField(max_length=5, blank=True, null=True)
    bridging_pcare_daftar = models.CharField(max_length=5, blank=True, null=True)
    pcare_mapping_dokter = models.CharField(max_length=5, blank=True, null=True)
    ranap_per_ruang = models.CharField(max_length=5, blank=True, null=True)
    penyakit_ranap_cara_bayar = models.CharField(max_length=5, blank=True, null=True)
    anggota_militer_dirawat = models.CharField(max_length=5, blank=True, null=True)
    set_input_parsial = models.CharField(max_length=5, blank=True, null=True)
    lama_pelayanan_radiologi = models.CharField(max_length=5, blank=True, null=True)
    lama_pelayanan_lab = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_sep = models.CharField(max_length=5, blank=True, null=True)
    catatan_perawatan = models.CharField(max_length=5, blank=True, null=True)
    surat_keluar = models.CharField(max_length=5, blank=True, null=True)
    kegiatan_farmasi = models.CharField(max_length=5, blank=True, null=True)
    stok_opname_logistik = models.CharField(max_length=5, blank=True, null=True)
    sirkulasi_non_medis = models.CharField(max_length=5, blank=True, null=True)
    rekap_lab_pertahun = models.CharField(max_length=5, blank=True, null=True)
    perujuk_lab_pertahun = models.CharField(max_length=5, blank=True, null=True)
    rekap_radiologi_pertahun = models.CharField(max_length=5, blank=True, null=True)
    perujuk_radiologi_pertahun = models.CharField(max_length=5, blank=True, null=True)
    jumlah_porsi_diet = models.CharField(max_length=5, blank=True, null=True)
    jumlah_macam_diet = models.CharField(max_length=5, blank=True, null=True)
    payment_point2 = models.CharField(max_length=5, blank=True, null=True)
    pembayaran_akun_bayar2 = models.CharField(max_length=5, blank=True, null=True)
    hapus_nota_salah = models.CharField(max_length=5, blank=True, null=True)
    pengkajian_askep = models.CharField(max_length=5, blank=True, null=True)
    hais_perbangsal = models.CharField(max_length=5, blank=True, null=True)
    ppn_obat = models.CharField(max_length=5, blank=True, null=True)
    saldo_akun_perbulan = models.CharField(max_length=5, blank=True, null=True)
    display_apotek = models.CharField(max_length=5, blank=True, null=True)
    sisrute_referensi_faskes = models.CharField(max_length=5, blank=True, null=True)
    sisrute_referensi_alasanrujuk = models.CharField(max_length=5, blank=True, null=True)
    sisrute_referensi_diagnosa = models.CharField(max_length=5, blank=True, null=True)
    sisrute_rujukan_masuk = models.CharField(max_length=5, blank=True, null=True)
    sisrute_rujukan_keluar = models.CharField(max_length=5, blank=True, null=True)
    bpjs_cek_skdp = models.CharField(max_length=5, blank=True, null=True)
    data_batch = models.CharField(max_length=5, blank=True, null=True)
    kunjungan_permintaan_lab = models.CharField(max_length=5, blank=True, null=True)
    kunjungan_permintaan_lab2 = models.CharField(max_length=5, blank=True, null=True)
    kunjungan_permintaan_radiologi = models.CharField(max_length=5, blank=True, null=True)
    kunjungan_permintaan_radiologi2 = models.CharField(max_length=5, blank=True, null=True)
    pcare_pemberian_obat = models.CharField(max_length=5, blank=True, null=True)
    pcare_pemberian_tindakan = models.CharField(max_length=5)
    pembayaran_akun_bayar3 = models.CharField(max_length=5, blank=True, null=True)
    password_asuransi = models.CharField(max_length=5, blank=True, null=True)
    kemenkes_sitt = models.CharField(max_length=5)
    siranap_ketersediaan_kamar = models.CharField(max_length=5, blank=True, null=True)
    grafik_tb_periodelaporan = models.CharField(max_length=5, blank=True, null=True)
    grafik_tb_rujukan = models.CharField(max_length=5, blank=True, null=True)
    grafik_tb_riwayat = models.CharField(max_length=5, blank=True, null=True)
    grafik_tb_tipediagnosis = models.CharField(max_length=5, blank=True, null=True)
    grafik_tb_statushiv = models.CharField(max_length=5, blank=True, null=True)
    grafik_tb_skoringanak = models.CharField(max_length=5, blank=True, null=True)
    grafik_tb_konfirmasiskoring5 = models.CharField(max_length=5, blank=True, null=True)
    grafik_tb_konfirmasiskoring6 = models.CharField(max_length=5, blank=True, null=True)
    grafik_tb_sumberobat = models.CharField(max_length=5, blank=True, null=True)
    grafik_tb_hasilakhirpengobatan = models.CharField(max_length=5, blank=True, null=True)
    grafik_tb_hasilteshiv = models.CharField(max_length=5)
    kadaluarsa_batch = models.CharField(max_length=5)
    sisa_stok = models.CharField(max_length=5, blank=True, null=True)
    obat_per_resep = models.CharField(max_length=5, blank=True, null=True)
    pemakaian_air_pdam = models.CharField(max_length=5, blank=True, null=True)
    limbah_b3_medis = models.CharField(max_length=5, blank=True, null=True)
    grafik_air_pdam_pertanggal = models.CharField(max_length=5, blank=True, null=True)
    grafik_air_pdam_perbulan = models.CharField(max_length=5, blank=True, null=True)
    grafik_limbahb3_pertanggal = models.CharField(max_length=5, blank=True, null=True)
    grafik_limbahb3_perbulan = models.CharField(max_length=5, blank=True, null=True)
    limbah_domestik = models.CharField(max_length=5, blank=True, null=True)
    grafik_limbahdomestik_pertanggal = models.CharField(max_length=5, blank=True, null=True)
    grafik_limbahdomestik_perbulan = models.CharField(max_length=5, blank=True, null=True)
    mutu_air_limbah = models.CharField(max_length=5, blank=True, null=True)
    pest_control = models.CharField(max_length=5, blank=True, null=True)
    ruang_perpustakaan = models.CharField(max_length=5, blank=True, null=True)
    kategori_perpustakaan = models.CharField(max_length=5, blank=True, null=True)
    jenis_perpustakaan = models.CharField(max_length=5, blank=True, null=True)
    pengarang_perpustakaan = models.CharField(max_length=5, blank=True, null=True)
    penerbit_perpustakaan = models.CharField(max_length=5, blank=True, null=True)
    koleksi_perpustakaan = models.CharField(max_length=5, blank=True, null=True)
    inventaris_perpustakaan = models.CharField(max_length=5, blank=True, null=True)
    set_peminjaman_perpustakaan = models.CharField(max_length=5, blank=True, null=True)
    denda_perpustakaan = models.CharField(max_length=5, blank=True, null=True)
    anggota_perpustakaan = models.CharField(max_length=5, blank=True, null=True)
    peminjaman_perpustakaan = models.CharField(max_length=5, blank=True, null=True)
    bayar_denda_perpustakaan = models.CharField(max_length=5, blank=True, null=True)
    ebook_perpustakaan = models.CharField(max_length=5, blank=True, null=True)
    jenis_cidera_k3rs = models.CharField(max_length=5, blank=True, null=True)
    penyebab_k3rs = models.CharField(max_length=5, blank=True, null=True)
    jenis_luka_k3rs = models.CharField(max_length=5, blank=True, null=True)
    lokasi_kejadian_k3rs = models.CharField(max_length=5, blank=True, null=True)
    dampak_cidera_k3rs = models.CharField(max_length=5, blank=True, null=True)
    jenis_pekerjaan_k3rs = models.CharField(max_length=5, blank=True, null=True)
    bagian_tubuh_k3rs = models.CharField(max_length=5, blank=True, null=True)
    peristiwa_k3rs = models.CharField(max_length=5, blank=True, null=True)
    grafik_k3_pertahun = models.CharField(max_length=5, blank=True, null=True)
    grafik_k3_perbulan = models.CharField(max_length=5, blank=True, null=True)
    grafik_k3_pertanggal = models.CharField(max_length=5, blank=True, null=True)
    grafik_k3_perjeniscidera = models.CharField(max_length=5, blank=True, null=True)
    grafik_k3_perpenyebab = models.CharField(max_length=5, blank=True, null=True)
    grafik_k3_perjenisluka = models.CharField(max_length=5, blank=True, null=True)
    grafik_k3_lokasikejadian = models.CharField(max_length=5, blank=True, null=True)
    grafik_k3_dampakcidera = models.CharField(max_length=5, blank=True, null=True)
    grafik_k3_perjenispekerjaan = models.CharField(max_length=5, blank=True, null=True)
    grafik_k3_perbagiantubuh = models.CharField(max_length=5, blank=True, null=True)
    jenis_cidera_k3rstahun = models.CharField(max_length=5, blank=True, null=True)
    penyebab_k3rstahun = models.CharField(max_length=5, blank=True, null=True)
    jenis_luka_k3rstahun = models.CharField(max_length=5, blank=True, null=True)
    lokasi_kejadian_k3rstahun = models.CharField(max_length=5, blank=True, null=True)
    dampak_cidera_k3rstahun = models.CharField(max_length=5, blank=True, null=True)
    jenis_pekerjaan_k3rstahun = models.CharField(max_length=5, blank=True, null=True)
    bagian_tubuh_k3rstahun = models.CharField(max_length=5, blank=True, null=True)
    sekrining_rawat_jalan = models.CharField(max_length=5, blank=True, null=True)
    bpjs_histori_pelayanan = models.CharField(max_length=5, blank=True, null=True)
    rekap_mutasi_berkas = models.CharField(max_length=5, blank=True, null=True)
    skrining_ralan_pernapasan_pertahun = models.CharField(max_length=5, blank=True, null=True)
    pengajuan_barang_medis = models.CharField(max_length=5, blank=True, null=True)
    pengajuan_barang_nonmedis = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_ranapbulan = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_ranaptanggal = models.CharField(max_length=5, blank=True, null=True)
    grafik_kunjungan_ranap_peruang = models.CharField(max_length=5, blank=True, null=True)
    kunjungan_bangsal_pertahun = models.CharField(max_length=5, blank=True, null=True)
    grafik_jenjang_jabatanpegawai = models.CharField(max_length=5, blank=True, null=True)
    grafik_bidangpegawai = models.CharField(max_length=5, blank=True, null=True)
    grafik_departemenpegawai = models.CharField(max_length=5, blank=True, null=True)
    grafik_pendidikanpegawai = models.CharField(max_length=5, blank=True, null=True)
    grafik_sttswppegawai = models.CharField(max_length=5, blank=True, null=True)
    grafik_sttskerjapegawai = models.CharField(max_length=5, blank=True, null=True)
    grafik_sttspulangranap = models.CharField(max_length=5, blank=True, null=True)
    kip_pasien_ranap = models.CharField(max_length=5, blank=True, null=True)
    kip_pasien_ralan = models.CharField(max_length=5, blank=True, null=True)
    bpjs_mapping_dokterdpjp = models.CharField(max_length=5, blank=True, null=True)
    data_triase_igd = models.CharField(max_length=5, blank=True, null=True)
    master_triase_skala1 = models.CharField(max_length=5, blank=True, null=True)
    master_triase_skala2 = models.CharField(max_length=5, blank=True, null=True)
    master_triase_skala3 = models.CharField(max_length=5, blank=True, null=True)
    master_triase_skala4 = models.CharField(max_length=5, blank=True, null=True)
    master_triase_skala5 = models.CharField(max_length=5, blank=True, null=True)
    master_triase_pemeriksaan = models.CharField(max_length=5, blank=True, null=True)
    master_triase_macamkasus = models.CharField(max_length=5, blank=True, null=True)
    rekap_permintaan_diet = models.CharField(max_length=5, blank=True, null=True)
    daftar_pasien_ranap = models.CharField(max_length=5, blank=True, null=True)
    daftar_pasien_ranaptni = models.CharField(max_length=5, blank=True, null=True)
    pengajuan_asetinventaris = models.CharField(max_length=5, blank=True, null=True)
    item_apotek_jenis = models.CharField(max_length=5, blank=True, null=True)
    item_apotek_kategori = models.CharField(max_length=5, blank=True, null=True)
    item_apotek_golongan = models.CharField(max_length=5, blank=True, null=True)
    item_apotek_industrifarmasi = models.CharField(max_length=5, blank=True, null=True)
    number_10_obat_terbanyak_poli = models.CharField(db_column='10_obat_terbanyak_poli', max_length=5, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    grafik_pengajuan_aset_urgensi = models.CharField(max_length=5, blank=True, null=True)
    grafik_pengajuan_aset_status = models.CharField(max_length=5, blank=True, null=True)
    grafik_pengajuan_aset_departemen = models.CharField(max_length=5, blank=True, null=True)
    rekap_pengajuan_aset_departemen = models.CharField(max_length=5, blank=True, null=True)
    grafik_kelompok_jabatanpegawai = models.CharField(max_length=5, blank=True, null=True)
    grafik_resiko_kerjapegawai = models.CharField(max_length=5, blank=True, null=True)
    grafik_emergency_indexpegawai = models.CharField(max_length=5, blank=True, null=True)
    grafik_inventaris_ruang = models.CharField(max_length=5, blank=True, null=True)
    harian_hais2 = models.CharField(db_column='harian_HAIs2', max_length=5, blank=True, null=True)  # Field name made lowercase.
    grafik_inventaris_jenis = models.CharField(max_length=5, blank=True, null=True)
    data_resume_pasien = models.CharField(max_length=5, blank=True, null=True)
    perkiraan_biaya_ranap = models.CharField(max_length=5, blank=True, null=True)
    rekap_obat_poli = models.CharField(max_length=5, blank=True, null=True)
    rekap_obat_pasien = models.CharField(max_length=5, blank=True, null=True)
    permintaan_perbaikan_inventaris = models.CharField(max_length=5, blank=True, null=True)
    grafik_hais_pasienbangsal = models.CharField(db_column='grafik_HAIs_pasienbangsal', max_length=5, blank=True, null=True)  # Field name made lowercase.
    grafik_hais_pasienbulan = models.CharField(db_column='grafik_HAIs_pasienbulan', max_length=5, blank=True, null=True)  # Field name made lowercase.
    grafik_hais_laju_vap = models.CharField(db_column='grafik_HAIs_laju_vap', max_length=5, blank=True, null=True)  # Field name made lowercase.
    grafik_hais_laju_iad = models.CharField(db_column='grafik_HAIs_laju_iad', max_length=5, blank=True, null=True)  # Field name made lowercase.
    grafik_hais_laju_pleb = models.CharField(db_column='grafik_HAIs_laju_pleb', max_length=5, blank=True, null=True)  # Field name made lowercase.
    grafik_hais_laju_isk = models.CharField(db_column='grafik_HAIs_laju_isk', max_length=5, blank=True, null=True)  # Field name made lowercase.
    grafik_hais_laju_ilo = models.CharField(db_column='grafik_HAIs_laju_ilo', max_length=5, blank=True, null=True)  # Field name made lowercase.
    grafik_hais_laju_hap = models.CharField(db_column='grafik_HAIs_laju_hap', max_length=5, blank=True, null=True)  # Field name made lowercase.
    inhealth_mapping_poli = models.CharField(max_length=5, blank=True, null=True)
    inhealth_mapping_dokter = models.CharField(max_length=5, blank=True, null=True)
    inhealth_mapping_tindakan_ralan = models.CharField(max_length=5, blank=True, null=True)
    inhealth_mapping_tindakan_ranap = models.CharField(max_length=5, blank=True, null=True)
    inhealth_mapping_tindakan_radiologi = models.CharField(max_length=5, blank=True, null=True)
    inhealth_mapping_tindakan_laborat = models.CharField(max_length=5, blank=True, null=True)
    inhealth_mapping_tindakan_operasi = models.CharField(max_length=5, blank=True, null=True)
    hibah_obat_bhp = models.CharField(max_length=5, blank=True, null=True)
    asal_hibah = models.CharField(max_length=5, blank=True, null=True)
    asuhan_gizi = models.CharField(max_length=5, blank=True, null=True)
    inhealth_kirim_tagihan = models.CharField(max_length=5, blank=True, null=True)
    sirkulasi_obat4 = models.CharField(max_length=5, blank=True, null=True)
    sirkulasi_obat5 = models.CharField(max_length=5, blank=True, null=True)
    sirkulasi_non_medis2 = models.CharField(max_length=5, blank=True, null=True)
    monitoring_asuhan_gizi = models.CharField(max_length=5, blank=True, null=True)
    penerimaan_obat_perbulan = models.CharField(max_length=5, blank=True, null=True)
    rekap_kunjungan = models.CharField(max_length=5, blank=True, null=True)
    surat_sakit = models.CharField(max_length=5, blank=True, null=True)
    penilaian_awal_keperawatan_ralan = models.CharField(max_length=5, blank=True, null=True)
    permintaan_diet = models.CharField(max_length=5, blank=True, null=True)
    master_masalah_keperawatan = models.CharField(max_length=5, blank=True, null=True)
    pengajuan_cuti = models.CharField(max_length=5, blank=True, null=True)
    kedatangan_pasien = models.CharField(max_length=5, blank=True, null=True)
    utd_pendonor = models.CharField(max_length=5, blank=True, null=True)
    toko_suplier = models.CharField(max_length=5, blank=True, null=True)
    toko_jenis = models.CharField(max_length=5, blank=True, null=True)
    toko_set_harga = models.CharField(max_length=5, blank=True, null=True)
    toko_barang = models.CharField(max_length=5, blank=True, null=True)
    penagihan_piutang_pasien = models.CharField(max_length=5, blank=True, null=True)
    akun_penagihan_piutang = models.CharField(max_length=5, blank=True, null=True)
    stok_opname_toko = models.CharField(max_length=5, blank=True, null=True)
    toko_riwayat_barang = models.CharField(max_length=5, blank=True, null=True)
    toko_surat_pemesanan = models.CharField(max_length=5, blank=True, null=True)
    toko_pengajuan_barang = models.CharField(max_length=5, blank=True, null=True)
    toko_penerimaan_barang = models.CharField(max_length=5, blank=True, null=True)
    toko_pengadaan_barang = models.CharField(max_length=5, blank=True, null=True)
    toko_hutang = models.CharField(max_length=5, blank=True, null=True)
    toko_bayar_pemesanan = models.CharField(max_length=5, blank=True, null=True)
    toko_member = models.CharField(max_length=5, blank=True, null=True)
    toko_penjualan = models.CharField(max_length=5, blank=True, null=True)
    registrasi_poli_per_tanggal = models.CharField(max_length=5, blank=True, null=True)
    toko_piutang = models.CharField(max_length=5, blank=True, null=True)
    toko_retur_beli = models.CharField(max_length=5, blank=True, null=True)
    ipsrs_returbeli = models.CharField(max_length=5, blank=True, null=True)
    ipsrs_riwayat_barang = models.CharField(max_length=5, blank=True, null=True)
    pasien_corona = models.CharField(max_length=5, blank=True, null=True)
    toko_pendapatan_harian = models.CharField(max_length=5, blank=True, null=True)
    diagnosa_pasien_corona = models.CharField(max_length=5, blank=True, null=True)
    perawatan_pasien_corona = models.CharField(max_length=5, blank=True, null=True)
    penilaian_awal_keperawatan_gigi = models.CharField(max_length=5, blank=True, null=True)
    master_masalah_keperawatan_gigi = models.CharField(max_length=5, blank=True, null=True)
    toko_bayar_piutang = models.CharField(max_length=5, blank=True, null=True)
    toko_piutang_harian = models.CharField(max_length=5, blank=True, null=True)
    toko_penjualan_harian = models.CharField(max_length=5, blank=True, null=True)
    deteksi_corona = models.CharField(max_length=5, blank=True, null=True)
    penilaian_awal_keperawatan_kebidanan = models.CharField(max_length=5, blank=True, null=True)
    pengumuman_epasien = models.CharField(max_length=5, blank=True, null=True)
    surat_hamil = models.CharField(max_length=5, blank=True, null=True)
    set_tarif_online = models.CharField(max_length=5, blank=True, null=True)
    booking_periksa = models.CharField(max_length=5, blank=True, null=True)
    toko_sirkulasi = models.CharField(max_length=5, blank=True, null=True)
    toko_retur_jual = models.CharField(max_length=5, blank=True, null=True)
    toko_retur_piutang = models.CharField(max_length=5, blank=True, null=True)
    toko_sirkulasi2 = models.CharField(max_length=5, blank=True, null=True)
    toko_keuntungan_barang = models.CharField(max_length=5, blank=True, null=True)
    zis_pengeluaran_penerima_dankes = models.CharField(max_length=5, blank=True, null=True)
    zis_penghasilan_penerima_dankes = models.CharField(max_length=5, blank=True, null=True)
    zis_ukuran_rumah_penerima_dankes = models.CharField(max_length=5, blank=True, null=True)
    zis_dinding_rumah_penerima_dankes = models.CharField(max_length=5, blank=True, null=True)
    zis_lantai_rumah_penerima_dankes = models.CharField(max_length=5, blank=True, null=True)
    zis_atap_rumah_penerima_dankes = models.CharField(max_length=5, blank=True, null=True)
    zis_kepemilikan_rumah_penerima_dankes = models.CharField(max_length=5, blank=True, null=True)
    zis_kamar_mandi_penerima_dankes = models.CharField(max_length=5, blank=True, null=True)
    zis_dapur_rumah_penerima_dankes = models.CharField(max_length=5, blank=True, null=True)
    zis_kursi_rumah_penerima_dankes = models.CharField(max_length=5, blank=True, null=True)
    zis_kategori_phbs_penerima_dankes = models.CharField(max_length=5, blank=True, null=True)
    zis_elektronik_penerima_dankes = models.CharField(max_length=5, blank=True, null=True)
    zis_ternak_penerima_dankes = models.CharField(max_length=5, blank=True, null=True)
    zis_jenis_simpanan_penerima_dankes = models.CharField(max_length=5, blank=True, null=True)
    penilaian_awal_keperawatan_anak = models.CharField(max_length=5, blank=True, null=True)
    zis_kategori_asnaf_penerima_dankes = models.CharField(max_length=5, blank=True, null=True)
    master_masalah_keperawatan_anak = models.CharField(max_length=5, blank=True, null=True)
    master_imunisasi = models.CharField(max_length=5, blank=True, null=True)
    zis_patologis_penerima_dankes = models.CharField(max_length=5, blank=True, null=True)
    pcare_cek_kartu = models.CharField(max_length=5, blank=True, null=True)
    surat_bebas_narkoba = models.CharField(max_length=5, blank=True, null=True)
    surat_keterangan_covid = models.CharField(max_length=5, blank=True, null=True)
    pemakaian_air_tanah = models.CharField(max_length=5, blank=True, null=True)
    grafik_air_tanah_pertanggal = models.CharField(max_length=5, blank=True, null=True)
    grafik_air_tanah_perbulan = models.CharField(max_length=5, blank=True, null=True)
    lama_pelayanan_poli = models.CharField(max_length=5, blank=True, null=True)
    hemodialisa = models.CharField(max_length=5, blank=True, null=True)
    laporan_tahunan_irj = models.CharField(max_length=5, blank=True, null=True)
    grafik_harian_hemodialisa = models.CharField(max_length=5, blank=True, null=True)
    grafik_bulanan_hemodialisa = models.CharField(max_length=5, blank=True, null=True)
    grafik_tahunan_hemodialisa = models.CharField(max_length=5, blank=True, null=True)
    grafik_bulanan_meninggal = models.CharField(max_length=5, blank=True, null=True)
    perbaikan_inventaris = models.CharField(max_length=5, blank=True, null=True)
    surat_cuti_hamil = models.CharField(max_length=5, blank=True, null=True)
    permintaan_stok_obat_pasien = models.CharField(max_length=5, blank=True, null=True)
    pemeliharaan_inventaris = models.CharField(max_length=5, blank=True, null=True)
    klasifikasi_pasien_ranap = models.CharField(max_length=5, blank=True, null=True)
    bulanan_klasifikasi_pasien_ranap = models.CharField(max_length=5, blank=True, null=True)
    harian_klasifikasi_pasien_ranap = models.CharField(max_length=5, blank=True, null=True)
    klasifikasi_pasien_perbangsal = models.CharField(max_length=5, blank=True, null=True)
    soap_perawatan = models.CharField(max_length=5, blank=True, null=True)
    klaim_rawat_jalan = models.CharField(max_length=5, blank=True, null=True)
    skrining_gizi = models.CharField(max_length=5, blank=True, null=True)
    lama_penyiapan_rm = models.CharField(max_length=5, blank=True, null=True)
    dosis_radiologi = models.CharField(max_length=5, blank=True, null=True)
    demografi_umur_kunjungan = models.CharField(max_length=5, blank=True, null=True)
    jam_diet_pasien = models.CharField(max_length=5, blank=True, null=True)
    rvu_bpjs = models.CharField(max_length=5, blank=True, null=True)
    verifikasi_penerimaan_farmasi = models.CharField(max_length=5, blank=True, null=True)
    verifikasi_penerimaan_logistik = models.CharField(max_length=5, blank=True, null=True)
    pemeriksaan_lab_pa = models.CharField(max_length=5, blank=True, null=True)
    ringkasan_pengajuan_obat = models.CharField(max_length=5, blank=True, null=True)
    ringkasan_pemesanan_obat = models.CharField(max_length=5, blank=True, null=True)
    ringkasan_pengadaan_obat = models.CharField(max_length=5, blank=True, null=True)
    ringkasan_penerimaan_obat = models.CharField(max_length=5, blank=True, null=True)
    ringkasan_hibah_obat = models.CharField(max_length=5, blank=True, null=True)
    ringkasan_penjualan_obat = models.CharField(max_length=5, blank=True, null=True)
    ringkasan_beri_obat = models.CharField(max_length=5, blank=True, null=True)
    ringkasan_piutang_obat = models.CharField(max_length=5, blank=True, null=True)
    ringkasan_stok_keluar_obat = models.CharField(max_length=5, blank=True, null=True)
    ringkasan_retur_suplier_obat = models.CharField(max_length=5, blank=True, null=True)
    ringkasan_retur_pembeli_obat = models.CharField(max_length=5, blank=True, null=True)
    penilaian_awal_keperawatan_ranapkebidanan = models.CharField(max_length=5, blank=True, null=True)
    ringkasan_pengajuan_nonmedis = models.CharField(max_length=5, blank=True, null=True)
    ringkasan_pemesanan_nonmedis = models.CharField(max_length=5, blank=True, null=True)
    ringkasan_pengadaan_nonmedis = models.CharField(max_length=5, blank=True, null=True)
    ringkasan_penerimaan_nonmedis = models.CharField(max_length=5, blank=True, null=True)
    ringkasan_stokkeluar_nonmedis = models.CharField(max_length=5, blank=True, null=True)
    ringkasan_returbeli_nonmedis = models.CharField(max_length=5, blank=True, null=True)
    omset_penerimaan = models.CharField(max_length=5, blank=True, null=True)
    validasi_penagihan_piutang = models.CharField(max_length=5, blank=True, null=True)
    permintaan_ranap = models.CharField(max_length=5, blank=True, null=True)
    bpjs_diagnosa_prb = models.CharField(max_length=5, blank=True, null=True)
    bpjs_obat_prb = models.CharField(max_length=5, blank=True, null=True)
    bpjs_surat_kontrol = models.CharField(max_length=5, blank=True, null=True)
    penggunaan_bhp_ok = models.CharField(max_length=5, blank=True, null=True)
    surat_keterangan_rawat_inap = models.CharField(max_length=5, blank=True, null=True)
    surat_keterangan_sehat = models.CharField(max_length=5, blank=True, null=True)
    pendapatan_per_carabayar = models.CharField(max_length=5, blank=True, null=True)
    akun_host_to_host_bank_jateng = models.CharField(max_length=5, blank=True, null=True)
    pembayaran_bank_jateng = models.CharField(max_length=5, blank=True, null=True)
    bpjs_surat_pri = models.CharField(max_length=5, blank=True, null=True)
    ringkasan_tindakan = models.CharField(max_length=5, blank=True, null=True)
    lama_pelayanan_pasien = models.CharField(max_length=5, blank=True, null=True)
    surat_sakit_pihak_2 = models.CharField(max_length=5, blank=True, null=True)
    tagihan_hutang_obat = models.CharField(max_length=5, blank=True, null=True)
    referensi_mobilejkn_bpjs = models.CharField(max_length=5, blank=True, null=True)
    batal_pendaftaran_mobilejkn_bpjs = models.CharField(max_length=5, blank=True, null=True)
    lama_operasi = models.CharField(max_length=5, blank=True, null=True)
    grafik_inventaris_kategori = models.CharField(max_length=5, blank=True, null=True)
    grafik_inventaris_merk = models.CharField(max_length=5, blank=True, null=True)
    grafik_inventaris_produsen = models.CharField(max_length=5, blank=True, null=True)
    pengembalian_deposit_pasien = models.CharField(max_length=5, blank=True, null=True)
    validasi_tagihan_hutang_obat = models.CharField(max_length=5, blank=True, null=True)
    piutang_obat_belum_lunas = models.CharField(max_length=5, blank=True, null=True)
    integrasi_briapi = models.CharField(max_length=5, blank=True, null=True)
    pengadaan_aset_inventaris = models.CharField(max_length=5, blank=True, null=True)
    akun_aset_inventaris = models.CharField(max_length=5, blank=True, null=True)
    suplier_inventaris = models.CharField(max_length=5, blank=True, null=True)
    penerimaan_aset_inventaris = models.CharField(max_length=5, blank=True, null=True)
    bayar_pemesanan_iventaris = models.CharField(max_length=5, blank=True, null=True)
    hutang_aset_inventaris = models.CharField(max_length=5, blank=True, null=True)
    hibah_aset_inventaris = models.CharField(max_length=5, blank=True, null=True)
    titip_faktur_non_medis = models.CharField(max_length=5, blank=True, null=True)
    validasi_tagihan_non_medis = models.CharField(max_length=5, blank=True, null=True)
    titip_faktur_aset = models.CharField(max_length=5, blank=True, null=True)
    validasi_tagihan_aset = models.CharField(max_length=5, blank=True, null=True)
    hibah_non_medis = models.CharField(max_length=5, blank=True, null=True)
    pcare_alasan_tacc = models.CharField(max_length=5, blank=True, null=True)
    resep_luar = models.CharField(max_length=5, blank=True, null=True)
    surat_bebas_tbc = models.CharField(max_length=5, blank=True, null=True)
    surat_buta_warna = models.CharField(max_length=5, blank=True, null=True)
    surat_bebas_tato = models.CharField(max_length=5, blank=True, null=True)
    surat_kewaspadaan_kesehatan = models.CharField(max_length=5, blank=True, null=True)
    grafik_porsidiet_pertanggal = models.CharField(max_length=5, blank=True, null=True)
    grafik_porsidiet_perbulan = models.CharField(max_length=5, blank=True, null=True)
    grafik_porsidiet_pertahun = models.CharField(max_length=5, blank=True, null=True)
    grafik_porsidiet_perbangsal = models.CharField(max_length=5, blank=True, null=True)
    penilaian_awal_medis_ralan = models.CharField(max_length=5, blank=True, null=True)
    master_masalah_keperawatan_mata = models.CharField(max_length=5, blank=True, null=True)
    penilaian_awal_keperawatan_mata = models.CharField(max_length=5, blank=True, null=True)
    penilaian_awal_medis_ranap = models.CharField(max_length=5, blank=True, null=True)
    penilaian_awal_medis_ranap_kebidanan = models.CharField(max_length=5, blank=True, null=True)
    penilaian_awal_medis_ralan_kebidanan = models.CharField(max_length=5, blank=True, null=True)
    penilaian_awal_medis_igd = models.CharField(max_length=5, blank=True, null=True)
    penilaian_awal_medis_ralan_anak = models.CharField(max_length=5, blank=True, null=True)
    bpjs_referensi_poli_hfis = models.CharField(max_length=5, blank=True, null=True)
    bpjs_referensi_dokter_hfis = models.CharField(max_length=5, blank=True, null=True)
    bpjs_referensi_jadwal_hfis = models.CharField(max_length=5, blank=True, null=True)
    penilaian_fisioterapi = models.CharField(max_length=5, blank=True, null=True)
    bpjs_program_prb = models.CharField(max_length=5, blank=True, null=True)
    bpjs_suplesi_jasaraharja = models.CharField(max_length=5, blank=True, null=True)
    bpjs_data_induk_kecelakaan = models.CharField(max_length=5, blank=True, null=True)
    bpjs_sep_internal = models.CharField(max_length=5, blank=True, null=True)
    bpjs_klaim_jasa_raharja = models.CharField(max_length=5, blank=True, null=True)
    bpjs_daftar_finger_print = models.CharField(max_length=5, blank=True, null=True)
    bpjs_rujukan_khusus = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class Runtext(models.Model):
    teks = models.TextField()
    aktifkan = models.CharField(max_length=3)
    gambar = models.TextField()

    class Meta:
        managed = False
        db_table = 'runtext'


class Runtextapotek(models.Model):
    teks = models.TextField()
    aktifkan = models.CharField(max_length=3)
    gambar = models.TextField()

    class Meta:
        managed = False
        db_table = 'runtextapotek'

