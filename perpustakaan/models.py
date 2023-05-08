from django.db import models

# Create your models here.


class PerpustakaanAnggota(models.Model):
    no_anggota = models.CharField(primary_key=True, max_length=10)
    nama_anggota = models.CharField(max_length=40, blank=True, null=True)
    tmp_lahir = models.CharField(max_length=20, blank=True, null=True)
    tgl_lahir = models.DateField(blank=True, null=True)
    j_kel = models.CharField(max_length=1, blank=True, null=True)
    alamat = models.CharField(max_length=70, blank=True, null=True)
    no_telp = models.CharField(max_length=13, blank=True, null=True)
    email = models.CharField(max_length=25, blank=True, null=True)
    tgl_gabung = models.DateField(blank=True, null=True)
    masa_berlaku = models.DateField(blank=True, null=True)
    jenis_anggota = models.CharField(max_length=7)
    nomer_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'perpustakaan_anggota'


class PerpustakaanBayarDenda(models.Model):
    tgl_denda = models.DateField(primary_key=True)
    no_anggota = models.ForeignKey(PerpustakaanAnggota, on_delete=models.DO_NOTHING, db_column='no_anggota')
    no_inventaris = models.ForeignKey('PerpustakaanInventaris', on_delete=models.DO_NOTHING, db_column='no_inventaris')
    kode_denda = models.ForeignKey('PerpustakaanDenda', on_delete=models.DO_NOTHING, db_column='kode_denda')
    besar_denda = models.FloatField(blank=True, null=True)
    keterangan_denda = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perpustakaan_bayar_denda'
        unique_together = (('tgl_denda', 'no_anggota', 'no_inventaris', 'kode_denda'),)


class PerpustakaanBayarDendaHarian(models.Model):
    tgl_denda = models.DateField(primary_key=True)
    no_anggota = models.ForeignKey(PerpustakaanAnggota, on_delete=models.DO_NOTHING, db_column='no_anggota')
    no_inventaris = models.ForeignKey('PerpustakaanInventaris', on_delete=models.DO_NOTHING, db_column='no_inventaris')
    keterlambatan = models.IntegerField(blank=True, null=True)
    besar_denda = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perpustakaan_bayar_denda_harian'
        unique_together = (('tgl_denda', 'no_anggota', 'no_inventaris'),)


class PerpustakaanBuku(models.Model):
    kode_buku = models.CharField(primary_key=True, max_length=10)
    judul_buku = models.CharField(max_length=200, blank=True, null=True)
    jml_halaman = models.CharField(max_length=5, blank=True, null=True)
    kode_penerbit = models.ForeignKey('PerpustakaanPenerbit', on_delete=models.DO_NOTHING, db_column='kode_penerbit', blank=True, null=True)
    kode_pengarang = models.ForeignKey('PerpustakaanPengarang', on_delete=models.DO_NOTHING, db_column='kode_pengarang', blank=True, null=True)
    thn_terbit = models.TextField(blank=True, null=True)  # This field type is a guess.
    isbn = models.CharField(max_length=20, blank=True, null=True)
    id_kategori = models.ForeignKey('PerpustakaanKategori', on_delete=models.DO_NOTHING, db_column='id_kategori', blank=True, null=True)
    id_jenis = models.ForeignKey('PerpustakaanJenisBuku', on_delete=models.DO_NOTHING, db_column='id_jenis', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perpustakaan_buku'


class PerpustakaanDenda(models.Model):
    kode_denda = models.CharField(primary_key=True, max_length=5)
    jenis_denda = models.CharField(max_length=40, blank=True, null=True)
    besar_denda = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perpustakaan_denda'


class PerpustakaanEbook(models.Model):
    kode_ebook = models.CharField(primary_key=True, max_length=10)
    judul_ebook = models.CharField(max_length=200, blank=True, null=True)
    jml_halaman = models.CharField(max_length=5, blank=True, null=True)
    kode_penerbit = models.ForeignKey('PerpustakaanPenerbit', on_delete=models.DO_NOTHING, db_column='kode_penerbit', blank=True, null=True)
    kode_pengarang = models.ForeignKey('PerpustakaanPengarang', on_delete=models.DO_NOTHING, db_column='kode_pengarang', blank=True, null=True)
    thn_terbit = models.TextField(blank=True, null=True)  # This field type is a guess.
    id_kategori = models.ForeignKey('PerpustakaanKategori', on_delete=models.DO_NOTHING, db_column='id_kategori', blank=True, null=True)
    id_jenis = models.ForeignKey('PerpustakaanJenisBuku', on_delete=models.DO_NOTHING, db_column='id_jenis', blank=True, null=True)
    berkas = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'perpustakaan_ebook'


class PerpustakaanInventaris(models.Model):
    no_inventaris = models.CharField(primary_key=True, max_length=20)
    kode_buku = models.ForeignKey(PerpustakaanBuku, on_delete=models.DO_NOTHING, db_column='kode_buku', blank=True, null=True)
    asal_buku = models.CharField(max_length=7, blank=True, null=True)
    tgl_pengadaan = models.DateField(blank=True, null=True)
    harga = models.FloatField(blank=True, null=True)
    status_buku = models.CharField(max_length=8, blank=True, null=True)
    kd_ruang = models.ForeignKey('PerpustakaanRuang', on_delete=models.DO_NOTHING, db_column='kd_ruang', blank=True, null=True)
    no_rak = models.CharField(max_length=3, blank=True, null=True)
    no_box = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perpustakaan_inventaris'


class PerpustakaanJenisBuku(models.Model):
    id_jenis = models.CharField(primary_key=True, max_length=5)
    nama_jenis = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perpustakaan_jenis_buku'


class PerpustakaanKategori(models.Model):
    id_kategori = models.CharField(primary_key=True, max_length=5)
    nama_kategori = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perpustakaan_kategori'


class PerpustakaanPeminjaman(models.Model):
    no_anggota = models.ForeignKey(PerpustakaanAnggota, on_delete=models.DO_NOTHING, db_column='no_anggota', blank=True, null=True)
    no_inventaris = models.ForeignKey(PerpustakaanInventaris, on_delete=models.DO_NOTHING, db_column='no_inventaris', blank=True, null=True)
    tgl_pinjam = models.DateField(blank=True, null=True)
    tgl_kembali = models.DateField(blank=True, null=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    status_pinjam = models.CharField(max_length=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perpustakaan_peminjaman'


class PerpustakaanPenerbit(models.Model):
    kode_penerbit = models.CharField(primary_key=True, max_length=10)
    nama_penerbit = models.CharField(max_length=40, blank=True, null=True)
    alamat_penerbit = models.CharField(max_length=70, blank=True, null=True)
    no_telp = models.CharField(max_length=13, blank=True, null=True)
    email = models.CharField(max_length=25, blank=True, null=True)
    website_penerbit = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perpustakaan_penerbit'


class PerpustakaanPengarang(models.Model):
    kode_pengarang = models.CharField(primary_key=True, max_length=7)
    nama_pengarang = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perpustakaan_pengarang'


class PerpustakaanRuang(models.Model):
    kd_ruang = models.CharField(primary_key=True, max_length=5)
    nm_ruang = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perpustakaan_ruang'


class PerpustakaanSetPeminjaman(models.Model):
    max_pinjam = models.IntegerField(blank=True, null=True)
    lama_pinjam = models.IntegerField(blank=True, null=True)
    denda_perhari = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perpustakaan_set_peminjaman'

