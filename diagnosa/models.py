from django.db import models

# Create your models here.

class KategoriPenyakit(models.Model):
    kd_ktg = models.CharField(primary_key=True, max_length=8)
    nm_kategori = models.CharField(max_length=30, blank=True, null=True)
    ciri_umum = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kategori_penyakit'


class Penyakit(models.Model):
    kd_penyakit = models.CharField(primary_key=True, max_length=10)
    nm_penyakit = models.CharField(max_length=100, blank=True, null=True)
    ciri_ciri = models.TextField(blank=True, null=True)
    keterangan = models.CharField(max_length=60, blank=True, null=True)
    kd_ktg = models.ForeignKey(KategoriPenyakit, on_delete=models.DO_NOTHING, db_column='kd_ktg', blank=True, null=True)
    status = models.CharField(max_length=13)

    class Meta:
        managed = False
        db_table = 'penyakit'


class PenyakitPd3I(models.Model):
    kd_penyakit = models.OneToOneField(Penyakit, on_delete=models.DO_NOTHING, db_column='kd_penyakit', primary_key=True)

    class Meta:
        managed = False
        db_table = 'penyakit_pd3i'


class DiagnosaPasien(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    kd_penyakit = models.ForeignKey('diagnosa.Penyakit', on_delete=models.DO_NOTHING, db_column='kd_penyakit')
    status = models.CharField(max_length=5)
    prioritas = models.IntegerField()
    status_penyakit = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diagnosa_pasien'
        unique_together = (('no_rawat', 'kd_penyakit', 'status'),)
        

class DiagnosaCorona(models.Model):
    no_rkm_medis = models.OneToOneField('pasien.PasienCorona', on_delete=models.DO_NOTHING, db_column='no_rkm_medis', primary_key=True)
    kode_icd = models.CharField(max_length=10)
    nama_penyakit = models.CharField(max_length=200, blank=True, null=True)
    status = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diagnosa_corona'
        unique_together = (('no_rkm_medis', 'kode_icd'),)


class TemporarySurveilensPenyakit(models.Model):
    kd_penyakit = models.ForeignKey(Penyakit, on_delete=models.DO_NOTHING, db_column='kd_penyakit', related_name='kd_penyakit_temporary_surveilans_penyakit')
    kd_penyakit2 = models.ForeignKey(Penyakit, on_delete=models.DO_NOTHING, db_column='kd_penyakit2', related_name='kd_penyakit2_temporary_surveilans_penyakit')

    class Meta:
        managed = False
        db_table = 'temporary_surveilens_penyakit'



############# INACBGs
class InacbgGroupingStage1(models.Model):
    no_sep = models.OneToOneField('asuransi.BridgingSep', on_delete=models.DO_NOTHING, db_column='no_sep', primary_key=True)
    code_cbg = models.CharField(max_length=10, blank=True, null=True)
    deskripsi = models.CharField(max_length=200, blank=True, null=True)
    tarif = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inacbg_grouping_stage1'


class InacbgGroupingStage12(models.Model):
    no_sep = models.OneToOneField('InacbgKlaimBaru2', on_delete=models.DO_NOTHING, db_column='no_sep', primary_key=True)
    code_cbg = models.CharField(max_length=10, blank=True, null=True)
    deskripsi = models.CharField(max_length=200, blank=True, null=True)
    tarif = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inacbg_grouping_stage12'


class InacbgKlaimBaru(models.Model):
    no_sep = models.OneToOneField('asuransi.BridgingSep', on_delete=models.DO_NOTHING, db_column='no_sep', primary_key=True)
    patient_id = models.CharField(max_length=30, blank=True, null=True)
    admission_id = models.CharField(max_length=30, blank=True, null=True)
    hospital_admission_id = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inacbg_klaim_baru'


class InacbgKlaimBaru2(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    no_sep = models.CharField(unique=True, max_length=40)
    patient_id = models.CharField(max_length=30, blank=True, null=True)
    admission_id = models.CharField(max_length=30, blank=True, null=True)
    hospital_admission_id = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inacbg_klaim_baru2'


class InacbgNoklaimCorona(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    no_klaim = models.CharField(unique=True, max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inacbg_noklaim_corona'


class InacbgCoderNik(models.Model):
    nik = models.OneToOneField('pegawai.Pegawai', on_delete=models.DO_NOTHING, db_column='nik', primary_key=True)
    no_ik = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inacbg_coder_nik'
        
        
class InacbgDataTerkirim(models.Model):
    no_sep = models.OneToOneField('asuransi.BridgingSep', on_delete=models.DO_NOTHING, db_column='no_sep', primary_key=True)
    nik = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inacbg_data_terkirim'


class InacbgDataTerkirim2(models.Model):
    no_sep = models.OneToOneField('InacbgKlaimBaru2', on_delete=models.DO_NOTHING, db_column='no_sep', primary_key=True)
    nik = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inacbg_data_terkirim2'


########## MASALAH KEPERAWATAN

class MasterMasalahKeperawatan(models.Model):
    kode_masalah = models.CharField(primary_key=True, max_length=3)
    nama_masalah = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_masalah_keperawatan'


class MasterMasalahKeperawatanAnak(models.Model):
    kode_masalah = models.CharField(primary_key=True, max_length=3)
    nama_masalah = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_masalah_keperawatan_anak'


class MasterMasalahKeperawatanGigi(models.Model):
    kode_masalah = models.CharField(primary_key=True, max_length=3)
    nama_masalah = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_masalah_keperawatan_gigi'


class MasterMasalahKeperawatanMata(models.Model):
    kode_masalah = models.CharField(primary_key=True, max_length=3)
    nama_masalah = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_masalah_keperawatan_mata'


class PenilaianAwalKeperawatanMataMasalah(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    kode_masalah = models.ForeignKey(MasterMasalahKeperawatan, on_delete=models.DO_NOTHING, db_column='kode_masalah')

    class Meta:
        managed = False
        db_table = 'penilaian_awal_keperawatan_mata_masalah'
        unique_together = (('no_rawat', 'kode_masalah'),)