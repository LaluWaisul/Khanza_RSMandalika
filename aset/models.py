from django.db import models

# Create your models here.

class Ipsrsbarang(models.Model):
    kode_brng = models.CharField(primary_key=True, max_length=15)
    nama_brng = models.CharField(max_length=80)
    kode_sat = models.ForeignKey('data.Kodesatuan', on_delete=models.DO_NOTHING, db_column='kode_sat')
    jenis = models.ForeignKey('Ipsrsjenisbarang', on_delete=models.DO_NOTHING, db_column='jenis', blank=True, null=True)
    stok = models.FloatField()
    harga = models.FloatField()
    status = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'ipsrsbarang'


class IpsrsHibah(models.Model):
    no_hibah = models.CharField(primary_key=True, max_length=20)
    kode_pemberi = models.ForeignKey('suplier.Pemberihibah', on_delete=models.DO_NOTHING, db_column='kode_pemberi', blank=True, null=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    tgl_hibah = models.DateField(blank=True, null=True)
    totalhibah = models.FloatField()
    keterangan = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'ipsrs_hibah'


class IpsrsDetailHibah(models.Model):
    no_hibah = models.OneToOneField('IpsrsHibah', on_delete=models.DO_NOTHING, db_column='no_hibah', primary_key=True)
    kode_brng = models.ForeignKey('Ipsrsbarang', on_delete=models.DO_NOTHING, db_column='kode_brng')
    kode_sat = models.ForeignKey('data.Kodesatuan', on_delete=models.DO_NOTHING, db_column='kode_sat')
    jumlah = models.FloatField(blank=True, null=True)
    h_hibah = models.FloatField(blank=True, null=True)
    subtotalhibah = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ipsrs_detail_hibah'
        unique_together = (('no_hibah', 'kode_brng'),)


class IpsrsDetailReturbeli(models.Model):
    no_retur_beli = models.ForeignKey('Ipsrsreturbeli', on_delete=models.DO_NOTHING, db_column='no_retur_beli')
    no_faktur = models.CharField(max_length=20)
    kode_brng = models.ForeignKey('Ipsrsbarang', on_delete=models.DO_NOTHING, db_column='kode_brng')
    kode_sat = models.ForeignKey('data.Kodesatuan', on_delete=models.DO_NOTHING, db_column='kode_sat', blank=True, null=True)
    h_beli = models.FloatField(blank=True, null=True)
    h_retur = models.FloatField(blank=True, null=True)
    jml_retur = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ipsrs_detail_returbeli'


class IpsrsDetailTitipFaktur(models.Model):
    no_tagihan = models.OneToOneField('IpsrsTitipFaktur', on_delete=models.DO_NOTHING, db_column='no_tagihan', primary_key=True)
    no_faktur = models.ForeignKey('Ipsrspemesanan', on_delete=models.DO_NOTHING, db_column='no_faktur')

    class Meta:
        managed = False
        db_table = 'ipsrs_detail_titip_faktur'
        unique_together = (('no_tagihan', 'no_faktur'),)
        
        
class BuktiPemesananLogistik(models.Model):
    no_faktur = models.OneToOneField('Ipsrspemesanan', on_delete=models.DO_NOTHING, db_column='no_faktur', primary_key=True)
    photo = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bukti_pemesanan_logistik'


class IpsrsRiwayatBarang(models.Model):
    kode_brng = models.ForeignKey('Ipsrsbarang', on_delete=models.DO_NOTHING, db_column='kode_brng', blank=True, null=True)
    stok_awal = models.FloatField(blank=True, null=True)
    masuk = models.FloatField(blank=True, null=True)
    keluar = models.FloatField(blank=True, null=True)
    stok_akhir = models.FloatField()
    posisi = models.CharField(max_length=15, blank=True, null=True)
    tanggal = models.DateField(blank=True, null=True)
    jam = models.TimeField(blank=True, null=True)
    petugas = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ipsrs_riwayat_barang'


class IpsrsTitipFaktur(models.Model):
    no_tagihan = models.CharField(primary_key=True, max_length=20)
    tanggal = models.DateField(blank=True, null=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    keterangan = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'ipsrs_titip_faktur'


class Ipsrsdetailbeli(models.Model):
    no_faktur = models.ForeignKey('Ipsrspembelian', on_delete=models.DO_NOTHING, db_column='no_faktur')
    kode_brng = models.ForeignKey(Ipsrsbarang, on_delete=models.DO_NOTHING, db_column='kode_brng')
    kode_sat = models.ForeignKey('data.Kodesatuan', on_delete=models.DO_NOTHING, db_column='kode_sat')
    jumlah = models.FloatField()
    harga = models.FloatField()
    subtotal = models.FloatField()
    dis = models.FloatField()
    besardis = models.FloatField()
    total = models.FloatField()

    class Meta:
        managed = False
        db_table = 'ipsrsdetailbeli'


class Ipsrsdetailpengeluaran(models.Model):
    no_keluar = models.ForeignKey('Ipsrspengeluaran', on_delete=models.DO_NOTHING, db_column='no_keluar')
    kode_brng = models.ForeignKey(Ipsrsbarang, on_delete=models.DO_NOTHING, db_column='kode_brng')
    kode_sat = models.ForeignKey('data.Kodesatuan', on_delete=models.DO_NOTHING, db_column='kode_sat')
    jumlah = models.FloatField()
    harga = models.FloatField()
    total = models.FloatField()

    class Meta:
        managed = False
        db_table = 'ipsrsdetailpengeluaran'


class Ipsrsdetailpesan(models.Model):
    no_faktur = models.ForeignKey('Ipsrspemesanan', on_delete=models.DO_NOTHING, db_column='no_faktur')
    kode_brng = models.ForeignKey(Ipsrsbarang, on_delete=models.DO_NOTHING, db_column='kode_brng')
    kode_sat = models.ForeignKey('data.Kodesatuan', on_delete=models.DO_NOTHING, db_column='kode_sat')
    jumlah = models.FloatField()
    harga = models.FloatField()
    subtotal = models.FloatField()
    dis = models.FloatField()
    besardis = models.FloatField()
    total = models.FloatField()

    class Meta:
        managed = False
        db_table = 'ipsrsdetailpesan'


class Ipsrsjenisbarang(models.Model):
    kd_jenis = models.CharField(primary_key=True, max_length=5)
    nm_jenis = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ipsrsjenisbarang'


class Ipsrsopname(models.Model):
    kode_brng = models.OneToOneField(Ipsrsbarang, on_delete=models.DO_NOTHING, db_column='kode_brng', primary_key=True)
    h_beli = models.FloatField(blank=True, null=True)
    tanggal = models.DateField()
    stok = models.IntegerField()
    real = models.IntegerField()
    selisih = models.IntegerField()
    nomihilang = models.FloatField()
    lebih = models.IntegerField()
    nomilebih = models.FloatField()
    keterangan = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'ipsrsopname'
        unique_together = (('kode_brng', 'tanggal'),)


class Ipsrspembelian(models.Model):
    no_faktur = models.CharField(primary_key=True, max_length=15)
    kode_suplier = models.ForeignKey('suplier.Ipsrssuplier', on_delete=models.DO_NOTHING, db_column='kode_suplier')
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip')
    tgl_beli = models.DateField()
    subtotal = models.FloatField()
    potongan = models.FloatField()
    total = models.FloatField()
    ppn = models.FloatField(blank=True, null=True)
    meterai = models.FloatField(blank=True, null=True)
    tagihan = models.FloatField(blank=True, null=True)
    kd_rek = models.ForeignKey('keuangan.Rekening', on_delete=models.DO_NOTHING, db_column='kd_rek', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ipsrspembelian'


class Ipsrspemesanan(models.Model):
    no_faktur = models.CharField(primary_key=True, max_length=20)
    no_order = models.CharField(max_length=20)
    kode_suplier = models.ForeignKey('suplier.Ipsrssuplier', on_delete=models.DO_NOTHING, db_column='kode_suplier', blank=True, null=True)
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
    status = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ipsrspemesanan'


class Ipsrspengeluaran(models.Model):
    no_keluar = models.CharField(primary_key=True, max_length=15)
    tanggal = models.DateField()
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip')
    keterangan = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'ipsrspengeluaran'


class Ipsrsreturbeli(models.Model):
    no_retur_beli = models.CharField(primary_key=True, max_length=15)
    tgl_retur = models.DateField(blank=True, null=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    kode_suplier = models.ForeignKey('suplier.Ipsrssuplier', on_delete=models.DO_NOTHING, db_column='kode_suplier')
    catatan = models.CharField(max_length=40)
    total = models.FloatField()

    class Meta:
        managed = False
        db_table = 'ipsrsreturbeli'


class AkunAsetInventaris(models.Model):
    kd_rek = models.ForeignKey('keuangan.Rekening', on_delete=models.DO_NOTHING, db_column='kd_rek', blank=True, null=True)
    id_jenis = models.OneToOneField('InventarisJenis', on_delete=models.DO_NOTHING, db_column='id_jenis', primary_key=True)

    class Meta:
        managed = False
        db_table = 'akun_aset_inventaris'


class PengajuanBarangNonmedis(models.Model):
    no_pengajuan = models.CharField(primary_key=True, max_length=20)
    nip = models.ForeignKey('pegawai.Pegawai', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    tanggal = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=16, blank=True, null=True)
    keterangan = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pengajuan_barang_nonmedis'


class DetailPengajuanBarangNonmedis(models.Model):
    no_pengajuan = models.ForeignKey('PengajuanBarangNonmedis', on_delete=models.DO_NOTHING, db_column='no_pengajuan')
    kode_brng = models.ForeignKey('Ipsrsbarang', on_delete=models.DO_NOTHING, db_column='kode_brng')
    kode_sat = models.ForeignKey('data.Kodesatuan', on_delete=models.DO_NOTHING, db_column='kode_sat', blank=True, null=True)
    jumlah = models.FloatField(blank=True, null=True)
    h_pengajuan = models.FloatField(blank=True, null=True)
    total = models.FloatField()

    class Meta:
        managed = False
        db_table = 'detail_pengajuan_barang_nonmedis'


class PengajuanInventaris(models.Model):
    no_pengajuan = models.CharField(primary_key=True, max_length=20)
    tanggal = models.DateField()
    nik = models.ForeignKey('pegawai.Pegawai', on_delete=models.DO_NOTHING, db_column='nik', related_name='nik_pengajuan_inventaris')
    urgensi = models.CharField(max_length=9)
    latar_belakang = models.CharField(max_length=200)
    nama_barang = models.CharField(max_length=70)
    spesifikasi = models.CharField(max_length=200)
    jumlah = models.FloatField()
    harga = models.FloatField()
    total = models.FloatField()
    keterangan = models.CharField(max_length=70)
    nik_pj = models.ForeignKey('pegawai.Pegawai', on_delete=models.DO_NOTHING, db_column='nik_pj', related_name='nik_pj_pengajuan_inventaris')
    status = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'pengajuan_inventaris'
        
        
class InventarisHibah(models.Model):
    no_hibah = models.CharField(primary_key=True, max_length=20)
    kode_pemberi = models.ForeignKey('suplier.Pemberihibah', on_delete=models.DO_NOTHING, db_column='kode_pemberi', blank=True, null=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    tgl_hibah = models.DateField(blank=True, null=True)
    totalhibah = models.FloatField()
    kd_rek_aset = models.ForeignKey('keuangan.Rekening', on_delete=models.DO_NOTHING, db_column='kd_rek_aset', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventaris_hibah'
        
        
class InventarisPembelian(models.Model):
    no_faktur = models.CharField(primary_key=True, max_length=15)
    kode_suplier = models.ForeignKey('suplier.InventarisSuplier', on_delete=models.DO_NOTHING, db_column='kode_suplier')
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip')
    tgl_beli = models.DateField()
    subtotal = models.FloatField()
    potongan = models.FloatField()
    total = models.FloatField()
    ppn = models.FloatField(blank=True, null=True)
    meterai = models.FloatField(blank=True, null=True)
    tagihan = models.FloatField(blank=True, null=True)
    kd_rek = models.ForeignKey('keuangan.Rekening', on_delete=models.DO_NOTHING, db_column='kd_rek', blank=True, null=True, related_name='kd_rek_inventaris_pembelian')
    kd_rek_aset = models.ForeignKey('keuangan.Rekening', on_delete=models.DO_NOTHING, db_column='kd_rek_aset', related_name='kd_rek_aset_inventaris_pembelian')

    class Meta:
        managed = False
        db_table = 'inventaris_pembelian'
        

class PermintaanNonMedis(models.Model):
    no_permintaan = models.CharField(primary_key=True, max_length=20)
    ruang = models.CharField(max_length=50, blank=True, null=True)
    nip = models.ForeignKey('pegawai.Pegawai', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    tanggal = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permintaan_non_medis'


class DetailPermintaanNonMedis(models.Model):
    no_permintaan = models.ForeignKey('PermintaanNonMedis', on_delete=models.DO_NOTHING, db_column='no_permintaan', blank=True, null=True)
    kode_brng = models.ForeignKey('Ipsrsbarang', on_delete=models.DO_NOTHING, db_column='kode_brng', blank=True, null=True)
    kode_sat = models.ForeignKey('data.Kodesatuan', on_delete=models.DO_NOTHING, db_column='kode_sat', blank=True, null=True)
    jumlah = models.FloatField(blank=True, null=True)
    keterangan = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detail_permintaan_non_medis'


class BeriBhpRadiologi(models.Model):
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat')
    tgl_periksa = models.DateField()
    jam = models.TimeField()
    kode_brng = models.ForeignKey('Ipsrsbarang', on_delete=models.DO_NOTHING, db_column='kode_brng')
    kode_sat = models.ForeignKey('data.Kodesatuan', on_delete=models.DO_NOTHING, db_column='kode_sat')
    jumlah = models.FloatField()
    harga = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'beri_bhp_radiologi'
        
        
class DetailSuratPemesananNonMedis(models.Model):
    no_pemesanan = models.ForeignKey('administer.SuratPemesananNonMedis', on_delete=models.DO_NOTHING, db_column='no_pemesanan')
    kode_brng = models.ForeignKey('Ipsrsbarang', on_delete=models.DO_NOTHING, db_column='kode_brng')
    kode_sat = models.ForeignKey('data.Kodesatuan', on_delete=models.DO_NOTHING, db_column='kode_sat', blank=True, null=True)
    jumlah = models.FloatField(blank=True, null=True)
    h_pesan = models.FloatField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    dis = models.FloatField()
    besardis = models.FloatField()
    total = models.FloatField()

    class Meta:
        managed = False
        db_table = 'detail_surat_pemesanan_non_medis'




######################### INVENTARIS


class InventarisRuang(models.Model):
    id_ruang = models.CharField(primary_key=True, max_length=5)
    nama_ruang = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'inventaris_ruang'
        
        
class InventarisMerk(models.Model):
    id_merk = models.CharField(primary_key=True, max_length=10)
    nama_merk = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'inventaris_merk'
        

class InventarisPemesanan(models.Model):
    no_faktur = models.CharField(primary_key=True, max_length=20)
    no_order = models.CharField(max_length=20)
    kode_suplier = models.ForeignKey('suplier.InventarisSuplier', on_delete=models.DO_NOTHING, db_column='kode_suplier', blank=True, null=True)
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
    status = models.CharField(max_length=13, blank=True, null=True)
    kd_rek_aset = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'inventaris_pemesanan'


class InventarisBarang(models.Model):
    kode_barang = models.CharField(primary_key=True, max_length=20)
    nama_barang = models.CharField(max_length=60, blank=True, null=True)
    jml_barang = models.IntegerField(blank=True, null=True)
    kode_produsen = models.ForeignKey('suplier.InventarisProdusen', on_delete=models.DO_NOTHING, db_column='kode_produsen', blank=True, null=True)
    id_merk = models.ForeignKey('InventarisMerk', on_delete=models.DO_NOTHING, db_column='id_merk', blank=True, null=True)
    thn_produksi = models.TextField(blank=True, null=True)  # This field type is a guess.
    isbn = models.CharField(max_length=20, blank=True, null=True)
    id_kategori = models.ForeignKey('InventarisKategori', on_delete=models.DO_NOTHING, db_column='id_kategori', blank=True, null=True)
    id_jenis = models.ForeignKey('InventarisJenis', on_delete=models.DO_NOTHING, db_column='id_jenis', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventaris_barang'


class Inventaris(models.Model):
    no_inventaris = models.CharField(primary_key=True, max_length=30)
    kode_barang = models.ForeignKey('InventarisBarang', on_delete=models.DO_NOTHING, db_column='kode_barang', blank=True, null=True)
    asal_barang = models.CharField(max_length=7, blank=True, null=True)
    tgl_pengadaan = models.DateField(blank=True, null=True)
    harga = models.FloatField(blank=True, null=True)
    status_barang = models.CharField(max_length=9, blank=True, null=True)
    id_ruang = models.ForeignKey('InventarisRuang', on_delete=models.DO_NOTHING, db_column='id_ruang', blank=True, null=True)
    no_rak = models.CharField(max_length=3, blank=True, null=True)
    no_box = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventaris'


class PermintaanPerbaikanInventaris(models.Model):
    no_permintaan = models.CharField(primary_key=True, max_length=15)
    no_inventaris = models.ForeignKey(Inventaris, on_delete=models.DO_NOTHING, db_column='no_inventaris', blank=True, null=True)
    nik = models.ForeignKey('pegawai.Pegawai', on_delete=models.DO_NOTHING, db_column='nik', blank=True, null=True)
    tanggal = models.DateTimeField(blank=True, null=True)
    deskripsi_kerusakan = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permintaan_perbaikan_inventaris'


class PerbaikanInventaris(models.Model):
    no_permintaan = models.OneToOneField('PermintaanPerbaikanInventaris', on_delete=models.DO_NOTHING, db_column='no_permintaan', primary_key=True)
    tanggal = models.DateField()
    uraian_kegiatan = models.CharField(max_length=255)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip')
    pelaksana = models.CharField(max_length=19)
    biaya = models.FloatField()
    keterangan = models.CharField(max_length=255)
    status = models.CharField(max_length=21)

    class Meta:
        managed = False
        db_table = 'perbaikan_inventaris'


class PemeliharaanInventaris(models.Model):
    no_inventaris = models.OneToOneField(Inventaris, on_delete=models.DO_NOTHING, db_column='no_inventaris', primary_key=True)
    tanggal = models.DateField()
    uraian_kegiatan = models.CharField(max_length=255)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip')
    pelaksana = models.CharField(max_length=19)
    biaya = models.FloatField()
    jenis_pemeliharaan = models.CharField(max_length=21)

    class Meta:
        managed = False
        db_table = 'pemeliharaan_inventaris'
        unique_together = (('no_inventaris', 'tanggal'),)


class InventarisPeminjaman(models.Model):
    peminjam = models.CharField(primary_key=True, max_length=50)
    tlp = models.CharField(max_length=13)
    no_inventaris = models.ForeignKey(Inventaris, on_delete=models.DO_NOTHING, db_column='no_inventaris')
    tgl_pinjam = models.DateField()
    tgl_kembali = models.DateField(blank=True, null=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip')
    status_pinjam = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventaris_peminjaman'
        unique_together = (('peminjam', 'no_inventaris', 'tgl_pinjam', 'nip'),)


class InventarisBuktiPemesanan(models.Model):
    no_faktur = models.OneToOneField('InventarisPemesanan', on_delete=models.DO_NOTHING, db_column='no_faktur', primary_key=True)
    photo = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventaris_bukti_pemesanan'


class InventarisDetailBeli(models.Model):
    no_faktur = models.OneToOneField('InventarisPembelian', on_delete=models.DO_NOTHING, db_column='no_faktur', primary_key=True)
    kode_barang = models.ForeignKey(InventarisBarang, on_delete=models.DO_NOTHING, db_column='kode_barang')
    jumlah = models.FloatField()
    harga = models.FloatField()
    subtotal = models.FloatField()
    dis = models.FloatField()
    besardis = models.FloatField()
    total = models.FloatField()

    class Meta:
        managed = False
        db_table = 'inventaris_detail_beli'
        unique_together = (('no_faktur', 'kode_barang'),)


class InventarisDetailHibah(models.Model):
    no_hibah = models.OneToOneField('InventarisHibah', on_delete=models.DO_NOTHING, db_column='no_hibah', primary_key=True, related_name='no_hibah_inventaris_detail_hibah')
    kode_barang = models.ForeignKey(InventarisBarang, on_delete=models.DO_NOTHING, db_column='kode_barang', related_name='kode_barang_inventaris_detail_hibah')
    jumlah = models.FloatField(blank=True, null=True)
    h_hibah = models.FloatField(blank=True, null=True)
    subtotalhibah = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventaris_detail_hibah'
        unique_together = (('no_hibah', 'kode_barang'),)


class InventarisDetailPesan(models.Model):
    no_faktur = models.ForeignKey('InventarisPemesanan', on_delete=models.DO_NOTHING, db_column='no_faktur')
    kode_barang = models.ForeignKey(InventarisBarang, on_delete=models.DO_NOTHING, db_column='kode_barang')
    jumlah = models.FloatField()
    harga = models.FloatField()
    subtotal = models.FloatField()
    dis = models.FloatField()
    besardis = models.FloatField()
    total = models.FloatField()

    class Meta:
        managed = False
        db_table = 'inventaris_detail_pesan'



class InventarisTitipFaktur(models.Model):
    no_tagihan = models.CharField(primary_key=True, max_length=20)
    tanggal = models.DateField(blank=True, null=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    keterangan = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'inventaris_titip_faktur'
        
        
class InventarisDetailTitipFaktur(models.Model):
    no_tagihan = models.OneToOneField('InventarisTitipFaktur', on_delete=models.DO_NOTHING, db_column='no_tagihan', primary_key=True)
    no_faktur = models.ForeignKey('InventarisPemesanan', on_delete=models.DO_NOTHING, db_column='no_faktur')

    class Meta:
        managed = False
        db_table = 'inventaris_detail_titip_faktur'
        unique_together = (('no_tagihan', 'no_faktur'),)



class InventarisJenis(models.Model):
    id_jenis = models.CharField(primary_key=True, max_length=10)
    nama_jenis = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventaris_jenis'


class InventarisKategori(models.Model):
    id_kategori = models.CharField(primary_key=True, max_length=10)
    nama_kategori = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventaris_kategori'


class PeminjamanBerkas(models.Model):
    peminjam = models.CharField(primary_key=True, max_length=60)
    id_ruang = models.ForeignKey(InventarisRuang, on_delete=models.DO_NOTHING, db_column='id_ruang')
    no_rkm_medis = models.ForeignKey('pasien.Pasien', on_delete=models.DO_NOTHING, db_column='no_rkm_medis')
    tgl_pinjam = models.DateField()
    tgl_kembali = models.DateField()
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip')
    status_pinjam = models.CharField(max_length=14)

    class Meta:
        managed = False
        db_table = 'peminjaman_berkas'
        unique_together = (('peminjam', 'id_ruang', 'no_rkm_medis', 'tgl_pinjam', 'nip'),)


class CssdBarang(models.Model):
    no_inventaris = models.OneToOneField('Inventaris', on_delete=models.DO_NOTHING, db_column='no_inventaris', primary_key=True)
    jenis_barang = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cssd_barang'


