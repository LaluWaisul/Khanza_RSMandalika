from django.db import models

# Create your models here.


class JnsPerawatanUtd(models.Model):
    kd_jenis_prw = models.CharField(primary_key=True, max_length=15)
    nm_perawatan = models.CharField(max_length=80, blank=True, null=True)
    bagian_rs = models.FloatField(blank=True, null=True)
    bhp = models.FloatField(blank=True, null=True)
    tarif_perujuk = models.FloatField(blank=True, null=True)
    tarif_tindakan_dokter = models.FloatField(blank=True, null=True)
    tarif_tindakan_petugas = models.FloatField(blank=True, null=True)
    kso = models.FloatField(blank=True, null=True)
    manajemen = models.FloatField(blank=True, null=True)
    total_byr = models.FloatField(blank=True, null=True)
    kd_pj = models.ForeignKey('asuransi.Penjab', on_delete=models.DO_NOTHING, db_column='kd_pj', blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jns_perawatan_utd'


class TemplateUtd(models.Model):
    kd_jenis_prw = models.ForeignKey(JnsPerawatanUtd, on_delete=models.DO_NOTHING, db_column='kd_jenis_prw', blank=True, null=True)
    id_template = models.AutoField(primary_key=True)
    pemeriksaan = models.CharField(max_length=200, blank=True, null=True)
    nilai_rujukan = models.CharField(max_length=30)
    bagian_rs = models.FloatField(blank=True, null=True)
    bhp = models.FloatField(blank=True, null=True)
    bagian_perujuk = models.FloatField(blank=True, null=True)
    bagian_dokter = models.FloatField(blank=True, null=True)
    petugas_utd = models.FloatField(blank=True, null=True)
    kso = models.FloatField(blank=True, null=True)
    menejemen = models.FloatField(blank=True, null=True)
    biaya_item = models.FloatField(blank=True, null=True)
    urut = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'template_utd'


class UtdPendonor(models.Model):
    no_pendonor = models.CharField(primary_key=True, max_length=15)
    nama = models.CharField(max_length=40)
    no_ktp = models.CharField(max_length=20)
    jk = models.CharField(max_length=1)
    tmp_lahir = models.CharField(max_length=15)
    tgl_lahir = models.DateField()
    alamat = models.CharField(max_length=100)
    kd_kel = models.ForeignKey('alamat.Kelurahan', on_delete=models.DO_NOTHING, db_column='kd_kel')
    kd_kec = models.ForeignKey('alamat.Kecamatan', on_delete=models.DO_NOTHING, db_column='kd_kec')
    kd_kab = models.ForeignKey('alamat.Kabupaten', on_delete=models.DO_NOTHING, db_column='kd_kab')
    kd_prop = models.ForeignKey('alamat.Propinsi', on_delete=models.DO_NOTHING, db_column='kd_prop')
    golongan_darah = models.CharField(max_length=2)
    resus = models.CharField(max_length=3)
    no_telp = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'utd_pendonor'


class UtdDonor(models.Model):
    no_donor = models.CharField(primary_key=True, max_length=15)
    no_pendonor = models.ForeignKey('UtdPendonor', on_delete=models.DO_NOTHING, db_column='no_pendonor')
    tanggal = models.DateField(blank=True, null=True)
    dinas = models.CharField(max_length=5, blank=True, null=True)
    tensi = models.CharField(max_length=7, blank=True, null=True)
    no_bag = models.IntegerField(blank=True, null=True)
    jenis_bag = models.CharField(max_length=2, blank=True, null=True)
    jenis_donor = models.CharField(max_length=2, blank=True, null=True)
    tempat_aftap = models.CharField(max_length=12, blank=True, null=True)
    petugas_aftap = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='petugas_aftap', blank=True, null=True, related_name='petugas_aftap_utd_donor')
    hbsag = models.CharField(max_length=7, blank=True, null=True)
    hcv = models.CharField(max_length=7, blank=True, null=True)
    hiv = models.CharField(max_length=7, blank=True, null=True)
    spilis = models.CharField(max_length=7, blank=True, null=True)
    malaria = models.CharField(max_length=7, blank=True, null=True)
    petugas_u_saring = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='petugas_u_saring', blank=True, null=True, related_name='petugas_u_saring_utd_donor')
    status = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utd_donor'


class UtdCekalDarah(models.Model):
    no_donor = models.OneToOneField('UtdDonor', on_delete=models.DO_NOTHING, db_column='no_donor', primary_key=True)
    tanggal = models.DateField(blank=True, null=True)
    dinas = models.CharField(max_length=5, blank=True, null=True)
    petugas_pemusnahan = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='petugas_pemusnahan', blank=True, null=True)
    keterangan = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utd_cekal_darah'


class UtdDetailPemisahanKomponen(models.Model):
    no_donor = models.ForeignKey('UtdPemisahanKomponen', on_delete=models.DO_NOTHING, db_column='no_donor', blank=True, null=True)
    no_kantong = models.CharField(primary_key=True, max_length=20)
    kode_komponen = models.CharField(max_length=5, blank=True, null=True)
    tanggal_kadaluarsa = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utd_detail_pemisahan_komponen'


class UtdKomponenDarah(models.Model):
    kode = models.CharField(primary_key=True, max_length=5)
    nama = models.CharField(max_length=70, blank=True, null=True)
    lama = models.SmallIntegerField(blank=True, null=True)
    jasa_sarana = models.FloatField(blank=True, null=True)
    paket_bhp = models.FloatField(blank=True, null=True)
    kso = models.FloatField(blank=True, null=True)
    manajemen = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    pembatalan = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utd_komponen_darah'


class UtdMedisRusak(models.Model):
    kode_brng = models.OneToOneField('farmasi.Databarang', on_delete=models.DO_NOTHING, db_column='kode_brng', primary_key=True)
    jml = models.FloatField(blank=True, null=True)
    hargabeli = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip')
    tanggal = models.DateTimeField()
    keterangan = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utd_medis_rusak'
        unique_together = (('kode_brng', 'nip', 'tanggal'),)


class UtdPemisahanKomponen(models.Model):
    no_donor = models.OneToOneField(UtdDonor, on_delete=models.DO_NOTHING, db_column='no_donor', primary_key=True)
    tanggal = models.DateField(blank=True, null=True)
    dinas = models.CharField(max_length=5, blank=True, null=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utd_pemisahan_komponen'


class UtdPengambilanMedis(models.Model):
    kode_brng = models.OneToOneField('farmasi.Databarang', on_delete=models.DO_NOTHING, db_column='kode_brng', primary_key=True)
    jml = models.FloatField(blank=True, null=True)
    hargabeli = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    kd_bangsal_dr = models.ForeignKey('bangsal.Bangsal', on_delete=models.DO_NOTHING, db_column='kd_bangsal_dr')
    tanggal = models.DateTimeField()
    keterangan = models.CharField(max_length=60, blank=True, null=True)
    no_batch = models.CharField(max_length=20)
    no_faktur = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'utd_pengambilan_medis'
        unique_together = (('kode_brng', 'tanggal', 'no_batch', 'no_faktur'),)


class UtdPengambilanPenunjang(models.Model):
    kode_brng = models.OneToOneField('aset.Ipsrsbarang', on_delete=models.DO_NOTHING, db_column='kode_brng', primary_key=True)
    jml = models.FloatField(blank=True, null=True)
    harga = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip')
    tanggal = models.DateTimeField()
    keterangan = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utd_pengambilan_penunjang'
        unique_together = (('kode_brng', 'nip', 'tanggal'),)


class UtdPenggunaanMedisDonor(models.Model):
    no_donor = models.OneToOneField(UtdDonor, on_delete=models.DO_NOTHING, db_column='no_donor', primary_key=True)
    kode_brng = models.ForeignKey('farmasi.Databarang', on_delete=models.DO_NOTHING, db_column='kode_brng')
    jml = models.FloatField(blank=True, null=True)
    harga = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utd_penggunaan_medis_donor'
        unique_together = (('no_donor', 'kode_brng'),)


class UtdPenggunaanMedisPemisahanKomponen(models.Model):
    no_donor = models.OneToOneField(UtdPemisahanKomponen, on_delete=models.DO_NOTHING, db_column='no_donor', primary_key=True)
    kode_brng = models.ForeignKey('farmasi.Databarang', on_delete=models.DO_NOTHING, db_column='kode_brng')
    jml = models.FloatField(blank=True, null=True)
    harga = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utd_penggunaan_medis_pemisahan_komponen'
        unique_together = (('no_donor', 'kode_brng'),)


class UtdPenggunaanMedisPenyerahanDarah(models.Model):
    no_penyerahan = models.OneToOneField('UtdPenyerahanDarah', on_delete=models.DO_NOTHING, db_column='no_penyerahan', primary_key=True)
    kode_brng = models.ForeignKey('farmasi.Databarang', on_delete=models.DO_NOTHING, db_column='kode_brng')
    jml = models.FloatField(blank=True, null=True)
    harga = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utd_penggunaan_medis_penyerahan_darah'
        unique_together = (('no_penyerahan', 'kode_brng'),)


class UtdPenggunaanPenunjangDonor(models.Model):
    no_donor = models.OneToOneField(UtdDonor, on_delete=models.DO_NOTHING, db_column='no_donor', primary_key=True)
    kode_brng = models.ForeignKey('aset.Ipsrsbarang', on_delete=models.DO_NOTHING, db_column='kode_brng')
    jml = models.FloatField(blank=True, null=True)
    harga = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utd_penggunaan_penunjang_donor'
        unique_together = (('no_donor', 'kode_brng'),)


class UtdPenggunaanPenunjangPemisahanKomponen(models.Model):
    no_donor = models.OneToOneField(UtdPemisahanKomponen, on_delete=models.DO_NOTHING, db_column='no_donor', primary_key=True)
    kode_brng = models.ForeignKey('aset.Ipsrsbarang', on_delete=models.DO_NOTHING, db_column='kode_brng')
    jml = models.FloatField(blank=True, null=True)
    harga = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utd_penggunaan_penunjang_pemisahan_komponen'
        unique_together = (('no_donor', 'kode_brng'),)


class UtdPenggunaanPenunjangPenyerahanDarah(models.Model):
    no_penyerahan = models.OneToOneField('UtdPenyerahanDarah', on_delete=models.DO_NOTHING, db_column='no_penyerahan', primary_key=True)
    kode_brng = models.ForeignKey('aset.Ipsrsbarang', on_delete=models.DO_NOTHING, db_column='kode_brng')
    jml = models.FloatField(blank=True, null=True)
    harga = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utd_penggunaan_penunjang_penyerahan_darah'
        unique_together = (('no_penyerahan', 'kode_brng'),)


class UtdPenunjangRusak(models.Model):
    kode_brng = models.OneToOneField('aset.Ipsrsbarang', on_delete=models.DO_NOTHING, db_column='kode_brng', primary_key=True)
    jml = models.FloatField(blank=True, null=True)
    harga = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip')
    tanggal = models.DateTimeField()
    keterangan = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utd_penunjang_rusak'
        unique_together = (('kode_brng', 'nip', 'tanggal'),)


class UtdPenyerahanDarah(models.Model):
    no_penyerahan = models.CharField(primary_key=True, max_length=17)
    tanggal = models.DateField(blank=True, null=True)
    dinas = models.CharField(max_length=5, blank=True, null=True)
    nip_cross = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip_cross', blank=True, null=True)
    keterangan = models.CharField(max_length=40, blank=True, null=True)
    status = models.CharField(max_length=13, blank=True, null=True)
    kd_rek = models.ForeignKey('keuangan.Rekening', on_delete=models.DO_NOTHING, db_column='kd_rek', blank=True, null=True)
    pengambil_darah = models.CharField(max_length=70, blank=True, null=True)
    alamat_pengambil_darah = models.CharField(max_length=120, blank=True, null=True)
    nip_pj = models.CharField(max_length=20, blank=True, null=True)
    besarppn = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utd_penyerahan_darah'


class UtdPenyerahanDarahDetail(models.Model):
    no_penyerahan = models.OneToOneField(UtdPenyerahanDarah, on_delete=models.DO_NOTHING, db_column='no_penyerahan', primary_key=True)
    no_kantong = models.ForeignKey('UtdStokDarah', on_delete=models.DO_NOTHING, db_column='no_kantong')
    jasa_sarana = models.FloatField(blank=True, null=True)
    paket_bhp = models.FloatField(blank=True, null=True)
    kso = models.FloatField(blank=True, null=True)
    manajemen = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utd_penyerahan_darah_detail'
        unique_together = (('no_penyerahan', 'no_kantong'),)


class UtdStokDarah(models.Model):
    no_kantong = models.CharField(primary_key=True, max_length=20)
    kode_komponen = models.ForeignKey(UtdKomponenDarah, on_delete=models.DO_NOTHING, db_column='kode_komponen', blank=True, null=True)
    golongan_darah = models.CharField(max_length=2, blank=True, null=True)
    resus = models.CharField(max_length=3, blank=True, null=True)
    tanggal_aftap = models.DateField(blank=True, null=True)
    tanggal_kadaluarsa = models.DateField(blank=True, null=True)
    asal_darah = models.CharField(max_length=16, blank=True, null=True)
    status = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utd_stok_darah'


class UtdStokMedis(models.Model):
    kode_brng = models.OneToOneField('farmasi.Databarang', on_delete=models.DO_NOTHING, db_column='kode_brng', primary_key=True)
    stok = models.FloatField(blank=True, null=True)
    hargaterakhir = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utd_stok_medis'


class UtdStokPenunjang(models.Model):
    kode_brng = models.OneToOneField('aset.Ipsrsbarang', on_delete=models.DO_NOTHING, db_column='kode_brng', primary_key=True)
    stok = models.FloatField(blank=True, null=True)
    hargaterakhir = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utd_stok_penunjang'


