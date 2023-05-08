from django.db import models

# Create your models here.

class TokoPengajuanBarang(models.Model):
    no_pengajuan = models.CharField(primary_key=True, max_length=20)
    nip = models.ForeignKey('pegawai.Pegawai', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    tanggal = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=16, blank=True, null=True)
    keterangan = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'toko_pengajuan_barang'


class Tokobarang(models.Model):
    kode_brng = models.CharField(primary_key=True, max_length=40)
    nama_brng = models.CharField(max_length=80)
    kode_sat = models.ForeignKey('data.Kodesatuan', on_delete=models.DO_NOTHING, db_column='kode_sat')
    jenis = models.ForeignKey('Tokojenisbarang', on_delete=models.DO_NOTHING, db_column='jenis', blank=True, null=True)
    stok = models.FloatField()
    dasar = models.FloatField()
    h_beli = models.FloatField()
    distributor = models.FloatField()
    grosir = models.FloatField()
    retail = models.FloatField()
    status = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'tokobarang'


class TokoRiwayatBarang(models.Model):
    kode_brng = models.ForeignKey('Tokobarang', on_delete=models.DO_NOTHING, db_column='kode_brng', blank=True, null=True)
    stok_awal = models.FloatField(blank=True, null=True)
    masuk = models.FloatField(blank=True, null=True)
    keluar = models.FloatField(blank=True, null=True)
    stok_akhir = models.FloatField()
    posisi = models.CharField(max_length=13, blank=True, null=True)
    tanggal = models.DateField(blank=True, null=True)
    jam = models.TimeField(blank=True, null=True)
    petugas = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'toko_riwayat_barang'


class Tokosuplier(models.Model):
    kode_suplier = models.CharField(primary_key=True, max_length=5)
    nama_suplier = models.CharField(max_length=50, blank=True, null=True)
    alamat = models.CharField(max_length=50, blank=True, null=True)
    kota = models.CharField(max_length=20, blank=True, null=True)
    no_telp = models.CharField(max_length=13, blank=True, null=True)
    nama_bank = models.CharField(max_length=30, blank=True, null=True)
    rekening = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tokosuplier'


class TokoSuratPemesanan(models.Model):
    no_pemesanan = models.CharField(primary_key=True, max_length=20)
    kode_suplier = models.ForeignKey('Tokosuplier', on_delete=models.DO_NOTHING, db_column='kode_suplier', blank=True, null=True)
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
        db_table = 'toko_surat_pemesanan'


class Tokojenisbarang(models.Model):
    kd_jenis = models.CharField(primary_key=True, max_length=5)
    nm_jenis = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tokojenisbarang'
        
        
class Tokomember(models.Model):
    no_member = models.CharField(primary_key=True, max_length=10)
    nama = models.CharField(max_length=50, blank=True, null=True)
    jk = models.CharField(max_length=1, blank=True, null=True)
    tmp_lahir = models.CharField(max_length=20, blank=True, null=True)
    tgl_lahir = models.DateField(blank=True, null=True)
    alamat = models.CharField(max_length=60, blank=True, null=True)
    no_telp = models.CharField(max_length=40, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tokomember'


class Tokoopname(models.Model):
    kode_brng = models.OneToOneField(Tokobarang, on_delete=models.DO_NOTHING, db_column='kode_brng', primary_key=True)
    dasar = models.FloatField(blank=True, null=True)
    tanggal = models.DateField()
    stok = models.IntegerField()
    real = models.IntegerField()
    selisih = models.IntegerField()
    nomihilang = models.FloatField()
    keterangan = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'tokoopname'
        unique_together = (('kode_brng', 'tanggal'),)


class Tokopembelian(models.Model):
    no_faktur = models.CharField(primary_key=True, max_length=20)
    kode_suplier = models.ForeignKey('Tokosuplier', on_delete=models.DO_NOTHING, db_column='kode_suplier')
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip')
    tgl_beli = models.DateField()
    subtotal = models.FloatField()
    potongan = models.FloatField()
    total = models.FloatField()
    ppn = models.FloatField(blank=True, null=True)
    meterai = models.FloatField(blank=True, null=True)
    tagihan = models.FloatField(blank=True, null=True)
    kd_rek = models.ForeignKey('keuangan.AkunBayar', on_delete=models.DO_NOTHING, db_column='kd_rek', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tokopembelian'


class Tokopemesanan(models.Model):
    no_faktur = models.CharField(primary_key=True, max_length=20)
    no_order = models.CharField(max_length=20)
    kode_suplier = models.ForeignKey('Tokosuplier', on_delete=models.DO_NOTHING, db_column='kode_suplier', blank=True, null=True)
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
        db_table = 'tokopemesanan'


class Tokopenjualan(models.Model):
    nota_jual = models.CharField(primary_key=True, max_length=15)
    tgl_jual = models.DateField(blank=True, null=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    no_member = models.ForeignKey(Tokomember, on_delete=models.DO_NOTHING, db_column='no_member', blank=True, null=True)
    nm_member = models.CharField(max_length=50, blank=True, null=True)
    keterangan = models.CharField(max_length=40, blank=True, null=True)
    jns_jual = models.CharField(max_length=11, blank=True, null=True)
    ongkir = models.FloatField(blank=True, null=True)
    ppn = models.FloatField()
    kd_rek = models.ForeignKey('keuangan.Rekening', on_delete=models.DO_NOTHING, db_column='kd_rek', blank=True, null=True)
    total = models.FloatField()
    nama_bayar = models.ForeignKey('keuangan.AkunBayar', on_delete=models.DO_NOTHING, db_column='nama_bayar')

    class Meta:
        managed = False
        db_table = 'tokopenjualan'


class Tokopiutang(models.Model):
    nota_piutang = models.CharField(primary_key=True, max_length=15)
    tgl_piutang = models.DateField(blank=True, null=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    no_member = models.ForeignKey(Tokomember, on_delete=models.DO_NOTHING, db_column='no_member', blank=True, null=True)
    nm_member = models.CharField(max_length=50, blank=True, null=True)
    catatan = models.CharField(max_length=40, blank=True, null=True)
    jns_jual = models.CharField(max_length=11, blank=True, null=True)
    ongkir = models.FloatField(blank=True, null=True)
    uangmuka = models.FloatField(blank=True, null=True)
    sisapiutang = models.FloatField()
    tgltempo = models.DateField()

    class Meta:
        managed = False
        db_table = 'tokopiutang'


class Tokoreturbeli(models.Model):
    no_retur_beli = models.CharField(primary_key=True, max_length=15)
    tgl_retur = models.DateField(blank=True, null=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    kode_suplier = models.ForeignKey('Tokosuplier', on_delete=models.DO_NOTHING, db_column='kode_suplier')
    catatan = models.CharField(max_length=40)
    total = models.FloatField()

    class Meta:
        managed = False
        db_table = 'tokoreturbeli'


class Tokoreturjual(models.Model):
    no_retur_jual = models.CharField(primary_key=True, max_length=15)
    tgl_retur = models.DateField(blank=True, null=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    no_member = models.ForeignKey(Tokomember, on_delete=models.DO_NOTHING, db_column='no_member')
    catatan = models.CharField(max_length=40)
    total = models.FloatField()

    class Meta:
        managed = False
        db_table = 'tokoreturjual'


class Tokoreturpiutang(models.Model):
    no_retur_piutang = models.CharField(primary_key=True, max_length=15)
    tgl_retur = models.DateField(blank=True, null=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    no_member = models.ForeignKey(Tokomember, on_delete=models.DO_NOTHING, db_column='no_member')
    catatan = models.CharField(max_length=40)
    total = models.FloatField()

    class Meta:
        managed = False
        db_table = 'tokoreturpiutang'


class Tokosetharga(models.Model):
    distributor = models.FloatField()
    grosir = models.FloatField()
    retail = models.FloatField()

    class Meta:
        managed = False
        db_table = 'tokosetharga'


class TokoBayarPemesanan(models.Model):
    tgl_bayar = models.DateField(blank=True, null=True)
    no_faktur = models.ForeignKey('Tokopemesanan', on_delete=models.DO_NOTHING, db_column='no_faktur', blank=True, null=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    besar_bayar = models.FloatField(blank=True, null=True)
    keterangan = models.CharField(max_length=100, blank=True, null=True)
    nama_bayar = models.ForeignKey('keuangan.AkunBayar', on_delete=models.DO_NOTHING, db_column='nama_bayar', blank=True, null=True)
    no_bukti = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'toko_bayar_pemesanan'


class TokoBayarPiutang(models.Model):
    tgl_bayar = models.DateField(primary_key=True)
    no_member = models.ForeignKey('Tokomember', on_delete=models.DO_NOTHING, db_column='no_member')
    besar_cicilan = models.FloatField()
    catatan = models.CharField(max_length=100)
    nota_piutang = models.ForeignKey('Tokopiutang', on_delete=models.DO_NOTHING, db_column='nota_piutang')
    kd_rek = models.ForeignKey('keuangan.Rekening', on_delete=models.DO_NOTHING, db_column='kd_rek', related_name='kd_rek_toko_bayar_piutang')
    kd_rek_kontra = models.ForeignKey('keuangan.Rekening', on_delete=models.DO_NOTHING, db_column='kd_rek_kontra', related_name='kd_rek_kontra_toko_bayar_piutang')

    class Meta:
        managed = False
        db_table = 'toko_bayar_piutang'
        unique_together = (('tgl_bayar', 'no_member', 'nota_piutang', 'kd_rek', 'kd_rek_kontra'),)


class TokoDetailBeli(models.Model):
    no_faktur = models.ForeignKey('Tokopembelian', on_delete=models.DO_NOTHING, db_column='no_faktur')
    kode_brng = models.ForeignKey('Tokobarang', on_delete=models.DO_NOTHING, db_column='kode_brng', blank=True, null=True)
    kode_sat = models.ForeignKey('data.Kodesatuan', on_delete=models.DO_NOTHING, db_column='kode_sat')
    jumlah = models.FloatField()
    harga = models.FloatField()
    subtotal = models.FloatField()
    dis = models.FloatField()
    besardis = models.FloatField()
    total = models.FloatField()

    class Meta:
        managed = False
        db_table = 'toko_detail_beli'


class TokoDetailJual(models.Model):
    nota_jual = models.ForeignKey('Tokopenjualan', on_delete=models.DO_NOTHING, db_column='nota_jual')
    kode_brng = models.ForeignKey('Tokobarang', on_delete=models.DO_NOTHING, db_column='kode_brng', blank=True, null=True)
    kode_sat = models.ForeignKey('data.Kodesatuan', on_delete=models.DO_NOTHING, db_column='kode_sat', blank=True, null=True)
    h_jual = models.FloatField(blank=True, null=True)
    h_beli = models.FloatField(blank=True, null=True)
    jumlah = models.FloatField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    dis = models.FloatField(blank=True, null=True)
    bsr_dis = models.FloatField(blank=True, null=True)
    tambahan = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'toko_detail_jual'


class TokoDetailPengajuanBarang(models.Model):
    no_pengajuan = models.ForeignKey('TokoPengajuanBarang', on_delete=models.DO_NOTHING, db_column='no_pengajuan')
    kode_brng = models.ForeignKey('Tokobarang', on_delete=models.DO_NOTHING, db_column='kode_brng', blank=True, null=True)
    kode_sat = models.ForeignKey('data.Kodesatuan', on_delete=models.DO_NOTHING, db_column='kode_sat', blank=True, null=True)
    jumlah = models.FloatField(blank=True, null=True)
    h_pengajuan = models.FloatField(blank=True, null=True)
    total = models.FloatField()

    class Meta:
        managed = False
        db_table = 'toko_detail_pengajuan_barang'


class TokoDetailPesan(models.Model):
    no_faktur = models.ForeignKey('Tokopemesanan', on_delete=models.DO_NOTHING, db_column='no_faktur')
    kode_brng = models.ForeignKey('Tokobarang', on_delete=models.DO_NOTHING, db_column='kode_brng', blank=True, null=True)
    kode_sat = models.ForeignKey('data.Kodesatuan', on_delete=models.DO_NOTHING, db_column='kode_sat')
    jumlah = models.FloatField()
    harga = models.FloatField()
    subtotal = models.FloatField()
    dis = models.FloatField()
    besardis = models.FloatField()
    total = models.FloatField()

    class Meta:
        managed = False
        db_table = 'toko_detail_pesan'


class TokoDetailPiutang(models.Model):
    nota_piutang = models.ForeignKey('Tokopiutang', on_delete=models.DO_NOTHING, db_column='nota_piutang', blank=True, null=True)
    kode_brng = models.ForeignKey('Tokobarang', on_delete=models.DO_NOTHING, db_column='kode_brng', blank=True, null=True)
    kode_sat = models.ForeignKey('data.Kodesatuan', on_delete=models.DO_NOTHING, db_column='kode_sat', blank=True, null=True)
    h_jual = models.FloatField(blank=True, null=True)
    h_beli = models.FloatField(blank=True, null=True)
    jumlah = models.FloatField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    dis = models.FloatField(blank=True, null=True)
    bsr_dis = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'toko_detail_piutang'


class TokoDetailReturbeli(models.Model):
    no_retur_beli = models.ForeignKey('Tokoreturbeli', on_delete=models.DO_NOTHING, db_column='no_retur_beli')
    no_faktur = models.CharField(max_length=20)
    kode_brng = models.ForeignKey('Tokobarang', on_delete=models.DO_NOTHING, db_column='kode_brng')
    kode_sat = models.ForeignKey('data.Kodesatuan', on_delete=models.DO_NOTHING, db_column='kode_sat', blank=True, null=True)
    h_beli = models.FloatField(blank=True, null=True)
    h_retur = models.FloatField(blank=True, null=True)
    jml_retur = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'toko_detail_returbeli'


class TokoDetailReturjual(models.Model):
    no_retur_jual = models.ForeignKey('Tokoreturjual', on_delete=models.DO_NOTHING, db_column='no_retur_jual')
    nota_jual = models.CharField(max_length=15)
    kode_brng = models.ForeignKey('Tokobarang', on_delete=models.DO_NOTHING, db_column='kode_brng')
    kode_sat = models.ForeignKey('data.Kodesatuan', on_delete=models.DO_NOTHING, db_column='kode_sat', blank=True, null=True)
    h_jual = models.FloatField(blank=True, null=True)
    h_retur = models.FloatField(blank=True, null=True)
    jml_retur = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'toko_detail_returjual'


class TokoDetailReturpiutang(models.Model):
    no_retur_piutang = models.ForeignKey('Tokoreturpiutang', on_delete=models.DO_NOTHING, db_column='no_retur_piutang')
    nota_piutang = models.CharField(max_length=15)
    kode_brng = models.ForeignKey('Tokobarang', on_delete=models.DO_NOTHING, db_column='kode_brng')
    kode_sat = models.ForeignKey('data.Kodesatuan', on_delete=models.DO_NOTHING, db_column='kode_sat', blank=True, null=True)
    h_piutang = models.FloatField(blank=True, null=True)
    h_retur = models.FloatField(blank=True, null=True)
    jml_retur = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'toko_detail_returpiutang'


class TokoDInteetailSuratPemesanan(models.Model):
    no_pemesanan = models.ForeignKey('TokoSuratPemesanan', on_delete=models.DO_NOTHING, db_column='no_pemesanan')
    kode_brng = models.ForeignKey('Tokobarang', on_delete=models.DO_NOTHING, db_column='kode_brng', blank=True, null=True)
    kode_sat = models.ForeignKey('data.Kodesatuan', on_delete=models.DO_NOTHING, db_column='kode_sat', blank=True, null=True)
    jumlah = models.FloatField(blank=True, null=True)
    h_pesan = models.FloatField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    dis = models.FloatField()
    besardis = models.FloatField()
    total = models.FloatField()

    class Meta:
        managed = False
        db_table = 'toko_detail_surat_pemesanan'

