from django.db import models

# Create your models here.

class GolonganPolri(models.Model):
    nama_golongan = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'golongan_polri'


class GolonganTni(models.Model):
    nama_golongan = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'golongan_tni'
        
class BahasaPasien(models.Model):
    nama_bahasa = models.CharField(unique=True, max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bahasa_pasien'
        
        
class SukuBangsa(models.Model):
    nama_suku_bangsa = models.CharField(unique=True, max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'suku_bangsa'
        
        
class CacatFisik(models.Model):
    nama_cacat = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'cacat_fisik'
        
        
class JabatanPolri(models.Model):
    nama_jabatan = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jabatan_polri'


class JabatanTni(models.Model):
    nama_jabatan = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jabatan_tni'
        
        
class PangkatPolri(models.Model):
    nama_pangkat = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pangkat_polri'


class PangkatTni(models.Model):
    nama_pangkat = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pangkat_tni'


class PerusahaanPasien(models.Model):
    kode_perusahaan = models.CharField(primary_key=True, max_length=8)
    nama_perusahaan = models.CharField(max_length=70, blank=True, null=True)
    alamat = models.CharField(max_length=100, blank=True, null=True)
    kota = models.CharField(max_length=40, blank=True, null=True)
    no_telp = models.CharField(max_length=27, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perusahaan_pasien'


class SatuanPolri(models.Model):
    nama_satuan = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'satuan_polri'


class SatuanTni(models.Model):
    nama_satuan = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'satuan_tni'


class Pasien(models.Model):
    no_rkm_medis = models.CharField(primary_key=True, max_length=15)
    nm_pasien = models.CharField(max_length=40, blank=True, null=True)
    no_ktp = models.CharField(max_length=20, blank=True, null=True)
    jk = models.CharField(max_length=1, blank=True, null=True)
    tmp_lahir = models.CharField(max_length=15, blank=True, null=True)
    tgl_lahir = models.DateField(blank=True, null=True)
    nm_ibu = models.CharField(max_length=40)
    alamat = models.CharField(max_length=200, blank=True, null=True)
    gol_darah = models.CharField(max_length=2, blank=True, null=True)
    pekerjaan = models.CharField(max_length=60, blank=True, null=True)
    stts_nikah = models.CharField(max_length=13, blank=True, null=True)
    agama = models.CharField(max_length=12, blank=True, null=True)
    tgl_daftar = models.DateField(blank=True, null=True)
    no_tlp = models.CharField(max_length=40, blank=True, null=True)
    umur = models.CharField(max_length=30)
    pnd = models.CharField(max_length=14)
    keluarga = models.CharField(max_length=7, blank=True, null=True)
    namakeluarga = models.CharField(max_length=50)
    kd_pj = models.ForeignKey('asuransi.Penjab', on_delete=models.DO_NOTHING, db_column='kd_pj')
    no_peserta = models.CharField(max_length=25, blank=True, null=True)
    kd_kel = models.ForeignKey('alamat.Kelurahan', on_delete=models.DO_NOTHING, db_column='kd_kel')
    kd_kec = models.ForeignKey('alamat.Kecamatan', on_delete=models.DO_NOTHING, db_column='kd_kec')
    kd_kab = models.ForeignKey('alamat.Kabupaten', on_delete=models.DO_NOTHING, db_column='kd_kab')
    pekerjaanpj = models.CharField(max_length=35)
    alamatpj = models.CharField(max_length=100)
    kelurahanpj = models.CharField(max_length=60)
    kecamatanpj = models.CharField(max_length=60)
    kabupatenpj = models.CharField(max_length=60)
    perusahaan_pasien = models.ForeignKey('PerusahaanPasien', on_delete=models.DO_NOTHING, db_column='perusahaan_pasien')
    suku_bangsa = models.ForeignKey('SukuBangsa', on_delete=models.DO_NOTHING, db_column='suku_bangsa')
    bahasa_pasien = models.ForeignKey(BahasaPasien, on_delete=models.DO_NOTHING, db_column='bahasa_pasien')
    cacat_fisik = models.ForeignKey(CacatFisik, on_delete=models.DO_NOTHING, db_column='cacat_fisik')
    email = models.CharField(max_length=50)
    nip = models.CharField(max_length=30)
    kd_prop = models.ForeignKey('alamat.Propinsi', on_delete=models.DO_NOTHING, db_column='kd_prop')
    propinsipj = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'pasien'
        
        
    def __str__(self):
        return self.no_rkm_medis


class PasienBayi(models.Model):
    no_rkm_medis = models.OneToOneField(Pasien, on_delete=models.DO_NOTHING, db_column='no_rkm_medis', primary_key=True)
    umur_ibu = models.CharField(max_length=8)
    nama_ayah = models.CharField(max_length=50)
    umur_ayah = models.CharField(max_length=8)
    berat_badan = models.CharField(max_length=10)
    panjang_badan = models.CharField(max_length=10)
    lingkar_kepala = models.CharField(max_length=10)
    proses_lahir = models.CharField(max_length=60)
    anakke = models.CharField(max_length=2)
    jam_lahir = models.TimeField()
    keterangan = models.CharField(max_length=50)
    diagnosa = models.CharField(max_length=60, blank=True, null=True)
    penyulit_kehamilan = models.CharField(max_length=60, blank=True, null=True)
    ketuban = models.CharField(max_length=60, blank=True, null=True)
    lingkar_perut = models.CharField(max_length=10, blank=True, null=True)
    lingkar_dada = models.CharField(max_length=10, blank=True, null=True)
    penolong = models.ForeignKey('pegawai.Pegawai', on_delete=models.DO_NOTHING, db_column='penolong', blank=True, null=True)
    no_skl = models.CharField(unique=True, max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pasien_bayi'


class PasienCorona(models.Model):
    no_pengenal = models.CharField(max_length=20, blank=True, null=True)
    no_rkm_medis = models.OneToOneField(Pasien, on_delete=models.DO_NOTHING, db_column='no_rkm_medis', primary_key=True)
    inisial = models.CharField(max_length=15, blank=True, null=True)
    nama_lengkap = models.CharField(max_length=40, blank=True, null=True)
    tgl_masuk = models.DateField(blank=True, null=True)
    kode_jk = models.CharField(max_length=1, blank=True, null=True)
    nama_jk = models.CharField(max_length=10, blank=True, null=True)
    tgl_lahir = models.DateField(blank=True, null=True)
    kode_kewarganegaraan = models.CharField(max_length=5, blank=True, null=True)
    nama_kewarganegaraan = models.CharField(max_length=25, blank=True, null=True)
    kode_penularan = models.CharField(max_length=5, blank=True, null=True)
    sumber_penularan = models.CharField(max_length=40, blank=True, null=True)
    kd_kelurahan = models.CharField(max_length=15, blank=True, null=True)
    nm_kelurahan = models.CharField(max_length=20, blank=True, null=True)
    kd_kecamatan = models.CharField(max_length=10, blank=True, null=True)
    nm_kecamatan = models.CharField(max_length=20, blank=True, null=True)
    kd_kabupaten = models.CharField(max_length=6, blank=True, null=True)
    nm_kabupaten = models.CharField(max_length=20, blank=True, null=True)
    kd_propinsi = models.CharField(max_length=3, blank=True, null=True)
    nm_propinsi = models.CharField(max_length=20, blank=True, null=True)
    tgl_keluar = models.DateField(blank=True, null=True)
    kode_statuskeluar = models.CharField(max_length=5, blank=True, null=True)
    nama_statuskeluar = models.CharField(max_length=40, blank=True, null=True)
    tgl_lapor = models.DateTimeField(blank=True, null=True)
    kode_statusrawat = models.CharField(max_length=5, blank=True, null=True)
    nama_statusrawat = models.CharField(max_length=40, blank=True, null=True)
    kode_statusisolasi = models.CharField(max_length=5, blank=True, null=True)
    nama_statusisolasi = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    notelp = models.CharField(max_length=40, blank=True, null=True)
    sebab_kematian = models.CharField(max_length=60, blank=True, null=True)
    kode_jenis_pasien = models.CharField(max_length=5)
    nama_jenis_pasien = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'pasien_corona'


class PasienMati(models.Model):
    tanggal = models.DateField(blank=True, null=True)
    jam = models.TimeField(blank=True, null=True)
    no_rkm_medis = models.OneToOneField(Pasien, on_delete=models.DO_NOTHING, db_column='no_rkm_medis', primary_key=True)
    keterangan = models.CharField(max_length=100, blank=True, null=True)
    temp_meninggal = models.CharField(max_length=24, blank=True, null=True)
    icd1 = models.CharField(max_length=20, blank=True, null=True)
    icd2 = models.CharField(max_length=20, blank=True, null=True)
    icd3 = models.CharField(max_length=20, blank=True, null=True)
    icd4 = models.CharField(max_length=20, blank=True, null=True)
    kd_dokter = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter')

    class Meta:
        managed = False
        db_table = 'pasien_mati'


class PasienPolri(models.Model):
    no_rkm_medis = models.OneToOneField(Pasien, on_delete=models.DO_NOTHING, db_column='no_rkm_medis', primary_key=True)
    golongan_polri = models.ForeignKey(GolonganPolri, on_delete=models.DO_NOTHING, db_column='golongan_polri')
    pangkat_polri = models.ForeignKey(PangkatPolri, on_delete=models.DO_NOTHING, db_column='pangkat_polri')
    satuan_polri = models.ForeignKey('SatuanPolri', on_delete=models.DO_NOTHING, db_column='satuan_polri')
    jabatan_polri = models.ForeignKey(JabatanPolri, on_delete=models.DO_NOTHING, db_column='jabatan_polri')

    class Meta:
        managed = False
        db_table = 'pasien_polri'


class PasienTni(models.Model):
    no_rkm_medis = models.OneToOneField(Pasien, on_delete=models.DO_NOTHING, db_column='no_rkm_medis', primary_key=True)
    golongan_tni = models.ForeignKey(GolonganTni, on_delete=models.DO_NOTHING, db_column='golongan_tni')
    pangkat_tni = models.ForeignKey(PangkatTni, on_delete=models.DO_NOTHING, db_column='pangkat_tni')
    satuan_tni = models.ForeignKey('SatuanTni', on_delete=models.DO_NOTHING, db_column='satuan_tni')
    jabatan_tni = models.ForeignKey(JabatanTni, on_delete=models.DO_NOTHING, db_column='jabatan_tni')

    class Meta:
        managed = False
        db_table = 'pasien_tni'


class PersonalPasien(models.Model):
    no_rkm_medis = models.OneToOneField(Pasien, on_delete=models.DO_NOTHING, db_column='no_rkm_medis', primary_key=True)
    gambar = models.CharField(max_length=1000, blank=True, null=True)
    password = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personal_pasien'        


class CatatanPasien(models.Model):
    no_rkm_medis = models.OneToOneField('Pasien', on_delete=models.DO_NOTHING, db_column='no_rkm_medis', primary_key=True)
    catatan = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catatan_pasien'

        
class MasterImunisasi(models.Model):
    kode_imunisasi = models.CharField(primary_key=True, max_length=3)
    nama_imunisasi = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_imunisasi'


class RiwayatImunisasi(models.Model):
    no_rkm_medis = models.OneToOneField(Pasien, on_delete=models.DO_NOTHING, db_column='no_rkm_medis', primary_key=True)
    kode_imunisasi = models.ForeignKey(MasterImunisasi, on_delete=models.DO_NOTHING, db_column='kode_imunisasi')
    no_imunisasi = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'riwayat_imunisasi'
        unique_together = (('no_rkm_medis', 'kode_imunisasi', 'no_imunisasi'),)


class RiwayatPersalinanPasien(models.Model):
    no_rkm_medis = models.OneToOneField(Pasien, on_delete=models.DO_NOTHING, db_column='no_rkm_medis', primary_key=True)
    tgl_thn = models.CharField(max_length=12)
    tempat_persalinan = models.CharField(max_length=30, blank=True, null=True)
    usia_hamil = models.CharField(max_length=20, blank=True, null=True)
    jenis_persalinan = models.CharField(max_length=20, blank=True, null=True)
    penolong = models.CharField(max_length=30, blank=True, null=True)
    penyulit = models.CharField(max_length=40, blank=True, null=True)
    jk = models.CharField(max_length=1, blank=True, null=True)
    bbpb = models.CharField(max_length=10, blank=True, null=True)
    keadaan = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'riwayat_persalinan_pasien'
        unique_together = (('no_rkm_medis', 'tgl_thn'),)


class SetKelengkapanDataPasien(models.Model):
    no_ktp = models.CharField(max_length=3, blank=True, null=True)
    p_no_ktp = models.IntegerField(blank=True, null=True)
    tmp_lahir = models.CharField(max_length=3, blank=True, null=True)
    p_tmp_lahir = models.IntegerField(blank=True, null=True)
    nm_ibu = models.CharField(max_length=3, blank=True, null=True)
    p_nm_ibu = models.IntegerField(blank=True, null=True)
    alamat = models.CharField(max_length=3, blank=True, null=True)
    p_alamat = models.IntegerField(blank=True, null=True)
    pekerjaan = models.CharField(max_length=3, blank=True, null=True)
    p_pekerjaan = models.IntegerField(blank=True, null=True)
    no_tlp = models.CharField(max_length=3, blank=True, null=True)
    p_no_tlp = models.IntegerField(blank=True, null=True)
    umur = models.CharField(max_length=3, blank=True, null=True)
    p_umur = models.IntegerField(blank=True, null=True)
    namakeluarga = models.CharField(max_length=3, blank=True, null=True)
    p_namakeluarga = models.IntegerField(blank=True, null=True)
    no_peserta = models.CharField(max_length=3, blank=True, null=True)
    p_no_peserta = models.IntegerField(blank=True, null=True)
    kelurahan = models.CharField(max_length=3, blank=True, null=True)
    p_kelurahan = models.IntegerField(blank=True, null=True)
    kecamatan = models.CharField(max_length=3, blank=True, null=True)
    p_kecamatan = models.IntegerField(blank=True, null=True)
    kabupaten = models.CharField(max_length=3, blank=True, null=True)
    p_kabupaten = models.IntegerField(blank=True, null=True)
    pekerjaanpj = models.CharField(max_length=3, blank=True, null=True)
    p_pekerjaanpj = models.IntegerField(blank=True, null=True)
    alamatpj = models.CharField(max_length=3, blank=True, null=True)
    p_alamatpj = models.IntegerField(blank=True, null=True)
    kelurahanpj = models.CharField(max_length=3, blank=True, null=True)
    p_kelurahanpj = models.IntegerField(blank=True, null=True)
    kecamatanpj = models.CharField(max_length=3, blank=True, null=True)
    p_kecamatanpj = models.IntegerField(blank=True, null=True)
    kabupatenpj = models.CharField(max_length=3, blank=True, null=True)
    p_kabupatenpj = models.IntegerField(blank=True, null=True)
    propinsi = models.CharField(max_length=3)
    p_propinsi = models.IntegerField()
    propinsipj = models.CharField(max_length=3)
    p_propinsipj = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'set_kelengkapan_data_pasien'


class Sidikjaripasien(models.Model):
    no_rkm_medis = models.OneToOneField(Pasien, on_delete=models.DO_NOTHING, db_column='no_rkm_medis', primary_key=True)
    sidikjari = models.TextField()

    class Meta:
        managed = False
        db_table = 'sidikjaripasien'


