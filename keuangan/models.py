from django.db import models

# Create your models here.

class SetModalPayment(models.Model):
    modal_awal = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'set_modal_payment'


class Rekening(models.Model):
    kd_rek = models.CharField(primary_key=True, max_length=15)
    nm_rek = models.CharField(max_length=100, blank=True, null=True)
    tipe = models.CharField(max_length=1, blank=True, null=True)
    balance = models.CharField(max_length=1, blank=True, null=True)
    level = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rekening'


class Rekeningtahun(models.Model):
    thn = models.TextField(primary_key=True)  # This field type is a guess.
    kd_rek = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='kd_rek')
    saldo_awal = models.FloatField()

    class Meta:
        managed = False
        db_table = 'rekeningtahun'
        unique_together = (('thn', 'kd_rek'),)


class AkunBayar(models.Model):
    nama_bayar = models.CharField(primary_key=True, max_length=50)
    kd_rek = models.ForeignKey('Rekening', on_delete=models.DO_NOTHING, db_column='kd_rek', blank=True, null=True)
    ppn = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'akun_bayar'


class Deposit(models.Model):
    no_deposit = models.CharField(primary_key=True, max_length=17)
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat')
    tgl_deposit = models.DateTimeField()
    nama_bayar = models.ForeignKey(AkunBayar, on_delete=models.DO_NOTHING, db_column='nama_bayar')
    besarppn = models.FloatField()
    besar_deposit = models.FloatField(blank=True, null=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip')

    class Meta:
        managed = False
        db_table = 'deposit'


class RiwayatNaikGaji(models.Model):
    id = models.OneToOneField('pegawai.Pegawai', on_delete=models.DO_NOTHING, db_column='id', primary_key=True)
    pangkatjabatan = models.CharField(max_length=50)
    gapok = models.FloatField()
    tmt_berkala = models.DateField()
    tmt_berkala_yad = models.DateField()
    no_sk = models.CharField(max_length=25)
    tgl_sk = models.DateField()
    masa_kerja = models.IntegerField()
    bulan_kerja = models.IntegerField()
    berkas = models.CharField(max_length=500)

    class Meta:
        managed = False
        db_table = 'riwayat_naik_gaji'
        unique_together = (('id', 'pangkatjabatan', 'gapok'),)
        
        
class AkunPiutang(models.Model):
    nama_bayar = models.CharField(primary_key=True, max_length=50)
    kd_rek = models.ForeignKey('Rekening', on_delete=models.DO_NOTHING, db_column='kd_rek', blank=True, null=True)
    kd_pj = models.ForeignKey('asuransi.Penjab', on_delete=models.DO_NOTHING, db_column='kd_pj', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'akun_piutang'
        unique_together = (('kd_rek', 'kd_pj'),)


class DetailPiutangPasien(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    nama_bayar = models.ForeignKey(AkunPiutang, on_delete=models.DO_NOTHING, db_column='nama_bayar')
    kd_pj = models.ForeignKey('asuransi.Penjab', on_delete=models.DO_NOTHING, db_column='kd_pj', blank=True, null=True)
    totalpiutang = models.FloatField(blank=True, null=True)
    sisapiutang = models.FloatField(blank=True, null=True)
    tgltempo = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detail_piutang_pasien'
        unique_together = (('no_rawat', 'nama_bayar'),)


class AkunPenagihanPiutang(models.Model):
    kd_rek = models.OneToOneField('Rekening', on_delete=models.DO_NOTHING, db_column='kd_rek', primary_key=True)
    nama_bank = models.CharField(max_length=70, blank=True, null=True)
    atas_nama = models.CharField(max_length=50, blank=True, null=True)
    no_rek = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'akun_penagihan_piutang'


class BayarPiutang(models.Model):
    tgl_bayar = models.DateField(primary_key=True)
    no_rkm_medis = models.ForeignKey('pasien.Pasien', on_delete=models.DO_NOTHING, db_column='no_rkm_medis')
    besar_cicilan = models.FloatField()
    catatan = models.CharField(max_length=100)
    no_rawat = models.CharField(max_length=17)
    kd_rek = models.ForeignKey('Rekening', on_delete=models.DO_NOTHING, db_column='kd_rek', related_name='kd_rek_bayar_piutang')
    kd_rek_kontra = models.ForeignKey('Rekening', on_delete=models.DO_NOTHING, db_column='kd_rek_kontra', related_name='kd_rek2_bayar_piutang')

    class Meta:
        managed = False
        db_table = 'bayar_piutang'
        unique_together = (('tgl_bayar', 'no_rkm_medis', 'no_rawat', 'kd_rek', 'kd_rek_kontra'),)


class SetAkun(models.Model):
    pengadaan_obat = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Pengadaan_Obat', blank=True, null=True, related_name='pengadaan_obat_set_akun')  # Field name made lowercase.
    pemesanan_obat = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Pemesanan_Obat', blank=True, null=True, related_name='Pemesanan_Obat_set_akun')  # Field name made lowercase.
    kontra_pemesanan_obat = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Kontra_Pemesanan_Obat', blank=True, null=True, related_name='Kontra_Pemesanan_Obat_set_akun')  # Field name made lowercase.
    bayar_pemesanan_obat = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Bayar_Pemesanan_Obat', blank=True, null=True, related_name='Bayar_Pemesanan_Obat_set_akun')  # Field name made lowercase.
    penjualan_obat = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Penjualan_Obat', blank=True, null=True, related_name='Penjualan_Obat_set_akun')  # Field name made lowercase.
    piutang_obat = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Piutang_Obat', blank=True, null=True, related_name='Piutang_Obat_set_akun')  # Field name made lowercase.
    kontra_piutang_obat = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Kontra_Piutang_Obat', blank=True, null=True, related_name='Kontra_Piutang_Obat_set_akun')  # Field name made lowercase.
    retur_ke_suplayer = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Retur_Ke_Suplayer', blank=True, null=True, related_name='Retur_Ke_Suplayer_set_akun')  # Field name made lowercase.
    kontra_retur_ke_suplayer = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Kontra_Retur_Ke_Suplayer', blank=True, null=True, related_name='Kontra_Retur_Ke_Suplayer_set_akun')  # Field name made lowercase.
    retur_dari_pembeli = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Retur_Dari_pembeli', blank=True, null=True, related_name='Retur_Dari_pembeli_set_akun')  # Field name made lowercase.
    kontra_retur_dari_pembeli = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Kontra_Retur_Dari_Pembeli', blank=True, null=True, related_name='Kontra_Retur_Dari_Pembeli_set_akun')  # Field name made lowercase.
    retur_piutang_obat = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Retur_Piutang_Obat', blank=True, null=True, related_name='Retur_Piutang_Obat_set_akun')  # Field name made lowercase.
    kontra_retur_piutang_obat = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Kontra_Retur_Piutang_Obat', blank=True, null=True, related_name='Kontra_Retur_Piutang_Obat_set_akun')  # Field name made lowercase.
    pengadaan_ipsrs = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Pengadaan_Ipsrs', blank=True, null=True, related_name='Pengadaan_Ipsrs_set_akun')  # Field name made lowercase.
    stok_keluar_ipsrs = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Stok_Keluar_Ipsrs', blank=True, null=True, related_name='Stok_Keluar_Ipsrs_set_akun')  # Field name made lowercase.
    kontra_stok_keluar_ipsrs = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Kontra_Stok_Keluar_Ipsrs', blank=True, null=True, related_name='Kontra_Stok_Keluar_Ipsrs_set_akun')  # Field name made lowercase.
    bayar_piutang_pasien = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Bayar_Piutang_Pasien', blank=True, null=True, related_name='Bayar_Piutang_Pasien_set_akun')  # Field name made lowercase.
    pengambilan_utd = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Pengambilan_Utd', blank=True, null=True, related_name='pengambilan_utd_set_akun')  # Field name made lowercase.
    kontra_pengambilan_utd = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Kontra_Pengambilan_Utd', blank=True, null=True, related_name='kontra_pengambilan_utd_set_akun')  # Field name made lowercase.
    pengambilan_penunjang_utd = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Pengambilan_Penunjang_Utd', blank=True, null=True, related_name='pengambilan_penunjang_utd_set_akun')  # Field name made lowercase.
    kontra_pengambilan_penunjang_utd = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Kontra_Pengambilan_Penunjang_Utd', blank=True, null=True, related_name='kontra_pengambilan_penunjang_utd_set_akun')  # Field name made lowercase.
    penyerahan_darah = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Penyerahan_Darah', blank=True, null=True, related_name='penyerahan_darah_set_akun')  # Field name made lowercase.
    stok_keluar_medis = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Stok_Keluar_Medis', related_name='stok_keluar_medis_set_akun')  # Field name made lowercase.
    kontra_stok_keluar_medis = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Kontra_Stok_Keluar_Medis', related_name='kontra_stok_keluar_medis_set_akun')  # Field name made lowercase.
    hpp_obat_jual_bebas = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='HPP_Obat_Jual_Bebas', blank=True, null=True, related_name='hpp_obat_jual_bebas_set_akun')  # Field name made lowercase.
    persediaan_obat_jual_bebas = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Persediaan_Obat_Jual_Bebas', blank=True, null=True, related_name='persediaan_obat_jual_bebas_set_akun')  # Field name made lowercase.
    penerimaan_nonmedis = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Penerimaan_NonMedis', related_name='penerimaan_nonmedis_set_akun')  # Field name made lowercase.
    kontra_penerimaan_nonmedis = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Kontra_Penerimaan_NonMedis', related_name='kontra_penerimaan_nonmedis_set_akun')  # Field name made lowercase.
    bayar_pemesanan_non_medis = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Bayar_Pemesanan_Non_Medis', related_name='bayar_pemesanan_non_medis_set_akun')  # Field name made lowercase.
    hibah_obat = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Hibah_Obat', related_name='hibah_obat_set_akun')  # Field name made lowercase.
    kontra_hibah_obat = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Kontra_Hibah_Obat', related_name='kontra_hibah_obat_set_akun')  # Field name made lowercase.
    penerimaan_toko = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Penerimaan_Toko', blank=True, null=True, related_name='penerimaan_toko_set_akun')  # Field name made lowercase.
    kontra_penerimaan_toko = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Kontra_Penerimaan_Toko', blank=True, null=True, related_name='kontra_penerimaan_toko_set_akun')  # Field name made lowercase.
    pengadaan_toko = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Pengadaan_Toko', related_name='pengadaan_toko_set_akun')  # Field name made lowercase.
    bayar_pemesanan_toko = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Bayar_Pemesanan_Toko', blank=True, null=True, related_name='bayar_pemesanan_toko_set_akun')  # Field name made lowercase.
    penjualan_toko = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Penjualan_Toko', blank=True, null=True, related_name='penjualan_toko_set_akun')  # Field name made lowercase.
    hpp_barang_toko = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='HPP_Barang_Toko', blank=True, null=True, related_name='hpp_barang_toko_set_akun')  # Field name made lowercase.
    persediaan_barang_toko = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Persediaan_Barang_Toko', blank=True, null=True, related_name='persediaan_barang_toko_set_akun')  # Field name made lowercase.
    piutang_toko = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Piutang_Toko', blank=True, null=True, related_name='piutang_toko_set_akun')  # Field name made lowercase.
    kontra_piutang_toko = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Kontra_Piutang_Toko', blank=True, null=True, related_name='kontra_piutang_toko_set_akun')  # Field name made lowercase.
    retur_beli_toko = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Retur_Beli_Toko', blank=True, null=True, related_name='retur_beli_toko_set_akun')  # Field name made lowercase.
    kontra_retur_beli_toko = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Kontra_Retur_Beli_Toko', blank=True, null=True, related_name='kontra_retur_beli_toko_set_akun')  # Field name made lowercase.
    retur_beli_non_medis = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Retur_Beli_Non_Medis', blank=True, null=True, related_name='retur_beli_non_medis_set_akun')  # Field name made lowercase.
    kontra_retur_beli_non_medis = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Kontra_Retur_Beli_Non_Medis', blank=True, null=True, related_name='kontra_retur_beli_non_medis_set_akun')  # Field name made lowercase.
    retur_jual_toko = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Retur_Jual_Toko', blank=True, null=True, related_name='retur_jual_toko_set_akun')  # Field name made lowercase.
    kontra_retur_jual_toko = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Kontra_Retur_Jual_Toko', blank=True, null=True, related_name='kontra_retur_jual_toko_set_akun')  # Field name made lowercase.
    retur_piutang_toko = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Retur_Piutang_Toko', blank=True, null=True, related_name='retur_piutang_toko_set_akun')  # Field name made lowercase.
    kontra_retur_piutang_toko = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Kontra_Retur_Piutang_Toko', blank=True, null=True, related_name='kontra_retur_piutang_toko_set_akun')  # Field name made lowercase.
    kerugian_klaim_bpjs_rvp = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Kerugian_Klaim_BPJS_RVP', related_name='kerugian_klaim_bpjs_rvp_set_akun')  # Field name made lowercase.
    lebih_bayar_klaim_bpjs_rvp = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Lebih_Bayar_Klaim_BPJS_RVP', related_name='lebih_bayar_klaim_bpjs_rvp_set_akun')  # Field name made lowercase.
    piutang_bpjs_rvp = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Piutang_BPJS_RVP', related_name='piutang_bpjs_rvp_set_akun')  # Field name made lowercase.
    kontra_penerimaan_asetinventaris = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Kontra_Penerimaan_AsetInventaris', related_name='kontra_penerimaan_asetinventaris_set_akun')  # Field name made lowercase.
    kontra_hibah_aset = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Kontra_Hibah_Aset', related_name='kontra_hibah_aset_set_akun')  # Field name made lowercase.
    hibah_non_medis = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Hibah_Non_Medis', related_name='hibah_non_medis_set_akun')  # Field name made lowercase.
    kontra_hibah_non_medis = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Kontra_Hibah_Non_Medis', related_name='kontra_hibah_non_medis_set_akun')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'set_akun'


class SetAkunBankbri(models.Model):
    kd_rek = models.OneToOneField(Rekening, on_delete=models.DO_NOTHING, db_column='kd_rek', primary_key=True)
    consumer_key = models.CharField(max_length=700, blank=True, null=True)
    consumer_secret = models.CharField(max_length=700, blank=True, null=True)
    institution_code = models.CharField(max_length=700, blank=True, null=True)
    briva_no = models.CharField(max_length=700, blank=True, null=True)
    urlapi = models.CharField(max_length=700)

    class Meta:
        managed = False
        db_table = 'set_akun_bankbri'


class SetAkunBankjateng(models.Model):
    kd_rek = models.OneToOneField(Rekening, on_delete=models.DO_NOTHING, db_column='kd_rek', primary_key=True)
    usere = models.CharField(max_length=700, blank=True, null=True)
    passworde = models.CharField(max_length=700, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'set_akun_bankjateng'
        unique_together = (('usere', 'passworde'),)


class SetAkunRalan(models.Model):
    suspen_piutang_tindakan_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='suspen_piutang_tindakan_ralan_set_akun_ralan', db_column='Suspen_Piutang_Tindakan_Ralan')  # Field name made lowercase.
    tindakan_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Tindakan_Ralan', related_name='tindakan_ralan_set_akun_ralan', blank=True, null=True)  # Field name made lowercase.
    beban_jasa_medik_dokter_tindakan_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='beban_jasa_medik_dokter_tindakan_ralan_set_akun_ralan', db_column='Beban_Jasa_Medik_Dokter_Tindakan_Ralan', blank=True, null=True)  # Field name made lowercase.
    utang_jasa_medik_dokter_tindakan_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='utang_jasa_medik_dokter_tindakan_ralan_set_akun_ralan', db_column='Utang_Jasa_Medik_Dokter_Tindakan_Ralan', blank=True, null=True)  # Field name made lowercase.
    beban_jasa_medik_paramedis_tindakan_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='beban_jasa_medik_paramedis_tindakan_ralan_set_akun_ralan', db_column='Beban_Jasa_Medik_Paramedis_Tindakan_Ralan', blank=True, null=True)  # Field name made lowercase.
    utang_jasa_medik_paramedis_tindakan_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='utang_jasa_medik_paramedis_tindakan_ralan_set_akun_ralan', db_column='Utang_Jasa_Medik_Paramedis_Tindakan_Ralan', blank=True, null=True)  # Field name made lowercase.
    beban_kso_tindakan_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='beban_kso_tindakan_ralan_set_akun_ralan', db_column='Beban_KSO_Tindakan_Ralan')  # Field name made lowercase.
    utang_kso_tindakan_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='utang_kso_tindakan_ralan_set_akun_ralan', db_column='Utang_KSO_Tindakan_Ralan')  # Field name made lowercase.
    beban_jasa_sarana_tindakan_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='beban_jasa_sarana_tindakan_ralan_set_akun_ralan', db_column='Beban_Jasa_Sarana_Tindakan_Ralan', blank=True, null=True)  # Field name made lowercase.
    utang_jasa_sarana_tindakan_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='utang_jasa_sarana_tindakan_ralan_set_akun_ralan', db_column='Utang_Jasa_Sarana_Tindakan_Ralan', blank=True, null=True)  # Field name made lowercase.
    hpp_bhp_tindakan_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='hpp_bhp_tindakan_ralan_set_akun_ralan', db_column='HPP_BHP_Tindakan_Ralan', blank=True, null=True)  # Field name made lowercase.
    persediaan_bhp_tindakan_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='persediaan_bhp_tindakan_ralan_set_akun_ralan', db_column='Persediaan_BHP_Tindakan_Ralan', blank=True, null=True)  # Field name made lowercase.
    beban_jasa_menejemen_tindakan_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='beban_jasa_menejemen_tindakan_ralan_set_akun_ralan', db_column='Beban_Jasa_Menejemen_Tindakan_Ralan', blank=True, null=True)  # Field name made lowercase.
    utang_jasa_menejemen_tindakan_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='utang_jasa_menejemen_tindakan_ralan_set_akun_ralan', db_column='Utang_Jasa_Menejemen_Tindakan_Ralan', blank=True, null=True)  # Field name made lowercase.
    suspen_piutang_laborat_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='suspen_piutang_laborat_ralan_set_akun_ralan', db_column='Suspen_Piutang_Laborat_Ralan')  # Field name made lowercase.
    laborat_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='laborat_ralan_set_akun_ralan', db_column='Laborat_Ralan', blank=True, null=True)  # Field name made lowercase.
    beban_jasa_medik_dokter_laborat_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='beban_jasa_medik_dokter_laborat_ralan_set_akun_ralan', db_column='Beban_Jasa_Medik_Dokter_Laborat_Ralan', blank=True, null=True)  # Field name made lowercase.
    utang_jasa_medik_dokter_laborat_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='utang_jasa_medik_dokter_laborat_ralan_set_akun_ralan', db_column='Utang_Jasa_Medik_Dokter_Laborat_Ralan', blank=True, null=True)  # Field name made lowercase.
    beban_jasa_medik_petugas_laborat_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='beban_jasa_medik_petugas_laborat_ralan_set_akun_ralan', db_column='Beban_Jasa_Medik_Petugas_Laborat_Ralan', blank=True, null=True)  # Field name made lowercase.
    utang_jasa_medik_petugas_laborat_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='utang_jasa_medik_petugas_laborat_ralan_set_akun_ralan', db_column='Utang_Jasa_Medik_Petugas_Laborat_Ralan', blank=True, null=True)  # Field name made lowercase.
    beban_kso_laborat_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='beban_kso_laborat_ralan_set_akun_ralan', db_column='Beban_Kso_Laborat_Ralan', blank=True, null=True)  # Field name made lowercase.
    utang_kso_laborat_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='utang_kso_laborat_ralan_set_akun_ralan', db_column='Utang_Kso_Laborat_Ralan', blank=True, null=True)  # Field name made lowercase.
    hpp_persediaan_laborat_rawat_jalan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='hpp_persediaan_laborat_rawat_jalan_set_akun_ralan', db_column='HPP_Persediaan_Laborat_Rawat_Jalan', blank=True, null=True)  # Field name made lowercase.
    persediaan_bhp_laborat_rawat_jalan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='persediaan_bhp_laborat_rawat_jalan_set_akun_ralan', db_column='Persediaan_BHP_Laborat_Rawat_Jalan', blank=True, null=True)  # Field name made lowercase.
    beban_jasa_sarana_laborat_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='beban_jasa_sarana_laborat_ralan_set_akun_ralan', db_column='Beban_Jasa_Sarana_Laborat_Ralan')  # Field name made lowercase.
    utang_jasa_sarana_laborat_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='utang_jasa_sarana_laborat_ralan_set_akun_ralan', db_column='Utang_Jasa_Sarana_Laborat_Ralan')  # Field name made lowercase.
    beban_jasa_perujuk_laborat_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='beban_jasa_perujuk_laborat_ralan_set_akun_ralan', db_column='Beban_Jasa_Perujuk_Laborat_Ralan')  # Field name made lowercase.
    utang_jasa_perujuk_laborat_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='utang_jasa_perujuk_laborat_ralan_set_akun_ralan', db_column='Utang_Jasa_Perujuk_Laborat_Ralan')  # Field name made lowercase.
    beban_jasa_menejemen_laborat_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='beban_jasa_menejemen_laborat_ralan_set_akun_ralan', db_column='Beban_Jasa_Menejemen_Laborat_Ralan')  # Field name made lowercase.
    utang_jasa_menejemen_laborat_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='utang_jasa_menejemen_laborat_ralan_set_akun_ralan', db_column='Utang_Jasa_Menejemen_Laborat_Ralan')  # Field name made lowercase.
    suspen_piutang_radiologi_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='suspen_piutang_radiologi_ralan_set_akun_ralan', db_column='Suspen_Piutang_Radiologi_Ralan')  # Field name made lowercase.
    radiologi_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='radiologi_ralan_set_akun_ralan', db_column='Radiologi_Ralan', blank=True, null=True)  # Field name made lowercase.
    beban_jasa_medik_dokter_radiologi_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='beban_jasa_medik_dokter_radiologi_ralan_set_akun_ralan', db_column='Beban_Jasa_Medik_Dokter_Radiologi_Ralan')  # Field name made lowercase.
    utang_jasa_medik_dokter_radiologi_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='utang_jasa_medik_dokter_radiologi_ralan_set_akun_ralan', db_column='Utang_Jasa_Medik_Dokter_Radiologi_Ralan')  # Field name made lowercase.
    beban_jasa_medik_petugas_radiologi_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='beban_jasa_medik_petugas_radiologi_ralan_set_akun_ralan', db_column='Beban_Jasa_Medik_Petugas_Radiologi_Ralan')  # Field name made lowercase.
    utang_jasa_medik_petugas_radiologi_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='utang_jasa_medik_petugas_radiologi_ralan_set_akun_ralan', db_column='Utang_Jasa_Medik_Petugas_Radiologi_Ralan')  # Field name made lowercase.
    beban_kso_radiologi_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='beban_kso_radiologi_ralan_set_akun_ralan', db_column='Beban_Kso_Radiologi_Ralan')  # Field name made lowercase.
    utang_kso_radiologi_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='utang_kso_radiologi_ralan_set_akun_ralan', db_column='Utang_Kso_Radiologi_Ralan')  # Field name made lowercase.
    hpp_persediaan_radiologi_rawat_jalan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='hpp_persediaan_radiologi_rawat_jalan_set_akun_ralan', db_column='HPP_Persediaan_Radiologi_Rawat_Jalan')  # Field name made lowercase.
    persediaan_bhp_radiologi_rawat_jalan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='persediaan_bhp_radiologi_rawat_jalan_set_akun_ralan', db_column='Persediaan_BHP_Radiologi_Rawat_Jalan')  # Field name made lowercase.
    beban_jasa_sarana_radiologi_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='beban_jasa_sarana_radiologi_ralan_set_akun_ralan', db_column='Beban_Jasa_Sarana_Radiologi_Ralan')  # Field name made lowercase.
    utang_jasa_sarana_radiologi_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='utang_jasa_sarana_radiologi_ralan_set_akun_ralan', db_column='Utang_Jasa_Sarana_Radiologi_Ralan')  # Field name made lowercase.
    beban_jasa_perujuk_radiologi_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='beban_jasa_perujuk_radiologi_ralan_set_akun_ralan', db_column='Beban_Jasa_Perujuk_Radiologi_Ralan')  # Field name made lowercase.
    utang_jasa_perujuk_radiologi_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='utang_jasa_perujuk_radiologi_ralan_set_akun_ralan', db_column='Utang_Jasa_Perujuk_Radiologi_Ralan')  # Field name made lowercase.
    beban_jasa_menejemen_radiologi_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='beban_jasa_menejemen_radiologi_ralan_set_akun_ralan', db_column='Beban_Jasa_Menejemen_Radiologi_Ralan')  # Field name made lowercase.
    utang_jasa_menejemen_radiologi_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='utang_jasa_menejemen_radiologi_ralan_set_akun_ralan', db_column='Utang_Jasa_Menejemen_Radiologi_Ralan')  # Field name made lowercase.
    suspen_piutang_obat_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='suspen_piutang_obat_ralan_set_akun_ralan', db_column='Suspen_Piutang_Obat_Ralan')  # Field name made lowercase.
    obat_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='obat_ralan_set_akun_ralan', db_column='Obat_Ralan', blank=True, null=True)  # Field name made lowercase.
    hpp_obat_rawat_jalan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='hpp_obat_rawat_jalan_set_akun_ralan', db_column='HPP_Obat_Rawat_Jalan')  # Field name made lowercase.
    persediaan_obat_rawat_jalan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='persediaan_obat_rawat_jalan_set_akun_ralan', db_column='Persediaan_Obat_Rawat_Jalan')  # Field name made lowercase.
    registrasi_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='registrasi_ralan_set_akun_ralan', db_column='Registrasi_Ralan', blank=True, null=True)  # Field name made lowercase.
    suspen_piutang_operasi_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='suspen_piutang_operasi_ralan_set_akun_ralan', db_column='Suspen_Piutang_Operasi_Ralan')  # Field name made lowercase.
    operasi_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='operasi_ralan_set_akun_ralan', db_column='Operasi_Ralan', blank=True, null=True)  # Field name made lowercase.
    beban_jasa_medik_dokter_operasi_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='beban_jasa_medik_dokter_operasi_ralan_set_akun_ralan', db_column='Beban_Jasa_Medik_Dokter_Operasi_Ralan')  # Field name made lowercase.
    utang_jasa_medik_dokter_operasi_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='utang_jasa_medik_dokter_operasi_ralan_set_akun_ralan', db_column='Utang_Jasa_Medik_Dokter_Operasi_Ralan')  # Field name made lowercase.
    beban_jasa_medik_paramedis_operasi_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='beban_jasa_medik_paramedis_operasi_ralan_set_akun_ralan', db_column='Beban_Jasa_Medik_Paramedis_Operasi_Ralan')  # Field name made lowercase.
    utang_jasa_medik_paramedis_operasi_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='utang_jasa_medik_paramedis_operasi_ralan_set_akun_ralan', db_column='Utang_Jasa_Medik_Paramedis_Operasi_Ralan')  # Field name made lowercase.
    hpp_obat_operasi_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='hpp_obat_operasi_ralan_set_akun_ralan', db_column='HPP_Obat_Operasi_Ralan')  # Field name made lowercase.
    persediaan_obat_kamar_operasi_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='persediaan_obat_kamar_operasi_ralan_set_akun_ralan', db_column='Persediaan_Obat_Kamar_Operasi_Ralan')  # Field name made lowercase.
    tambahan_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='tambahan_ralan_set_akun_ralan', db_column='Tambahan_Ralan', blank=True, null=True)  # Field name made lowercase.
    potongan_ralan = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='potongan_ralan_set_akun_ralan', db_column='Potongan_Ralan', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'set_akun_ralan'


class SetAkunRanap(models.Model):
    suspen_piutang_tindakan_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Suspen_Piutang_Tindakan_Ranap', related_name='sptr_set_akun_ranap')  # Field name made lowercase.
    tindakan_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Tindakan_Ranap', blank=True, null=True, related_name='tr_set_akun_ranap')  # Field name made lowercase.
    beban_jasa_medik_dokter_tindakan_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Beban_Jasa_Medik_Dokter_Tindakan_Ranap', related_name='bjmdtr_set_akun_ranap')  # Field name made lowercase.
    utang_jasa_medik_dokter_tindakan_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Utang_Jasa_Medik_Dokter_Tindakan_Ranap', related_name='ujmdtr_set_akun_ranap')  # Field name made lowercase.
    beban_jasa_medik_paramedis_tindakan_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Beban_Jasa_Medik_Paramedis_Tindakan_Ranap', related_name='bjmptr_set_akun_ranap')  # Field name made lowercase.
    utang_jasa_medik_paramedis_tindakan_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Utang_Jasa_Medik_Paramedis_Tindakan_Ranap', related_name='ujmptr_set_akun_ranap')  # Field name made lowercase.
    beban_kso_tindakan_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Beban_KSO_Tindakan_Ranap', related_name='bktr_set_akun_ranap')  # Field name made lowercase.
    utang_kso_tindakan_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Utang_KSO_Tindakan_Ranap', related_name='uktr_set_akun_ranap')  # Field name made lowercase.
    beban_jasa_sarana_tindakan_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Beban_Jasa_Sarana_Tindakan_Ranap', related_name='bjstr_set_akun_ranap')  # Field name made lowercase.
    utang_jasa_sarana_tindakan_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Utang_Jasa_Sarana_Tindakan_Ranap', related_name='ujstr_set_akun_ranap')  # Field name made lowercase.
    beban_jasa_menejemen_tindakan_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Beban_Jasa_Menejemen_Tindakan_Ranap', related_name='bjmtr_set_akun_ranap')  # Field name made lowercase.
    utang_jasa_menejemen_tindakan_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Utang_Jasa_Menejemen_Tindakan_Ranap', related_name='_set_akun_ranap')  # Field name made lowercase.
    hpp_bhp_tindakan_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='hpp_bhp_tindakan_ranap_set_akun_ranap', db_column='HPP_BHP_Tindakan_Ranap')  # Field name made lowercase.
    persediaan_bhp_tindakan_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='persediaan_bhp_tindakan_ranap_set_akun_ranap', db_column='Persediaan_BHP_Tindakan_Ranap')  # Field name made lowercase.
    suspen_piutang_laborat_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='suspen_piutang_laborat_ranap_set_akun_ranap', db_column='Suspen_Piutang_Laborat_Ranap')  # Field name made lowercase.
    laborat_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='laborat_ranap_set_akun_ranap', db_column='Laborat_Ranap', blank=True, null=True)  # Field name made lowercase.
    beban_jasa_medik_dokter_laborat_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='beban_jasa_medik_dokter_laborat_ranap_set_akun_ranap', db_column='Beban_Jasa_Medik_Dokter_Laborat_Ranap')  # Field name made lowercase.
    utang_jasa_medik_dokter_laborat_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='utang_jasa_medik_dokter_laborat_ranap_set_akun_ranap', db_column='Utang_Jasa_Medik_Dokter_Laborat_Ranap')  # Field name made lowercase.
    beban_jasa_medik_petugas_laborat_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='beban_jasa_medik_petugas_laborat_ranap_set_akun_ranap', db_column='Beban_Jasa_Medik_Petugas_Laborat_Ranap')  # Field name made lowercase.
    utang_jasa_medik_petugas_laborat_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='utang_jasa_medik_petugas_laborat_ranap_set_akun_ranap', db_column='Utang_Jasa_Medik_Petugas_Laborat_Ranap')  # Field name made lowercase.
    beban_kso_laborat_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='beban_kso_laborat_ranap_set_akun_ranap', db_column='Beban_Kso_Laborat_Ranap')  # Field name made lowercase.
    utang_kso_laborat_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='utang_kso_laborat_ranap_set_akun_ranap', db_column='Utang_Kso_Laborat_Ranap')  # Field name made lowercase.
    hpp_persediaan_laborat_rawat_inap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='hpp_persediaan_laborat_rawat_inap_set_akun_ranap', db_column='HPP_Persediaan_Laborat_Rawat_inap')  # Field name made lowercase.
    persediaan_bhp_laborat_rawat_inap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='persediaan_bhp_laborat_rawat_inap_set_akun_ranap', db_column='Persediaan_BHP_Laborat_Rawat_Inap')  # Field name made lowercase.
    beban_jasa_sarana_laborat_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='beban_jasa_sarana_laborat_ranap_set_akun_ranap', db_column='Beban_Jasa_Sarana_Laborat_Ranap')  # Field name made lowercase.
    utang_jasa_sarana_laborat_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='utang_jasa_sarana_laborat_ranap_set_akun_ranap', db_column='Utang_Jasa_Sarana_Laborat_Ranap')  # Field name made lowercase.
    beban_jasa_perujuk_laborat_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='beban_jasa_perujuk_laborat_ranap_set_akun_ranap', db_column='Beban_Jasa_Perujuk_Laborat_Ranap')  # Field name made lowercase.
    utang_jasa_perujuk_laborat_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='utang_jasa_perujuk_laborat_ranap_set_akun_ranap', db_column='Utang_Jasa_Perujuk_Laborat_Ranap')  # Field name made lowercase.
    beban_jasa_menejemen_laborat_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='beban_jasa_menejemen_laborat_ranap_set_akun_ranap', db_column='Beban_Jasa_Menejemen_Laborat_Ranap')  # Field name made lowercase.
    utang_jasa_menejemen_laborat_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='utang_jasa_menejemen_laborat_ranap_set_akun_ranap', db_column='Utang_Jasa_Menejemen_Laborat_Ranap')  # Field name made lowercase.
    suspen_piutang_radiologi_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='suspen_piutang_radiologi_ranap_set_akun_ranap', db_column='Suspen_Piutang_Radiologi_Ranap')  # Field name made lowercase.
    radiologi_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='radiologi_ranap_set_akun_ranap', db_column='Radiologi_Ranap', blank=True, null=True)  # Field name made lowercase.
    beban_jasa_medik_dokter_radiologi_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='beban_jasa_medik_dokter_radiologi_ranap_set_akun_ranap', db_column='Beban_Jasa_Medik_Dokter_Radiologi_Ranap')  # Field name made lowercase.
    utang_jasa_medik_dokter_radiologi_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='utang_jasa_medik_dokter_radiologi_ranap_set_akun_ranap', db_column='Utang_Jasa_Medik_Dokter_Radiologi_Ranap')  # Field name made lowercase.
    beban_jasa_medik_petugas_radiologi_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='beban_jasa_medik_petugas_radiologi_ranap_set_akun_ranap', db_column='Beban_Jasa_Medik_Petugas_Radiologi_Ranap')  # Field name made lowercase.
    utang_jasa_medik_petugas_radiologi_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='utang_jasa_medik_petugas_radiologi_ranap_set_akun_ranap', db_column='Utang_Jasa_Medik_Petugas_Radiologi_Ranap')  # Field name made lowercase.
    beban_kso_radiologi_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='beban_kso_radiologi_ranap_set_akun_ranap', db_column='Beban_Kso_Radiologi_Ranap')  # Field name made lowercase.
    utang_kso_radiologi_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='utang_kso_radiologi_ranap_set_akun_ranap', db_column='Utang_Kso_Radiologi_Ranap')  # Field name made lowercase.
    hpp_persediaan_radiologi_rawat_inap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='hpp_persediaan_radiologi_rawat_inap_set_akun_ranap', db_column='HPP_Persediaan_Radiologi_Rawat_Inap')  # Field name made lowercase.
    persediaan_bhp_radiologi_rawat_inap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='persediaan_bhp_radiologi_rawat_inap_set_akun_ranap', db_column='Persediaan_BHP_Radiologi_Rawat_Inap')  # Field name made lowercase.
    beban_jasa_sarana_radiologi_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='beban_jasa_sarana_radiologi_ranap_set_akun_ranap', db_column='Beban_Jasa_Sarana_Radiologi_Ranap')  # Field name made lowercase.
    utang_jasa_sarana_radiologi_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='utang_jasa_sarana_radiologi_ranap_set_akun_ranap', db_column='Utang_Jasa_Sarana_Radiologi_Ranap')  # Field name made lowercase.
    beban_jasa_perujuk_radiologi_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='beban_jasa_perujuk_radiologi_ranap_set_akun_ranap', db_column='Beban_Jasa_Perujuk_Radiologi_Ranap')  # Field name made lowercase.
    utang_jasa_perujuk_radiologi_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='utang_jasa_perujuk_radiologi_ranap_set_akun_ranap', db_column='Utang_Jasa_Perujuk_Radiologi_Ranap')  # Field name made lowercase.
    beban_jasa_menejemen_radiologi_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='beban_jasa_menejemen_radiologi_ranap_set_akun_ranap', db_column='Beban_Jasa_Menejemen_Radiologi_Ranap')  # Field name made lowercase.
    utang_jasa_menejemen_radiologi_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='utang_jasa_menejemen_radiologi_ranap_set_akun_ranap', db_column='Utang_Jasa_Menejemen_Radiologi_Ranap')  # Field name made lowercase.
    suspen_piutang_obat_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='suspen_piutang_obat_ranap_set_akun_ranap', db_column='Suspen_Piutang_Obat_Ranap')  # Field name made lowercase.
    obat_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='obat_ranap_set_akun_ranap', db_column='Obat_Ranap', blank=True, null=True)  # Field name made lowercase.
    hpp_obat_rawat_inap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='hpp_obat_rawat_inap_set_akun_ranap', db_column='HPP_Obat_Rawat_Inap')  # Field name made lowercase.
    persediaan_obat_rawat_inap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='persediaan_obat_rawat_inap_set_akun_ranap', db_column='Persediaan_Obat_Rawat_Inap')  # Field name made lowercase.
    registrasi_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='registrasi_ranap_set_akun_ranap', db_column='Registrasi_Ranap', blank=True, null=True)  # Field name made lowercase.
    service_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='service_ranap_set_akun_ranap', db_column='Service_Ranap', blank=True, null=True)  # Field name made lowercase.
    tambahan_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='tambahan_ranap_set_akun_ranap', db_column='Tambahan_Ranap', blank=True, null=True)  # Field name made lowercase.
    potongan_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='potongan_ranap_set_akun_ranap', db_column='Potongan_Ranap', blank=True, null=True)  # Field name made lowercase.
    retur_obat_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='retur_obat_ranap_set_akun_ranap', db_column='Retur_Obat_Ranap', blank=True, null=True)  # Field name made lowercase.
    resep_pulang_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='resep_pulang_ranap_set_akun_ranap', db_column='Resep_Pulang_Ranap', blank=True, null=True)  # Field name made lowercase.
    kamar_inap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='kamar_inap_set_akun_ranap', db_column='Kamar_Inap', blank=True, null=True)  # Field name made lowercase.
    suspen_piutang_operasi_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='suspen_piutang_operasi_ranap_set_akun_ranap', db_column='Suspen_Piutang_Operasi_Ranap')  # Field name made lowercase.
    operasi_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='operasi_ranap_set_akun_ranap', db_column='Operasi_Ranap', blank=True, null=True)  # Field name made lowercase.
    beban_jasa_medik_dokter_operasi_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='beban_jasa_medik_dokter_operasi_ranap_set_akun_ranap', db_column='Beban_Jasa_Medik_Dokter_Operasi_Ranap')  # Field name made lowercase.
    utang_jasa_medik_dokter_operasi_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='utang_jasa_medik_dokter_operasi_ranap_set_akun_ranap', db_column='Utang_Jasa_Medik_Dokter_Operasi_Ranap')  # Field name made lowercase.
    beban_jasa_medik_paramedis_operasi_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='beban_jasa_medik_paramedis_operasi_ranap_set_akun_ranap', db_column='Beban_Jasa_Medik_Paramedis_Operasi_Ranap')  # Field name made lowercase.
    utang_jasa_medik_paramedis_operasi_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='utang_jasa_medik_paramedis_operasi_ranap_set_akun_ranap', db_column='Utang_Jasa_Medik_Paramedis_Operasi_Ranap')  # Field name made lowercase.
    hpp_obat_operasi_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, related_name='hpp_obat_operasi_ranap_set_akun_ranap', db_column='HPP_Obat_Operasi_Ranap')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'set_akun_ranap'


class SetAkunRanap2(models.Model):
    persediaan_obat_kamar_operasi_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Persediaan_Obat_Kamar_Operasi_Ranap', related_name='persediaan_obat_setakun_ranap2')  # Field name made lowercase.
    harian_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Harian_Ranap', blank=True, null=True, related_name='harian_ranap_set_akun_ranap2')  # Field name made lowercase.
    uang_muka_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Uang_Muka_Ranap', blank=True, null=True, related_name='uang_muka_ranap_set_akun_ranap2')  # Field name made lowercase.
    piutang_pasien_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Piutang_Pasien_Ranap', blank=True, null=True, related_name='piutang_pasien_ranap_set_akun_ranap2')  # Field name made lowercase.
    sisa_uang_muka_ranap = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='Sisa_Uang_Muka_Ranap', related_name='sisa_uang_muka_ranap_set_akun_ranap2')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'set_akun_ranap2'


class Piutang(models.Model):
    nota_piutang = models.CharField(primary_key=True, max_length=20)
    tgl_piutang = models.DateField(blank=True, null=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    no_rkm_medis = models.ForeignKey('pasien.Pasien', on_delete=models.DO_NOTHING, db_column='no_rkm_medis', blank=True, null=True)
    nm_pasien = models.CharField(max_length=50, blank=True, null=True)
    catatan = models.CharField(max_length=40, blank=True, null=True)
    jns_jual = models.CharField(max_length=11, blank=True, null=True)
    ongkir = models.FloatField(blank=True, null=True)
    uangmuka = models.FloatField(blank=True, null=True)
    sisapiutang = models.FloatField()
    status = models.CharField(max_length=5, blank=True, null=True)
    tgltempo = models.DateField()
    kd_bangsal = models.ForeignKey('bangsal.Bangsal', on_delete=models.DO_NOTHING, db_column='kd_bangsal')

    class Meta:
        managed = False
        db_table = 'piutang'


class Detailpiutang(models.Model):
    nota_piutang = models.ForeignKey('Piutang', on_delete=models.DO_NOTHING, db_column='nota_piutang')
    kode_brng = models.ForeignKey('farmasi.Databarang', on_delete=models.DO_NOTHING, db_column='kode_brng')
    kode_sat = models.ForeignKey('data.Kodesatuan', on_delete=models.DO_NOTHING, db_column='kode_sat', blank=True, null=True)
    h_jual = models.FloatField(blank=True, null=True)
    h_beli = models.FloatField(blank=True, null=True)
    jumlah = models.FloatField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    dis = models.FloatField(blank=True, null=True)
    bsr_dis = models.FloatField(blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    no_batch = models.CharField(max_length=20)
    no_faktur = models.CharField(max_length=20)
    aturan_pakai = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'detailpiutang'


class Returpiutang(models.Model):
    no_retur_piutang = models.CharField(primary_key=True, max_length=20)
    tgl_retur = models.DateField(blank=True, null=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    no_rkm_medis = models.ForeignKey('pasien.Pasien', on_delete=models.DO_NOTHING, db_column='no_rkm_medis')
    kd_bangsal = models.ForeignKey('bangsal.Bangsal', on_delete=models.DO_NOTHING, db_column='kd_bangsal')

    class Meta:
        managed = False
        db_table = 'returpiutang'
        

class Detreturpiutang(models.Model):
    no_retur_piutang = models.ForeignKey('Returpiutang', on_delete=models.DO_NOTHING, db_column='no_retur_piutang')
    nota_piutang = models.CharField(max_length=20)
    kode_brng = models.ForeignKey('farmasi.Databarang', on_delete=models.DO_NOTHING, db_column='kode_brng')
    kode_sat = models.ForeignKey('data.Kodesatuan', on_delete=models.DO_NOTHING, db_column='kode_sat', blank=True, null=True)
    jml_piutang = models.FloatField(blank=True, null=True)
    h_piutang = models.FloatField(blank=True, null=True)
    jml_retur = models.FloatField(blank=True, null=True)
    h_retur = models.FloatField(blank=True, null=True)
    subtotal = models.FloatField(blank=True, null=True)
    no_batch = models.CharField(max_length=20)
    no_faktur = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'detreturpiutang'
        
        
class PiutangPasien(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    tgl_piutang = models.DateField(blank=True, null=True)
    no_rkm_medis = models.ForeignKey('pasien.Pasien', on_delete=models.DO_NOTHING, db_column='no_rkm_medis', blank=True, null=True)
    status = models.CharField(max_length=11)
    totalpiutang = models.FloatField(blank=True, null=True)
    uangmuka = models.FloatField(blank=True, null=True)
    sisapiutang = models.FloatField()
    tgltempo = models.DateField()

    class Meta:
        managed = False
        db_table = 'piutang_pasien'


class SetHargaKamar(models.Model):
    kd_kamar = models.OneToOneField('bangsal.Kamar', on_delete=models.DO_NOTHING, db_column='kd_kamar', primary_key=True)
    kd_pj = models.ForeignKey('asuransi.Penjab', on_delete=models.DO_NOTHING, db_column='kd_pj')
    tarif = models.FloatField()

    class Meta:
        managed = False
        db_table = 'set_harga_kamar'
        unique_together = (('kd_kamar', 'kd_pj'),)
        
        
class SetTarif(models.Model):
    poli_ralan = models.CharField(max_length=3)
    cara_bayar_ralan = models.CharField(max_length=3)
    ruang_ranap = models.CharField(max_length=3)
    cara_bayar_ranap = models.CharField(max_length=3)
    cara_bayar_lab = models.CharField(max_length=3)
    cara_bayar_radiologi = models.CharField(max_length=3)
    cara_bayar_operasi = models.CharField(max_length=3, blank=True, null=True)
    kelas_ranap = models.CharField(max_length=3)
    kelas_lab = models.CharField(max_length=3)
    kelas_radiologi = models.CharField(max_length=3)
    kelas_operasi = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'set_tarif'


class SetTarifOnline(models.Model):
    kd_jenis_prw = models.OneToOneField('ralan.JnsPerawatan', on_delete=models.DO_NOTHING, db_column='kd_jenis_prw', primary_key=True)

    class Meta:
        managed = False
        db_table = 'set_tarif_online'


class SetNota(models.Model):
    notaralan = models.CharField(max_length=11)
    kwitansiralan = models.CharField(max_length=11)
    nota1ranap = models.CharField(max_length=11)
    nota2ranap = models.CharField(max_length=11)
    kwitansiranap = models.CharField(max_length=11)
    notaapotek = models.CharField(max_length=11)
    notalabrad = models.CharField(max_length=11)
    notatoko = models.CharField(max_length=11)
    cetaknotasimpanralan = models.CharField(max_length=3)
    cetaknotasimpanranap = models.CharField(max_length=3)
    rinciandokterralan = models.CharField(max_length=3)
    rinciandokterranap = models.CharField(max_length=3)
    centangdokterralan = models.CharField(max_length=3)
    centangdokterranap = models.CharField(max_length=3)
    tampilkan_administrasi_di_billingranap = models.CharField(max_length=3)
    rincianoperasi = models.CharField(max_length=3, blank=True, null=True)
    tampilkan_ppnobat_ralan = models.CharField(max_length=3, blank=True, null=True)
    tampilkan_ppnobat_ranap = models.CharField(max_length=3, blank=True, null=True)
    tampilkan_tombol_nota_ralan = models.CharField(max_length=3, blank=True, null=True)
    tampilkan_tombol_nota_ranap = models.CharField(max_length=3, blank=True, null=True)
    verifikasi_penjualan_di_kasir = models.CharField(max_length=3, blank=True, null=True)
    verifikasi_penyerahan_darah_di_kasir = models.CharField(max_length=3, blank=True, null=True)
    cetaknotasimpanpenjualan = models.CharField(max_length=3, blank=True, null=True)
    tampilkan_tombol_nota_penjualan = models.CharField(max_length=3, blank=True, null=True)
    centangobatralan = models.CharField(max_length=3, blank=True, null=True)
    centangobatranap = models.CharField(max_length=3, blank=True, null=True)
    cetaknotasimpantoko = models.CharField(max_length=3)
    tampilkan_tombol_nota_toko = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'set_nota'


class NotaInap(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    no_nota = models.CharField(unique=True, max_length=17, blank=True, null=True)
    tanggal = models.DateField(blank=True, null=True)
    jam = models.TimeField(blank=True, null=True)
    uang_muka = models.FloatField(db_column='Uang_Muka', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nota_inap'


class NotaJalan(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    no_nota = models.CharField(unique=True, max_length=17, blank=True, null=True)
    tanggal = models.DateField(blank=True, null=True)
    jam = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nota_jalan'


class DetailNotaInap(models.Model):
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', blank=True, null=True)
    nama_bayar = models.ForeignKey(AkunBayar, on_delete=models.DO_NOTHING, db_column='nama_bayar', blank=True, null=True)
    besarppn = models.FloatField(blank=True, null=True)
    besar_bayar = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detail_nota_inap'


class DetailNotaJalan(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    nama_bayar = models.ForeignKey(AkunBayar, on_delete=models.DO_NOTHING, db_column='nama_bayar')
    besarppn = models.FloatField(blank=True, null=True)
    besar_bayar = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detail_nota_jalan'
        unique_together = (('no_rawat', 'nama_bayar'),)


class DetailPenagihanPiutang(models.Model):
    no_tagihan = models.OneToOneField('PenagihanPiutang', on_delete=models.DO_NOTHING, db_column='no_tagihan', primary_key=True)
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat')
    sisapiutang = models.FloatField()

    class Meta:
        managed = False
        db_table = 'detail_penagihan_piutang'
        unique_together = (('no_tagihan', 'no_rawat'),)


class BiayaHarian(models.Model):
    kd_kamar = models.OneToOneField('bangsal.Kamar', on_delete=models.DO_NOTHING, db_column='kd_kamar', primary_key=True)
    nama_biaya = models.CharField(max_length=50)
    besar_biaya = models.FloatField()
    jml = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'biaya_harian'
        unique_together = (('kd_kamar', 'nama_biaya'),)


class BiayaSekali(models.Model):
    kd_kamar = models.OneToOneField('bangsal.Kamar', on_delete=models.DO_NOTHING, db_column='kd_kamar', primary_key=True)
    nama_biaya = models.CharField(max_length=50)
    besar_biaya = models.FloatField()

    class Meta:
        managed = False
        db_table = 'biaya_sekali'
        unique_together = (('kd_kamar', 'nama_biaya'),)


class Billing(models.Model):
    noindex = models.IntegerField()
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat')
    tgl_byr = models.DateField(blank=True, null=True)
    no = models.CharField(max_length=50)
    nm_perawatan = models.CharField(max_length=200)
    pemisah = models.CharField(max_length=1)
    biaya = models.FloatField()
    jumlah = models.FloatField()
    tambahan = models.FloatField()
    totalbiaya = models.FloatField()
    status = models.CharField(max_length=22, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'billing'


class Bank(models.Model):
    namabank = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'bank'


class BayarPemesanan(models.Model):
    tgl_bayar = models.DateField(primary_key=True)
    no_faktur = models.ForeignKey('farmasi.Pemesanan', on_delete=models.DO_NOTHING, db_column='no_faktur')
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    besar_bayar = models.FloatField(blank=True, null=True)
    keterangan = models.CharField(max_length=100, blank=True, null=True)
    nama_bayar = models.ForeignKey(AkunBayar, on_delete=models.DO_NOTHING, db_column='nama_bayar', blank=True, null=True)
    no_bukti = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'bayar_pemesanan'
        unique_together = (('tgl_bayar', 'no_faktur', 'no_bukti'),)


class BayarPemesananInventaris(models.Model):
    tgl_bayar = models.DateField(primary_key=True)
    no_faktur = models.ForeignKey('aset.InventarisPemesanan', on_delete=models.DO_NOTHING, db_column='no_faktur')
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    besar_bayar = models.FloatField(blank=True, null=True)
    keterangan = models.CharField(max_length=100, blank=True, null=True)
    nama_bayar = models.ForeignKey(AkunBayar, on_delete=models.DO_NOTHING, db_column='nama_bayar', blank=True, null=True)
    no_bukti = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'bayar_pemesanan_inventaris'
        unique_together = (('tgl_bayar', 'no_faktur', 'no_bukti'),)


class BayarPemesananNonMedis(models.Model):
    tgl_bayar = models.DateField(primary_key=True)
    no_faktur = models.ForeignKey('aset.Ipsrspemesanan', on_delete=models.DO_NOTHING, db_column='no_faktur')
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    besar_bayar = models.FloatField(blank=True, null=True)
    keterangan = models.CharField(max_length=100, blank=True, null=True)
    nama_bayar = models.ForeignKey(AkunBayar, on_delete=models.DO_NOTHING, db_column='nama_bayar', blank=True, null=True)
    no_bukti = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'bayar_pemesanan_non_medis'
        unique_together = (('tgl_bayar', 'no_faktur', 'no_bukti'),)


class Subrekening(models.Model):
    kd_rek = models.ForeignKey(Rekening, on_delete=models.DO_NOTHING, db_column='kd_rek', related_name='kd_rek_subrekening')
    kd_rek2 = models.OneToOneField(Rekening, on_delete=models.DO_NOTHING, db_column='kd_rek2', primary_key=True, related_name='kd_rek2_subrekening')

    class Meta:
        managed = False
        db_table = 'subrekening'


class TagihanBpdJateng(models.Model):
    no_rkm_medis = models.ForeignKey('pasien.Pasien', on_delete=models.DO_NOTHING, db_column='no_rkm_medis', blank=True, null=True)
    nm_pasien = models.CharField(max_length=40, blank=True, null=True)
    alamat = models.CharField(max_length=200, blank=True, null=True)
    jk = models.CharField(max_length=1, blank=True, null=True)
    tgl_lahir = models.DateField()
    umurdaftar = models.CharField(max_length=7, blank=True, null=True)
    tgl_registrasi = models.DateField(blank=True, null=True)
    no_nota = models.CharField(primary_key=True, max_length=17)
    besar_bayar = models.FloatField(blank=True, null=True)
    keterangan = models.CharField(max_length=255, blank=True, null=True)
    no_rawat = models.CharField(max_length=17, blank=True, null=True)
    status_lanjut = models.CharField(max_length=13, blank=True, null=True)
    tgl_closing = models.DateField(blank=True, null=True)
    status_bayar = models.CharField(max_length=7, blank=True, null=True)
    kasir = models.CharField(max_length=50, blank=True, null=True)
    diupdatebank = models.DateTimeField(blank=True, null=True)
    referensi = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'tagihan_bpd_jateng'


class TagihanSadewa(models.Model):
    no_nota = models.CharField(primary_key=True, max_length=17)
    no_rkm_medis = models.CharField(max_length=15)
    nama_pasien = models.CharField(max_length=60)
    alamat = models.CharField(max_length=200)
    tgl_bayar = models.DateTimeField()
    jenis_bayar = models.CharField(max_length=9)
    jumlah_tagihan = models.FloatField()
    jumlah_bayar = models.FloatField()
    status = models.CharField(max_length=5)
    petugas = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tagihan_sadewa'


class TambahanBiaya(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    nama_biaya = models.CharField(max_length=60)
    besar_biaya = models.FloatField()

    class Meta:
        managed = False
        db_table = 'tambahan_biaya'
        unique_together = (('no_rawat', 'nama_biaya'),)



class MasterTunjanganBulanan(models.Model):
    nama = models.CharField(max_length=60)
    tnj = models.FloatField()

    class Meta:
        managed = False
        db_table = 'master_tunjangan_bulanan'


class MasterTunjanganHarian(models.Model):
    nama = models.CharField(max_length=40)
    tnj = models.FloatField()

    class Meta:
        managed = False
        db_table = 'master_tunjangan_harian'


class PnmTnjBulanan(models.Model):
    id = models.OneToOneField('pegawai.Pegawai', on_delete=models.DO_NOTHING, db_column='id', primary_key=True)
    id_tnj = models.ForeignKey(MasterTunjanganBulanan, on_delete=models.DO_NOTHING, db_column='id_tnj')

    class Meta:
        managed = False
        db_table = 'pnm_tnj_bulanan'
        unique_together = (('id', 'id_tnj'),)


class PnmTnjHarian(models.Model):
    id = models.OneToOneField('pegawai.Pegawai', on_delete=models.DO_NOTHING, db_column='id', primary_key=True)
    id_tnj = models.ForeignKey(MasterTunjanganHarian, on_delete=models.DO_NOTHING, db_column='id_tnj')

    class Meta:
        managed = False
        db_table = 'pnm_tnj_harian'
        unique_together = (('id', 'id_tnj'),)
        

class Dansos(models.Model):
    dana = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'dansos'


class KategoriPemasukanLain(models.Model):
    kode_kategori = models.CharField(primary_key=True, max_length=5)
    nama_kategori = models.CharField(max_length=40, blank=True, null=True)
    kd_rek = models.ForeignKey('Rekening', on_delete=models.DO_NOTHING, db_column='kd_rek', blank=True, null=True, related_name='kd_rek_kategori_pemasukan_lain')
    kd_rek2 = models.ForeignKey('Rekening', on_delete=models.DO_NOTHING, db_column='kd_rek2', blank=True, null=True, related_name='kd_rek2_kategori_pemasukan_lain')

    class Meta:
        managed = False
        db_table = 'kategori_pemasukan_lain'
        
        
class PemasukanLain(models.Model):
    no_masuk = models.CharField(primary_key=True, max_length=17)
    tanggal = models.DateTimeField()
    kode_kategori = models.ForeignKey(KategoriPemasukanLain, on_delete=models.DO_NOTHING, db_column='kode_kategori')
    besar = models.FloatField(blank=True, null=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    keterangan = models.CharField(max_length=50, blank=True, null=True)
    keperluan = models.CharField(max_length=70, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pemasukan_lain'




class KategoriPengeluaranHarian(models.Model):
    kode_kategori = models.CharField(primary_key=True, max_length=5)
    nama_kategori = models.CharField(max_length=40, blank=True, null=True)
    kd_rek = models.ForeignKey('Rekening', on_delete=models.DO_NOTHING, db_column='kd_rek', blank=True, null=True, related_name='kd_rek_kategori_pengeluaran_harian')
    kd_rek2 = models.ForeignKey('Rekening', on_delete=models.DO_NOTHING, db_column='kd_rek2', blank=True, null=True, related_name='kd_rek2_kategori_pengeluaran_harian')

    class Meta:
        managed = False
        db_table = 'kategori_pengeluaran_harian'


class PengeluaranHarian(models.Model):
    no_keluar = models.CharField(primary_key=True, max_length=17)
    tanggal = models.DateTimeField()
    kode_kategori = models.ForeignKey(KategoriPengeluaranHarian, on_delete=models.DO_NOTHING, db_column='kode_kategori', blank=True, null=True)
    biaya = models.FloatField()
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    keterangan = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'pengeluaran_harian'


class PengembalianDeposit(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    tanggal = models.DateTimeField()
    petugas = models.CharField(max_length=20, blank=True, null=True)
    besar_pengembalian = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pengembalian_deposit'


class PenguranganBiaya(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    nama_pengurangan = models.CharField(max_length=60)
    besar_pengurangan = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pengurangan_biaya'
        unique_together = (('no_rawat', 'nama_pengurangan'),)


class MatrikAkunJnsPerawatan(models.Model):
    kd_jenis_prw = models.OneToOneField('ralan.JnsPerawatan', on_delete=models.DO_NOTHING, db_column='kd_jenis_prw', primary_key=True)
    pendapatan_tindakan = models.ForeignKey('Rekening', on_delete=models.DO_NOTHING, related_name='pendapatan_tindakan_matrik_akun_jns_perawatan',db_column='pendapatan_tindakan', blank=True, null=True)
    beban_jasa_dokter = models.ForeignKey('Rekening', on_delete=models.DO_NOTHING, related_name='beban_jasa_dokter_matrik_akun_jns_perawatan',db_column='beban_jasa_dokter', blank=True, null=True)
    utang_jasa_dokter = models.ForeignKey('Rekening', on_delete=models.DO_NOTHING, related_name='utang_jasa_dokter_matrik_akun_jns_perawatan',db_column='utang_jasa_dokter', blank=True, null=True)
    beban_jasa_paramedis = models.ForeignKey('Rekening', on_delete=models.DO_NOTHING, related_name='beban_jasa_paramedis_matrik_akun_jns_perawatan',db_column='beban_jasa_paramedis', blank=True, null=True)
    utang_jasa_paramedis = models.ForeignKey('Rekening', on_delete=models.DO_NOTHING, related_name='utang_jasa_paramedis_matrik_akun_jns_perawatan',db_column='utang_jasa_paramedis', blank=True, null=True)
    beban_kso = models.ForeignKey('Rekening', on_delete=models.DO_NOTHING, related_name='beban_kso_matrik_akun_jns_perawatan',db_column='beban_kso', blank=True, null=True)
    utang_kso = models.ForeignKey('Rekening', on_delete=models.DO_NOTHING, related_name='utang_kso_matrik_akun_jns_perawatan',db_column='utang_kso', blank=True, null=True)
    hpp_persediaan = models.ForeignKey('Rekening', on_delete=models.DO_NOTHING, related_name='hpp_persediaan_matrik_akun_jns_perawatan',db_column='hpp_persediaan', blank=True, null=True)
    persediaan_bhp = models.ForeignKey('Rekening', on_delete=models.DO_NOTHING, related_name='persediaan_bhp_matrik_akun_jns_perawatan',db_column='persediaan_bhp', blank=True, null=True)
    beban_jasa_sarana = models.ForeignKey('Rekening', on_delete=models.DO_NOTHING, related_name='beban_jasa_sarana_matrik_akun_jns_perawatan',db_column='beban_jasa_sarana', blank=True, null=True)
    utang_jasa_sarana = models.ForeignKey('Rekening', on_delete=models.DO_NOTHING, related_name='utang_jasa_sarana_matrik_akun_jns_perawatan',db_column='utang_jasa_sarana', blank=True, null=True)
    beban_menejemen = models.ForeignKey('Rekening', on_delete=models.DO_NOTHING, related_name='beban_menejemen_matrik_akun_jns_perawatan',db_column='beban_menejemen', blank=True, null=True)
    utang_menejemen = models.ForeignKey('Rekening', on_delete=models.DO_NOTHING, related_name='utang_menejemen_matrik_akun_jns_perawatan',db_column='utang_menejemen', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'matrik_akun_jns_perawatan'


class MatrikAkunJnsPerawatanInap(models.Model):
    kd_jenis_prw = models.OneToOneField('ranap.JnsPerawatanInap', on_delete=models.DO_NOTHING, db_column='kd_jenis_prw', primary_key=True)
    pendapatan_tindakan = models.ForeignKey('Rekening', on_delete=models.DO_NOTHING, related_name='pendapatan_tindakan_matrik_akun_jns_perawatan_inap',db_column='pendapatan_tindakan', blank=True, null=True)
    beban_jasa_dokter = models.ForeignKey('Rekening', on_delete=models.DO_NOTHING, related_name='beban_jasa_dokter_matrik_akun_jns_perawatan_inap',db_column='beban_jasa_dokter', blank=True, null=True)
    utang_jasa_dokter = models.ForeignKey('Rekening', on_delete=models.DO_NOTHING, related_name='utang_jasa_dokter_matrik_akun_jns_perawatan_inap',db_column='utang_jasa_dokter', blank=True, null=True)
    beban_jasa_paramedis = models.ForeignKey('Rekening', on_delete=models.DO_NOTHING, related_name='beban_jasa_paramedis_matrik_akun_jns_perawatan_inap',db_column='beban_jasa_paramedis', blank=True, null=True)
    utang_jasa_paramedis = models.ForeignKey('Rekening', on_delete=models.DO_NOTHING, related_name='utang_jasa_paramedis_matrik_akun_jns_perawatan_inap',db_column='utang_jasa_paramedis', blank=True, null=True)
    beban_kso = models.ForeignKey('Rekening', on_delete=models.DO_NOTHING, related_name='beban_kso_matrik_akun_jns_perawatan_inap',db_column='beban_kso', blank=True, null=True)
    utang_kso = models.ForeignKey('Rekening', on_delete=models.DO_NOTHING, related_name='utang_kso_matrik_akun_jns_perawatan_inap',db_column='utang_kso', blank=True, null=True)
    hpp_persediaan = models.ForeignKey('Rekening', on_delete=models.DO_NOTHING, related_name='hpp_persediaan_matrik_akun_jns_perawatan_inap',db_column='hpp_persediaan', blank=True, null=True)
    persediaan_bhp = models.ForeignKey('Rekening', on_delete=models.DO_NOTHING, related_name='persediaan_bhp_matrik_akun_jns_perawatan_inap',db_column='persediaan_bhp', blank=True, null=True)
    beban_jasa_sarana = models.ForeignKey('Rekening', on_delete=models.DO_NOTHING, related_name='beban_jasa_sarana_matrik_akun_jns_perawatan_inap',db_column='beban_jasa_sarana', blank=True, null=True)
    utang_jasa_sarana = models.ForeignKey('Rekening', on_delete=models.DO_NOTHING, related_name='utang_jasa_sarana_matrik_akun_jns_perawatan_inap',db_column='utang_jasa_sarana', blank=True, null=True)
    beban_menejemen = models.ForeignKey('Rekening', on_delete=models.DO_NOTHING, related_name='beban_menejemen_matrik_akun_jns_perawatan_inap',db_column='beban_menejemen', blank=True, null=True)
    utang_menejemen = models.ForeignKey('Rekening', on_delete=models.DO_NOTHING, related_name='utang_menejemen_matrik_akun_jns_perawatan_inap',db_column='utang_menejemen', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'matrik_akun_jns_perawatan_inap'


class PenagihanPiutang(models.Model):
    no_tagihan = models.CharField(primary_key=True, max_length=17)
    tanggal = models.DateField()
    tanggaltempo = models.DateField()
    tempo = models.IntegerField()
    nip = models.ForeignKey('pegawai.Pegawai', on_delete=models.DO_NOTHING, db_column='nip', related_name='nip_pegawai_penagihan_piutang')
    nip_menyetujui = models.ForeignKey('pegawai.Pegawai', on_delete=models.DO_NOTHING, db_column='nip_menyetujui', related_name='nip_menyetujui_penagihan_piutang')
    kd_pj = models.ForeignKey('asuransi.Penjab', on_delete=models.DO_NOTHING, db_column='kd_pj')
    catatan = models.CharField(max_length=100)
    kd_rek = models.ForeignKey('Rekening', on_delete=models.DO_NOTHING, db_column='kd_rek')
    status = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'penagihan_piutang'


class BuktiPenagihanPiutang(models.Model):
    no_tagihan = models.OneToOneField('PenagihanPiutang', on_delete=models.DO_NOTHING, db_column='no_tagihan', primary_key=True)
    photo = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bukti_penagihan_piutang'


class ClosingKasir(models.Model):
    shift = models.CharField(primary_key=True, max_length=5)
    jam_masuk = models.TimeField()
    jam_pulang = models.TimeField()

    class Meta:
        managed = False
        db_table = 'closing_kasir'


