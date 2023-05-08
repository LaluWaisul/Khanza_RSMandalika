## NAMA TABEL FARMASI
# 1. Data Barang
# 2. Data Batch
# 3. Stock Obat Pasien
# 4. Permintaan Obat


from django.db import models

# Create your models here.

class MasterAturanPakai(models.Model):
    aturan = models.CharField(primary_key=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'master_aturan_pakai'


class PengajuanBarangMedis(models.Model):
    no_pengajuan = models.CharField(primary_key=True, max_length=20)
    nip = models.ForeignKey('pegawai.Pegawai', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    tanggal = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=16, blank=True, null=True)
    keterangan = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pengajuan_barang_medis'


class Jenis(models.Model):
    kdjns = models.CharField(primary_key=True, max_length=4)
    nama = models.CharField(max_length=30)
    keterangan = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'jenis'
        
        
class KategoriBarang(models.Model):
    kode = models.CharField(primary_key=True, max_length=4)
    nama = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kategori_barang'
        

class GolonganBarang(models.Model):
    kode = models.CharField(primary_key=True, max_length=4)
    nama = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'golongan_barang'
     

class MetodeRacik(models.Model):
    kd_racik = models.CharField(primary_key=True, max_length=3)
    nm_racik = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'metode_racik'


class Pembelian(models.Model):
    no_faktur = models.CharField(primary_key=True, max_length=20)
    kode_suplier = models.ForeignKey('suplier.Datasuplier', on_delete=models.DO_NOTHING, db_column='kode_suplier', blank=True, null=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    tgl_beli = models.DateField(blank=True, null=True)
    total1 = models.FloatField()
    potongan = models.FloatField()
    total2 = models.FloatField()
    ppn = models.FloatField()
    tagihan = models.FloatField()
    kd_bangsal = models.ForeignKey('bangsal.Bangsal', on_delete=models.DO_NOTHING, db_column='kd_bangsal')
    kd_rek = models.ForeignKey('keuangan.Rekening', on_delete=models.DO_NOTHING, db_column='kd_rek', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pembelian'


class Penjualan(models.Model):
    nota_jual = models.CharField(primary_key=True, max_length=20)
    tgl_jual = models.DateField(blank=True, null=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    no_rkm_medis = models.ForeignKey('pasien.Pasien', on_delete=models.DO_NOTHING, db_column='no_rkm_medis', blank=True, null=True)
    nm_pasien = models.CharField(max_length=50, blank=True, null=True)
    keterangan = models.CharField(max_length=40, blank=True, null=True)
    jns_jual = models.CharField(max_length=11, blank=True, null=True)
    ongkir = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=13, blank=True, null=True)
    kd_bangsal = models.ForeignKey('bangsal.Bangsal', on_delete=models.DO_NOTHING, db_column='kd_bangsal')
    kd_rek = models.ForeignKey('keuangan.Rekening', on_delete=models.DO_NOTHING, db_column='kd_rek', blank=True, null=True)
    nama_bayar = models.ForeignKey('keuangan.AkunBayar', on_delete=models.DO_NOTHING, db_column='nama_bayar', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'penjualan'


class Databarang(models.Model):
    kode_brng = models.CharField(primary_key=True, max_length=15)
    nama_brng = models.CharField(max_length=80, blank=True, null=True)
    kode_satbesar = models.ForeignKey('data.Kodesatuan', on_delete=models.DO_NOTHING, db_column='kode_satbesar', related_name='kode_satbesar_data_barang')
    kode_sat = models.ForeignKey('data.Kodesatuan', on_delete=models.DO_NOTHING, db_column='kode_sat', blank=True, null=True, related_name='kode_sat_data_barang')
    letak_barang = models.CharField(max_length=50, blank=True, null=True)
    dasar = models.FloatField()
    h_beli = models.FloatField(blank=True, null=True)
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
    stokminimal = models.FloatField(blank=True, null=True)
    kdjns = models.ForeignKey('Jenis', on_delete=models.DO_NOTHING, db_column='kdjns', blank=True, null=True)
    isi = models.FloatField()
    kapasitas = models.FloatField()
    expire = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=1)
    kode_industri = models.ForeignKey('suplier.Industrifarmasi', on_delete=models.DO_NOTHING, db_column='kode_industri', blank=True, null=True)
    kode_kategori = models.ForeignKey('KategoriBarang', on_delete=models.DO_NOTHING, db_column='kode_kategori', blank=True, null=True)
    kode_golongan = models.ForeignKey('GolonganBarang', on_delete=models.DO_NOTHING, db_column='kode_golongan', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'databarang'
        
        
class AturanPakai(models.Model):
    tgl_perawatan = models.DateField(primary_key=True)
    jam = models.TimeField()
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat')
    kode_brng = models.ForeignKey('Databarang', on_delete=models.DO_NOTHING, db_column='kode_brng')
    aturan = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aturan_pakai'
        unique_together = (('tgl_perawatan', 'jam', 'no_rawat', 'kode_brng'),)


class DataBatch(models.Model):
    no_batch = models.CharField(primary_key=True, max_length=20)
    kode_brng = models.ForeignKey('Databarang', on_delete=models.DO_NOTHING, db_column='kode_brng')
    tgl_beli = models.DateField()
    tgl_kadaluarsa = models.DateField()
    asal = models.CharField(max_length=10)
    no_faktur = models.CharField(max_length=20)
    dasar = models.FloatField()
    h_beli = models.FloatField(blank=True, null=True)
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
    jumlahbeli = models.FloatField()
    sisa = models.FloatField()

    class Meta:
        managed = False
        db_table = 'data_batch'
        unique_together = (('no_batch', 'kode_brng', 'no_faktur'),)


class StokObatPasien(models.Model):
    tanggal = models.DateField(primary_key=True)
    jam = models.TimeField()
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat')
    kode_brng = models.ForeignKey(Databarang, on_delete=models.DO_NOTHING, db_column='kode_brng')
    jumlah = models.FloatField()
    kd_bangsal = models.ForeignKey('bangsal.Bangsal', on_delete=models.DO_NOTHING, db_column='kd_bangsal')
    no_batch = models.CharField(max_length=20)
    no_faktur = models.CharField(max_length=20)
    aturan_pakai = models.CharField(max_length=150)
    pg = models.CharField(max_length=5)
    sg = models.CharField(max_length=5)
    sr = models.CharField(max_length=5)
    ml = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'stok_obat_pasien'
        unique_together = (('tanggal', 'jam', 'no_rawat', 'kode_brng', 'no_batch', 'no_faktur'),)


class PermintaanObat(models.Model):
    tanggal = models.DateField(primary_key=True)
    jam = models.TimeField()
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat')
    kode_brng = models.ForeignKey(Databarang, on_delete=models.DO_NOTHING, db_column='kode_brng')

    class Meta:
        managed = False
        db_table = 'permintaan_obat'
        unique_together = (('tanggal', 'jam', 'no_rawat', 'kode_brng'),)


class ResepObat(models.Model):
    no_resep = models.CharField(primary_key=True, max_length=14)
    tgl_perawatan = models.DateField(blank=True, null=True)
    jam = models.TimeField()
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat')
    kd_dokter = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter')
    tgl_peresepan = models.DateField(blank=True, null=True)
    jam_peresepan = models.TimeField(blank=True, null=True)
    status = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resep_obat'
        unique_together = (('tgl_perawatan', 'jam', 'no_rawat'),)
        
        
class ObatRacikan(models.Model):
    tgl_perawatan = models.DateField(primary_key=True)
    jam = models.TimeField()
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat')
    no_racik = models.CharField(max_length=2)
    nama_racik = models.CharField(max_length=100)
    kd_racik = models.ForeignKey(MetodeRacik, on_delete=models.DO_NOTHING, db_column='kd_racik')
    jml_dr = models.IntegerField()
    aturan_pakai = models.CharField(max_length=150)
    keterangan = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'obat_racikan'
        unique_together = (('tgl_perawatan', 'jam', 'no_rawat', 'no_racik'),)


class ObatRacikanJual(models.Model):
    nota_jual = models.OneToOneField('Penjualan', on_delete=models.DO_NOTHING, db_column='nota_jual', primary_key=True)
    no_racik = models.CharField(max_length=2)
    nama_racik = models.CharField(max_length=100)
    kd_racik = models.ForeignKey(MetodeRacik, on_delete=models.DO_NOTHING, db_column='kd_racik')
    jml_dr = models.IntegerField()
    aturan_pakai = models.CharField(max_length=150)
    keterangan = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'obat_racikan_jual'
        unique_together = (('nota_jual', 'no_racik'),)


class DetailObatRacikan(models.Model):
    tgl_perawatan = models.DateField(primary_key=True)
    jam = models.TimeField()
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat')
    no_racik = models.CharField(max_length=2)
    kode_brng = models.ForeignKey(Databarang, on_delete=models.DO_NOTHING, db_column='kode_brng')

    class Meta:
        managed = False
        db_table = 'detail_obat_racikan'
        unique_together = (('tgl_perawatan', 'jam', 'no_rawat', 'no_racik', 'kode_brng'),)


class DetailObatRacikanJual(models.Model):
    nota_jual = models.OneToOneField('Penjualan', on_delete=models.DO_NOTHING, db_column='nota_jual', primary_key=True)
    no_racik = models.CharField(max_length=2)
    kode_brng = models.ForeignKey(Databarang, on_delete=models.DO_NOTHING, db_column='kode_brng')

    class Meta:
        managed = False
        db_table = 'detail_obat_racikan_jual'
        unique_together = (('nota_jual', 'no_racik', 'kode_brng'),)


class DetailPemberianObat(models.Model):
    tgl_perawatan = models.DateField(primary_key=True)
    jam = models.TimeField()
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat')
    kode_brng = models.ForeignKey(Databarang, on_delete=models.DO_NOTHING, db_column='kode_brng')
    h_beli = models.FloatField(blank=True, null=True)
    biaya_obat = models.FloatField(blank=True, null=True)
    jml = models.FloatField()
    embalase = models.FloatField(blank=True, null=True)
    tuslah = models.FloatField(blank=True, null=True)
    total = models.FloatField()
    status = models.CharField(max_length=5, blank=True, null=True)
    kd_bangsal = models.ForeignKey('bangsal.Bangsal', on_delete=models.DO_NOTHING, db_column='kd_bangsal', blank=True, null=True)
    no_batch = models.CharField(max_length=20)
    no_faktur = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'detail_pemberian_obat'
        unique_together = (('tgl_perawatan', 'jam', 'no_rawat', 'kode_brng', 'no_batch', 'no_faktur'),)


class PengeluaranObatBhp(models.Model):
    no_keluar = models.CharField(primary_key=True, max_length=15)
    tanggal = models.DateField()
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip')
    keterangan = models.CharField(max_length=200)
    kd_bangsal = models.ForeignKey('bangsal.Bangsal', on_delete=models.DO_NOTHING, db_column='kd_bangsal', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pengeluaran_obat_bhp'


class DetailPengeluaranObatBhp(models.Model):
    no_keluar = models.ForeignKey('PengeluaranObatBhp', on_delete=models.DO_NOTHING, db_column='no_keluar')
    kode_brng = models.ForeignKey(Databarang, on_delete=models.DO_NOTHING, db_column='kode_brng')
    kode_sat = models.ForeignKey('data.Kodesatuan', on_delete=models.DO_NOTHING, db_column='kode_sat')
    no_batch = models.CharField(max_length=20, blank=True, null=True)
    jumlah = models.FloatField()
    harga_beli = models.FloatField()
    total = models.FloatField()
    no_faktur = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'detail_pengeluaran_obat_bhp'


class PermintaanStokObatPasien(models.Model):
    no_permintaan = models.CharField(primary_key=True, max_length=14)
    tgl_permintaan = models.DateField(blank=True, null=True)
    jam = models.TimeField()
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat')
    kd_dokter = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter')
    status = models.CharField(max_length=5)
    tgl_validasi = models.DateField()
    jam_validasi = models.TimeField()

    class Meta:
        managed = False
        db_table = 'permintaan_stok_obat_pasien'
        unique_together = (('tgl_permintaan', 'jam', 'no_rawat'),)


class DetailPermintaanStokObatPasien(models.Model):
    no_permintaan = models.ForeignKey('PermintaanStokObatPasien', on_delete=models.DO_NOTHING, db_column='no_permintaan', blank=True, null=True)
    kode_brng = models.ForeignKey(Databarang, on_delete=models.DO_NOTHING, db_column='kode_brng', blank=True, null=True)
    jml = models.FloatField(blank=True, null=True)
    aturan_pakai = models.CharField(max_length=150, blank=True, null=True)
    pg = models.CharField(max_length=5)
    sg = models.CharField(max_length=5)
    sr = models.CharField(max_length=5)
    ml = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'detail_permintaan_stok_obat_pasien'


class HibahObatBhp(models.Model):
    no_hibah = models.CharField(primary_key=True, max_length=20)
    kode_pemberi = models.ForeignKey('suplier.Pemberihibah', on_delete=models.DO_NOTHING, db_column='kode_pemberi', blank=True, null=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    tgl_hibah = models.DateField(blank=True, null=True)
    totalhibah = models.FloatField()
    totalnilai = models.FloatField()
    kd_bangsal = models.ForeignKey('bangsal.Bangsal', on_delete=models.DO_NOTHING, db_column='kd_bangsal')

    class Meta:
        managed = False
        db_table = 'hibah_obat_bhp'


class DetailhibahObatBhp(models.Model):
    no_hibah = models.OneToOneField('HibahObatBhp', on_delete=models.DO_NOTHING, db_column='no_hibah', primary_key=True)
    kode_brng = models.ForeignKey(Databarang, on_delete=models.DO_NOTHING, db_column='kode_brng')
    kode_sat = models.ForeignKey('data.Kodesatuan', on_delete=models.DO_NOTHING, db_column='kode_sat', blank=True, null=True)
    jumlah = models.FloatField(blank=True, null=True)
    h_hibah = models.FloatField(blank=True, null=True)
    subtotalhibah = models.FloatField(blank=True, null=True)
    h_diakui = models.FloatField()
    subtotaldiakui = models.FloatField()
    no_batch = models.CharField(max_length=20)
    jumlah2 = models.FloatField(blank=True, null=True)
    kadaluarsa = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detailhibah_obat_bhp'
        unique_together = (('no_hibah', 'kode_brng', 'no_batch'),)


class ObatbhpOk(models.Model):
    kd_obat = models.CharField(primary_key=True, max_length=15)
    nm_obat = models.CharField(max_length=50)
    kode_sat = models.ForeignKey('data.Kodesatuan', on_delete=models.DO_NOTHING, db_column='kode_sat')
    hargasatuan = models.FloatField()

    class Meta:
        managed = False
        db_table = 'obatbhp_ok'
        

class BeriObatOperasi(models.Model):
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat')
    tanggal = models.DateTimeField()
    kd_obat = models.ForeignKey(ObatbhpOk, on_delete=models.DO_NOTHING, db_column='kd_obat')
    hargasatuan = models.FloatField()
    jumlah = models.FloatField()

    class Meta:
        managed = False
        db_table = 'beri_obat_operasi'


class MapingObatPcare(models.Model):
    kode_brng = models.OneToOneField(Databarang, on_delete=models.DO_NOTHING, db_column='kode_brng', primary_key=True)
    kode_brng_pcare = models.CharField(max_length=15)
    nama_brng_pcare = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maping_obat_pcare'


class PcareObatDiberikan(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    nokunjungan = models.CharField(db_column='noKunjungan', max_length=40)  # Field name made lowercase.
    kdobatsk = models.CharField(db_column='kdObatSK', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tgl_perawatan = models.DateField()
    jam = models.TimeField()
    kode_brng = models.ForeignKey(MapingObatPcare, on_delete=models.DO_NOTHING, db_column='kode_brng')
    no_batch = models.CharField(max_length=20)
    no_faktur = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'pcare_obat_diberikan'
        unique_together = (('no_rawat', 'nokunjungan', 'tgl_perawatan', 'jam', 'kode_brng', 'no_batch', 'no_faktur'),)



class ObatPenyakit(models.Model):
    kd_penyakit = models.OneToOneField('diagnosa.Penyakit', on_delete=models.DO_NOTHING, db_column='kd_penyakit', primary_key=True)
    kode_brng = models.ForeignKey(Databarang, on_delete=models.DO_NOTHING, db_column='kode_brng')
    referensi = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'obat_penyakit'
        unique_together = (('kd_penyakit', 'kode_brng'),)


class ResepDokter(models.Model):
    no_resep = models.ForeignKey('ResepObat', on_delete=models.DO_NOTHING, db_column='no_resep', blank=True, null=True)
    kode_brng = models.ForeignKey(Databarang, on_delete=models.DO_NOTHING, db_column='kode_brng', blank=True, null=True)
    jml = models.FloatField(blank=True, null=True)
    aturan_pakai = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resep_dokter'


class ResepDokterRacikan(models.Model):
    no_resep = models.OneToOneField('ResepObat', on_delete=models.DO_NOTHING, db_column='no_resep', primary_key=True)
    no_racik = models.CharField(max_length=2)
    nama_racik = models.CharField(max_length=100)
    kd_racik = models.ForeignKey(MetodeRacik, on_delete=models.DO_NOTHING, db_column='kd_racik')
    jml_dr = models.IntegerField()
    aturan_pakai = models.CharField(max_length=150)
    keterangan = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'resep_dokter_racikan'
        unique_together = (('no_resep', 'no_racik'),)


class ResepDokterRacikanDetail(models.Model):
    no_resep = models.OneToOneField('ResepObat', on_delete=models.DO_NOTHING, db_column='no_resep', primary_key=True)
    no_racik = models.CharField(max_length=2)
    kode_brng = models.ForeignKey(Databarang, on_delete=models.DO_NOTHING, db_column='kode_brng')
    p1 = models.FloatField(blank=True, null=True)
    p2 = models.FloatField(blank=True, null=True)
    kandungan = models.CharField(max_length=10, blank=True, null=True)
    jml = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resep_dokter_racikan_detail'
        unique_together = (('no_resep', 'no_racik', 'kode_brng'),)


class ResepLuar(models.Model):
    no_resep = models.CharField(primary_key=True, max_length=14)
    tgl_perawatan = models.DateField(blank=True, null=True)
    jam = models.TimeField()
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat')
    kd_dokter = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter')
    tgl_peresepan = models.DateField(blank=True, null=True)
    jam_peresepan = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resep_luar'
        unique_together = (('tgl_perawatan', 'jam', 'no_rawat'),)


class ResepLuarObat(models.Model):
    no_resep = models.OneToOneField(ResepLuar, on_delete=models.DO_NOTHING, db_column='no_resep', primary_key=True)
    kode_brng = models.ForeignKey(Databarang, on_delete=models.DO_NOTHING, db_column='kode_brng')
    jml = models.FloatField(blank=True, null=True)
    aturan_pakai = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resep_luar_obat'
        unique_together = (('no_resep', 'kode_brng'),)


class ResepLuarRacikan(models.Model):
    no_resep = models.OneToOneField(ResepLuar, on_delete=models.DO_NOTHING, db_column='no_resep', primary_key=True)
    no_racik = models.CharField(max_length=2)
    nama_racik = models.CharField(max_length=100)
    kd_racik = models.ForeignKey(MetodeRacik, on_delete=models.DO_NOTHING, db_column='kd_racik')
    jml_dr = models.IntegerField()
    aturan_pakai = models.CharField(max_length=150)
    keterangan = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'resep_luar_racikan'
        unique_together = (('no_resep', 'no_racik'),)


class ResepLuarRacikanDetail(models.Model):
    no_resep = models.OneToOneField(ResepLuar, on_delete=models.DO_NOTHING, db_column='no_resep', primary_key=True)
    no_racik = models.CharField(max_length=2)
    kode_brng = models.ForeignKey(Databarang, on_delete=models.DO_NOTHING, db_column='kode_brng')
    p1 = models.FloatField(blank=True, null=True)
    p2 = models.FloatField(blank=True, null=True)
    kandungan = models.CharField(max_length=10, blank=True, null=True)
    jml = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resep_luar_racikan_detail'
        unique_together = (('no_resep', 'no_racik', 'kode_brng'),)


class ResepPulang(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    kode_brng = models.ForeignKey(Databarang, on_delete=models.DO_NOTHING, db_column='kode_brng')
    jml_barang = models.FloatField()
    harga = models.FloatField()
    total = models.FloatField()
    dosis = models.CharField(max_length=20)
    tanggal = models.DateField()
    jam = models.TimeField()
    kd_bangsal = models.ForeignKey('bangsal.Bangsal', on_delete=models.DO_NOTHING, db_column='kd_bangsal')
    no_batch = models.CharField(max_length=20)
    no_faktur = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'resep_pulang'
        unique_together = (('no_rawat', 'kode_brng', 'tanggal', 'jam', 'no_batch', 'no_faktur'),)


class SetDepoRalan(models.Model):
    kd_poli = models.OneToOneField('bangsal.Poliklinik', on_delete=models.DO_NOTHING, db_column='kd_poli', primary_key=True)
    kd_bangsal = models.ForeignKey('bangsal.Bangsal', on_delete=models.DO_NOTHING, db_column='kd_bangsal')

    class Meta:
        managed = False
        db_table = 'set_depo_ralan'
        unique_together = (('kd_poli', 'kd_bangsal'),)


class SetDepoRanap(models.Model):
    kd_bangsal = models.OneToOneField('bangsal.Bangsal', on_delete=models.DO_NOTHING, db_column='kd_bangsal', primary_key=True, related_name='kd_bangsal_set_depo_ranap')
    kd_depo = models.ForeignKey('bangsal.Bangsal', on_delete=models.DO_NOTHING, db_column='kd_depo', related_name='kd_depo_set_depo_ranap')

    class Meta:
        managed = False
        db_table = 'set_depo_ranap'
        unique_together = (('kd_bangsal', 'kd_depo'),)


class SetEmbalase(models.Model):
    embalase_per_obat = models.FloatField()
    tuslah_per_obat = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'set_embalase'
        

class SetTuslah(models.Model):
    tahun = models.TextField(primary_key=True)  # This field type is a guess.
    bulan = models.IntegerField()
    pendapatan_tuslah = models.FloatField()
    persen_rs = models.FloatField()
    bagian_rs = models.FloatField()
    persen_kry = models.FloatField()
    bagian_kry = models.FloatField()

    class Meta:
        managed = False
        db_table = 'set_tuslah'
        unique_together = (('tahun', 'bulan'),)


class SetHargaObat(models.Model):
    setharga = models.CharField(max_length=10)
    hargadasar = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'set_harga_obat'


class SetHargaObatRalan(models.Model):
    kd_pj = models.OneToOneField('asuransi.Penjab', on_delete=models.DO_NOTHING, db_column='kd_pj', primary_key=True)
    hargajual = models.FloatField()

    class Meta:
        managed = False
        db_table = 'set_harga_obat_ralan'


class SetHargaObatRanap(models.Model):
    kd_pj = models.OneToOneField('asuransi.Penjab', on_delete=models.DO_NOTHING, db_column='kd_pj', primary_key=True)
    kelas = models.CharField(max_length=11)
    hargajual = models.FloatField()

    class Meta:
        managed = False
        db_table = 'set_harga_obat_ranap'
        unique_together = (('kd_pj', 'kelas'),)


class TagihanObatLangsung(models.Model):
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat')
    besar_tagihan = models.FloatField()

    class Meta:
        managed = False
        db_table = 'tagihan_obat_langsung'


class Mutasibarang(models.Model):
    kode_brng = models.OneToOneField(Databarang, on_delete=models.DO_NOTHING, db_column='kode_brng', primary_key=True)
    jml = models.FloatField()
    harga = models.FloatField()
    kd_bangsaldari = models.ForeignKey('bangsal.Bangsal', on_delete=models.DO_NOTHING, db_column='kd_bangsaldari', related_name='kd_bangsaldari_mutasi_barang')
    kd_bangsalke = models.ForeignKey('bangsal.Bangsal', on_delete=models.DO_NOTHING, db_column='kd_bangsalke', related_name='kd_bangsalke_mutasi_barang')
    tanggal = models.DateTimeField()
    keterangan = models.CharField(max_length=60)
    no_batch = models.CharField(max_length=20)
    no_faktur = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'mutasibarang'
        unique_together = (('kode_brng', 'kd_bangsaldari', 'kd_bangsalke', 'tanggal', 'no_batch', 'no_faktur'),)


class Opname(models.Model):
    kode_brng = models.OneToOneField(Databarang, on_delete=models.DO_NOTHING, db_column='kode_brng', primary_key=True)
    h_beli = models.FloatField(blank=True, null=True)
    tanggal = models.DateField()
    stok = models.FloatField()
    real = models.FloatField()
    selisih = models.FloatField()
    nomihilang = models.FloatField()
    lebih = models.FloatField()
    nomilebih = models.FloatField()
    keterangan = models.CharField(max_length=60)
    kd_bangsal = models.ForeignKey('bangsal.Bangsal', on_delete=models.DO_NOTHING, db_column='kd_bangsal')
    no_batch = models.CharField(max_length=20)
    no_faktur = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'opname'
        unique_together = (('kode_brng', 'tanggal', 'kd_bangsal', 'no_batch', 'no_faktur'),)


class RiwayatBarangMedis(models.Model):
    kode_brng = models.ForeignKey(Databarang, on_delete=models.DO_NOTHING, db_column='kode_brng', blank=True, null=True)
    stok_awal = models.FloatField(blank=True, null=True)
    masuk = models.FloatField(blank=True, null=True)
    keluar = models.FloatField(blank=True, null=True)
    stok_akhir = models.FloatField()
    posisi = models.CharField(max_length=17, blank=True, null=True)
    tanggal = models.DateField(blank=True, null=True)
    jam = models.TimeField(blank=True, null=True)
    petugas = models.CharField(max_length=20, blank=True, null=True)
    kd_bangsal = models.ForeignKey('bangsal.Bangsal', on_delete=models.DO_NOTHING, db_column='kd_bangsal', blank=True, null=True)
    status = models.CharField(max_length=6, blank=True, null=True)
    no_batch = models.CharField(max_length=20)
    no_faktur = models.CharField(max_length=20)
    keterangan = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'riwayat_barang_medis'


class Gudangbarang(models.Model):
    kode_brng = models.OneToOneField(Databarang, on_delete=models.DO_NOTHING, db_column='kode_brng', primary_key=True)
    kd_bangsal = models.ForeignKey('bangsal.Bangsal', on_delete=models.DO_NOTHING, db_column='kd_bangsal')
    stok = models.FloatField()
    no_batch = models.CharField(max_length=20)
    no_faktur = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'gudangbarang'
        unique_together = (('kode_brng', 'kd_bangsal', 'no_batch', 'no_faktur'),)


class PermintaanMedis(models.Model):
    no_permintaan = models.CharField(primary_key=True, max_length=20)
    kd_bangsal = models.ForeignKey('bangsal.Bangsal', on_delete=models.DO_NOTHING, db_column='kd_bangsal', blank=True, null=True, related_name='kd_bangsal_permintaan_medis')
    nip = models.ForeignKey('pegawai.Pegawai', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    tanggal = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=15, blank=True, null=True)
    kd_bangsaltujuan = models.ForeignKey('bangsal.Bangsal', on_delete=models.DO_NOTHING, db_column='kd_bangsaltujuan', related_name='kd_bangsaltujuan_permintaan_medis')

    class Meta:
        managed = False
        db_table = 'permintaan_medis'
 
        
class DetailPermintaanMedis(models.Model):
    no_permintaan = models.ForeignKey('PermintaanMedis', on_delete=models.DO_NOTHING, db_column='no_permintaan', blank=True, null=True)
    kode_brng = models.ForeignKey(Databarang, on_delete=models.DO_NOTHING, db_column='kode_brng', blank=True, null=True)
    kode_sat = models.ForeignKey('data.Kodesatuan', on_delete=models.DO_NOTHING, db_column='kode_sat', blank=True, null=True)
    jumlah = models.FloatField(blank=True, null=True)
    keterangan = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detail_permintaan_medis'


class Tampbeli1(models.Model):
    kode_brng = models.OneToOneField(Databarang, on_delete=models.DO_NOTHING, db_column='kode_brng', primary_key=True)
    nama_brng = models.CharField(max_length=100, blank=True, null=True)
    satuan = models.CharField(max_length=10, blank=True, null=True)
    satuan_stok = models.CharField(max_length=10, blank=True, null=True)
    h_beli = models.FloatField(blank=True, null=True)
    jumlah = models.FloatField(blank=True, null=True)
    jumlah_stok = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tampbeli1'


class Tampjual1(models.Model):
    kode_brng = models.OneToOneField(Databarang, on_delete=models.DO_NOTHING, db_column='kode_brng', primary_key=True)
    nama_brng = models.CharField(max_length=100, blank=True, null=True)
    satuan = models.CharField(max_length=10, blank=True, null=True)
    h_jual = models.FloatField(blank=True, null=True)
    h_beli = models.FloatField()
    jumlah = models.FloatField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    dis = models.FloatField(blank=True, null=True)
    bsr_dis = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tampjual1'


class Tampjurnal(models.Model):
    kd_rek = models.CharField(primary_key=True, max_length=15)
    nm_rek = models.CharField(max_length=100, blank=True, null=True)
    debet = models.FloatField(blank=True, null=True)
    kredit = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tampjurnal'


class Tampjurnal2(models.Model):
    kd_rek = models.CharField(primary_key=True, max_length=15)
    nm_rek = models.CharField(max_length=100, blank=True, null=True)
    debet = models.FloatField(blank=True, null=True)
    kredit = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tampjurnal2'


class Pemesanan(models.Model):
    no_faktur = models.CharField(primary_key=True, max_length=20)
    no_order = models.CharField(max_length=20)
    kode_suplier = models.ForeignKey('suplier.Datasuplier', on_delete=models.DO_NOTHING, db_column='kode_suplier', blank=True, null=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    tgl_pesan = models.DateField(blank=True, null=True)
    tgl_faktur = models.DateField(blank=True, null=True)
    tgl_tempo = models.DateField(blank=True, null=True)
    total1 = models.FloatField()
    potongan = models.FloatField()
    total2 = models.FloatField()
    ppn = models.FloatField()
    meterai = models.FloatField(blank=True, null=True)
    tagihan = models.FloatField()
    kd_bangsal = models.ForeignKey('bangsal.Bangsal', on_delete=models.DO_NOTHING, db_column='kd_bangsal')
    status = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pemesanan'


class Detailpesan(models.Model):
    no_faktur = models.ForeignKey('Pemesanan', on_delete=models.DO_NOTHING, db_column='no_faktur')
    kode_brng = models.ForeignKey(Databarang, on_delete=models.DO_NOTHING, db_column='kode_brng')
    kode_sat = models.ForeignKey('data.Kodesatuan', on_delete=models.DO_NOTHING, db_column='kode_sat', blank=True, null=True)
    jumlah = models.FloatField(blank=True, null=True)
    h_pesan = models.FloatField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    dis = models.FloatField()
    besardis = models.FloatField()
    total = models.FloatField()
    no_batch = models.CharField(max_length=20)
    jumlah2 = models.FloatField(blank=True, null=True)
    kadaluarsa = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detailpesan'


class Tamppiutang(models.Model):
    kode_brng = models.OneToOneField(Databarang, on_delete=models.DO_NOTHING, db_column='kode_brng', primary_key=True)
    nama_brng = models.CharField(max_length=80, blank=True, null=True)
    satuan = models.CharField(max_length=10, blank=True, null=True)
    h_jual = models.FloatField(blank=True, null=True)
    h_beli = models.FloatField(blank=True, null=True)
    jumlah = models.FloatField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    dis = models.FloatField(blank=True, null=True)
    bsr_dis = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    no_batch = models.CharField(max_length=20)
    petugas = models.CharField(max_length=20)
    no_faktur = models.CharField(max_length=20)
    aturan_pakai = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'tamppiutang'
        unique_together = (('kode_brng', 'no_batch', 'no_faktur'),)


class Tampreturbeli(models.Model):
    no_faktur = models.CharField(primary_key=True, max_length=20)
    kode_brng = models.ForeignKey(Databarang, on_delete=models.DO_NOTHING, db_column='kode_brng')
    nama_brng = models.CharField(max_length=100, blank=True, null=True)
    satuan = models.CharField(max_length=10, blank=True, null=True)
    h_beli = models.FloatField(blank=True, null=True)
    jml_beli = models.FloatField(blank=True, null=True)
    h_retur = models.FloatField(blank=True, null=True)
    jml_retur = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    no_batch = models.CharField(max_length=20)
    jml_retur2 = models.FloatField(blank=True, null=True)
    kadaluarsa = models.CharField(max_length=14)
    petugas = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tampreturbeli'
        unique_together = (('no_faktur', 'kode_brng'),)


class Tampreturjual(models.Model):
    nota_jual = models.CharField(primary_key=True, max_length=20)
    kode_brng = models.ForeignKey(Databarang, on_delete=models.DO_NOTHING, db_column='kode_brng')
    nama_brng = models.CharField(max_length=100, blank=True, null=True)
    jml_jual = models.FloatField(blank=True, null=True)
    h_jual = models.FloatField(blank=True, null=True)
    jml_retur = models.FloatField(blank=True, null=True)
    h_retur = models.FloatField(blank=True, null=True)
    satuan = models.CharField(max_length=10, blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    no_batch = models.CharField(max_length=20)
    petugas = models.CharField(max_length=20)
    no_faktur = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tampreturjual'
        unique_together = (('nota_jual', 'kode_brng', 'no_batch', 'no_faktur'),)


class Tampreturpiutang(models.Model):
    nota_piutang = models.CharField(primary_key=True, max_length=20)
    kode_brng = models.ForeignKey(Databarang, on_delete=models.DO_NOTHING, db_column='kode_brng')
    nama_brng = models.CharField(max_length=100, blank=True, null=True)
    jml_piutang = models.FloatField(blank=True, null=True)
    h_piutang = models.FloatField(blank=True, null=True)
    jml_retur = models.FloatField(blank=True, null=True)
    h_retur = models.FloatField(blank=True, null=True)
    satuan = models.CharField(max_length=10, blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    no_batch = models.CharField(max_length=20)
    petugas = models.CharField(max_length=20, blank=True, null=True)
    no_faktur = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'tampreturpiutang'
        unique_together = (('nota_piutang', 'kode_brng', 'no_batch'),)
        

class TitipFaktur(models.Model):
    no_tagihan = models.CharField(primary_key=True, max_length=20)
    tanggal = models.DateField(blank=True, null=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    keterangan = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'titip_faktur'


class DetailPengajuanBarangMedis(models.Model):
    no_pengajuan = models.ForeignKey('PengajuanBarangMedis', on_delete=models.DO_NOTHING, db_column='no_pengajuan')
    kode_brng = models.ForeignKey(Databarang, on_delete=models.DO_NOTHING, db_column='kode_brng')
    kode_sat = models.ForeignKey('data.Kodesatuan', on_delete=models.DO_NOTHING, db_column='kode_sat', blank=True, null=True)
    jumlah = models.FloatField(blank=True, null=True)
    h_pengajuan = models.FloatField(blank=True, null=True)
    total = models.FloatField()
    jumlah2 = models.FloatField()

    class Meta:
        managed = False
        db_table = 'detail_pengajuan_barang_medis'


class DetailSuratPemesananMedis(models.Model):
    no_pemesanan = models.ForeignKey('administer.SuratPemesananMedis', on_delete=models.DO_NOTHING, db_column='no_pemesanan')
    kode_brng = models.ForeignKey(Databarang, on_delete=models.DO_NOTHING, db_column='kode_brng')
    kode_sat = models.ForeignKey('data.Kodesatuan', on_delete=models.DO_NOTHING, db_column='kode_sat', blank=True, null=True)
    jumlah = models.FloatField(blank=True, null=True)
    h_pesan = models.FloatField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    dis = models.FloatField()
    besardis = models.FloatField()
    total = models.FloatField()
    jumlah2 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detail_surat_pemesanan_medis'


class DetailTitipFaktur(models.Model):
    no_tagihan = models.OneToOneField('TitipFaktur', on_delete=models.DO_NOTHING, db_column='no_tagihan', primary_key=True)
    no_faktur = models.ForeignKey(Pemesanan, on_delete=models.DO_NOTHING, db_column='no_faktur')

    class Meta:
        managed = False
        db_table = 'detail_titip_faktur'
        unique_together = (('no_tagihan', 'no_faktur'),)


class Detailbeli(models.Model):
    no_faktur = models.ForeignKey('Pembelian', on_delete=models.DO_NOTHING, db_column='no_faktur')
    kode_brng = models.ForeignKey(Databarang, on_delete=models.DO_NOTHING, db_column='kode_brng')
    kode_sat = models.ForeignKey('data.Kodesatuan', on_delete=models.DO_NOTHING, db_column='kode_sat', blank=True, null=True)
    jumlah = models.FloatField(blank=True, null=True)
    h_beli = models.FloatField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    dis = models.FloatField()
    besardis = models.FloatField()
    total = models.FloatField()
    no_batch = models.CharField(max_length=20)
    jumlah2 = models.FloatField(blank=True, null=True)
    kadaluarsa = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detailbeli'


class Detailjual(models.Model):
    nota_jual = models.ForeignKey('Penjualan', on_delete=models.DO_NOTHING, db_column='nota_jual')
    kode_brng = models.ForeignKey(Databarang, on_delete=models.DO_NOTHING, db_column='kode_brng')
    kode_sat = models.ForeignKey('data.Kodesatuan', on_delete=models.DO_NOTHING, db_column='kode_sat', blank=True, null=True)
    h_jual = models.FloatField(blank=True, null=True)
    h_beli = models.FloatField(blank=True, null=True)
    jumlah = models.FloatField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    dis = models.FloatField(blank=True, null=True)
    bsr_dis = models.FloatField(blank=True, null=True)
    tambahan = models.FloatField(blank=True, null=True)
    embalase = models.FloatField()
    tuslah = models.FloatField()
    aturan_pakai = models.CharField(max_length=150)
    total = models.FloatField(blank=True, null=True)
    no_batch = models.CharField(max_length=20)
    no_faktur = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'detailjual'


class PembagianTuslah(models.Model):
    id = models.OneToOneField('pegawai.Pegawai', on_delete=models.DO_NOTHING, db_column='id', primary_key=True)
    persen = models.FloatField()

    class Meta:
        managed = False
        db_table = 'pembagian_tuslah'


class Setpenjualanperbarang(models.Model):
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
    kode_brng = models.OneToOneField(Databarang, on_delete=models.DO_NOTHING, db_column='kode_brng', primary_key=True)

    class Meta:
        managed = False
        db_table = 'setpenjualanperbarang'
        
        
class Returbeli(models.Model):
    no_retur_beli = models.CharField(primary_key=True, max_length=20)
    tgl_retur = models.DateField(blank=True, null=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    kode_suplier = models.ForeignKey('suplier.Datasuplier', on_delete=models.DO_NOTHING, db_column='kode_suplier')
    kd_bangsal = models.ForeignKey('bangsal.Bangsal', on_delete=models.DO_NOTHING, db_column='kd_bangsal')

    class Meta:
        managed = False
        db_table = 'returbeli'

        
class Detreturbeli(models.Model):
    no_retur_beli = models.ForeignKey('Returbeli', on_delete=models.DO_NOTHING, db_column='no_retur_beli')
    no_faktur = models.CharField(max_length=20)
    kode_brng = models.ForeignKey(Databarang, on_delete=models.DO_NOTHING, db_column='kode_brng')
    kode_sat = models.ForeignKey('data.Kodesatuan', on_delete=models.DO_NOTHING, db_column='kode_sat', blank=True, null=True)
    h_beli = models.FloatField(blank=True, null=True)
    jml_beli = models.FloatField(blank=True, null=True)
    h_retur = models.FloatField(blank=True, null=True)
    jml_retur = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    no_batch = models.CharField(max_length=20)
    jml_retur2 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detreturbeli'
        

class Returjual(models.Model):
    no_retur_jual = models.CharField(primary_key=True, max_length=20)
    tgl_retur = models.DateField(blank=True, null=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    no_rkm_medis = models.ForeignKey('pasien.Pasien', on_delete=models.DO_NOTHING, db_column='no_rkm_medis')
    kd_bangsal = models.ForeignKey('bangsal.Bangsal', on_delete=models.DO_NOTHING, db_column='kd_bangsal')

    class Meta:
        managed = False
        db_table = 'returjual'


class Detreturjual(models.Model):
    no_retur_jual = models.ForeignKey('Returjual', on_delete=models.DO_NOTHING, db_column='no_retur_jual')
    nota_jual = models.CharField(max_length=20)
    kode_brng = models.ForeignKey(Databarang, on_delete=models.DO_NOTHING, db_column='kode_brng')
    kode_sat = models.ForeignKey('data.Kodesatuan', on_delete=models.DO_NOTHING, db_column='kode_sat', blank=True, null=True)
    jml_jual = models.FloatField(blank=True, null=True)
    h_jual = models.FloatField(blank=True, null=True)
    jml_retur = models.FloatField(blank=True, null=True)
    h_retur = models.FloatField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    no_batch = models.CharField(max_length=20)
    no_faktur = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'detreturjual'


class Returpasien(models.Model):
    tanggal = models.DateField(primary_key=True)
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat')
    kode_brng = models.ForeignKey(Databarang, on_delete=models.DO_NOTHING, db_column='kode_brng')
    jml = models.FloatField()
    no_batch = models.CharField(max_length=20)
    no_faktur = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'returpasien'
        unique_together = (('tanggal', 'no_rawat', 'kode_brng', 'no_batch', 'no_faktur'),)


class Antriapotek(models.Model):
    loket = models.IntegerField()
    antrian = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'antriapotek'


class BuktiPemesanan(models.Model):
    no_faktur = models.OneToOneField('Pemesanan', on_delete=models.DO_NOTHING, db_column='no_faktur', primary_key=True)
    photo = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bukti_pemesanan'

