from django.db import models

# Create your models here.

class SetPjlab(models.Model):
    kd_dokterlab = models.OneToOneField('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokterlab', primary_key=True, related_name='kd_dokterlab_setpjlab')
    kd_dokterrad = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokterrad', related_name='kd_dokterrad_setpjlab')
    kd_dokterhemodialisa = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokterhemodialisa', related_name='kd_dokterhemodialisa_setpjlab')
    kd_dokterutd = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokterutd', blank=True, null=True, related_name='kd_dokterutd_setpjlab')
    kd_dokterlabpa = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokterlabpa', related_name='kd_dokterlabpa_setpjlab')

    class Meta:
        managed = False
        db_table = 'set_pjlab'
        unique_together = (('kd_dokterlab', 'kd_dokterrad', 'kd_dokterhemodialisa'),)


class JnsPerawatanLab(models.Model):
    kd_jenis_prw = models.CharField(primary_key=True, max_length=15)
    nm_perawatan = models.CharField(max_length=80, blank=True, null=True)
    bagian_rs = models.FloatField(blank=True, null=True)
    bhp = models.FloatField()
    tarif_perujuk = models.FloatField()
    tarif_tindakan_dokter = models.FloatField()
    tarif_tindakan_petugas = models.FloatField(blank=True, null=True)
    kso = models.FloatField(blank=True, null=True)
    menejemen = models.FloatField(blank=True, null=True)
    total_byr = models.FloatField(blank=True, null=True)
    kd_pj = models.ForeignKey('asuransi.Penjab', on_delete=models.DO_NOTHING, db_column='kd_pj')
    status = models.CharField(max_length=1)
    kelas = models.CharField(max_length=11)
    kategori = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'jns_perawatan_lab'


class PeriksaLab(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip')
    kd_jenis_prw = models.ForeignKey(JnsPerawatanLab, on_delete=models.DO_NOTHING, db_column='kd_jenis_prw')
    tgl_periksa = models.DateField()
    jam = models.TimeField()
    dokter_perujuk = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='dokter_perujuk', related_name='dokter_perujuk_periksalab')
    bagian_rs = models.FloatField()
    bhp = models.FloatField()
    tarif_perujuk = models.FloatField()
    tarif_tindakan_dokter = models.FloatField()
    tarif_tindakan_petugas = models.FloatField()
    kso = models.FloatField(blank=True, null=True)
    menejemen = models.FloatField(blank=True, null=True)
    biaya = models.FloatField()
    kd_dokter = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter', related_name='kd_dokter_periksalab')
    status = models.CharField(max_length=5, blank=True, null=True)
    kategori = models.CharField(max_length=2)

    class Meta:
        managed = False
        db_table = 'periksa_lab'
        unique_together = (('no_rawat', 'kd_jenis_prw', 'tgl_periksa', 'jam'),)


class PermintaanLab(models.Model):
    noorder = models.CharField(primary_key=True, max_length=15)
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat')
    tgl_permintaan = models.DateField()
    jam_permintaan = models.TimeField()
    tgl_sampel = models.DateField()
    jam_sampel = models.TimeField()
    tgl_hasil = models.DateField()
    jam_hasil = models.TimeField()
    dokter_perujuk = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='dokter_perujuk')
    status = models.CharField(max_length=5)
    informasi_tambahan = models.CharField(max_length=60)
    diagnosa_klinis = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'permintaan_lab'


class PermintaanLabpa(models.Model):
    noorder = models.CharField(primary_key=True, max_length=15)
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat')
    tgl_permintaan = models.DateField()
    jam_permintaan = models.TimeField()
    tgl_sampel = models.DateField()
    jam_sampel = models.TimeField()
    tgl_hasil = models.DateField()
    jam_hasil = models.TimeField()
    dokter_perujuk = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='dokter_perujuk')
    status = models.CharField(max_length=5)
    informasi_tambahan = models.CharField(max_length=60)
    diagnosa_klinis = models.CharField(max_length=80)
    pengambilan_bahan = models.DateField(blank=True, null=True)
    diperoleh_dengan = models.CharField(max_length=40, blank=True, null=True)
    lokasi_jaringan = models.CharField(max_length=40, blank=True, null=True)
    diawetkan_dengan = models.CharField(max_length=40, blank=True, null=True)
    pernah_dilakukan_di = models.CharField(max_length=100, blank=True, null=True)
    tanggal_pa_sebelumnya = models.DateField(blank=True, null=True)
    nomor_pa_sebelumnya = models.CharField(max_length=20, blank=True, null=True)
    diagnosa_pa_sebelumnya = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permintaan_labpa'


class TemplateLaboratorium(models.Model):
    kd_jenis_prw = models.ForeignKey(JnsPerawatanLab, on_delete=models.DO_NOTHING, db_column='kd_jenis_prw')
    id_template = models.AutoField(primary_key=True)
    pemeriksaan = models.CharField(db_column='Pemeriksaan', max_length=200)  # Field name made lowercase.
    satuan = models.CharField(max_length=20)
    nilai_rujukan_ld = models.CharField(max_length=30)
    nilai_rujukan_la = models.CharField(max_length=30)
    nilai_rujukan_pd = models.CharField(max_length=30)
    nilai_rujukan_pa = models.CharField(max_length=30)
    bagian_rs = models.FloatField()
    bhp = models.FloatField()
    bagian_perujuk = models.FloatField()
    bagian_dokter = models.FloatField()
    bagian_laborat = models.FloatField()
    kso = models.FloatField(blank=True, null=True)
    menejemen = models.FloatField(blank=True, null=True)
    biaya_item = models.FloatField()
    urut = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'template_laboratorium'


class PermintaanDetailPermintaanLab(models.Model):
    noorder = models.OneToOneField('PermintaanLab', on_delete=models.DO_NOTHING, db_column='noorder', primary_key=True)
    kd_jenis_prw = models.ForeignKey(JnsPerawatanLab, on_delete=models.DO_NOTHING, db_column='kd_jenis_prw')
    id_template = models.ForeignKey('TemplateLaboratorium', on_delete=models.DO_NOTHING, db_column='id_template')
    stts_bayar = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permintaan_detail_permintaan_lab'
        unique_together = (('noorder', 'kd_jenis_prw', 'id_template'),)


class PermintaanPemeriksaanLab(models.Model):
    noorder = models.OneToOneField(PermintaanLab, on_delete=models.DO_NOTHING, db_column='noorder', primary_key=True)
    kd_jenis_prw = models.ForeignKey(JnsPerawatanLab, on_delete=models.DO_NOTHING, db_column='kd_jenis_prw')
    stts_bayar = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permintaan_pemeriksaan_lab'
        unique_together = (('noorder', 'kd_jenis_prw'),)


class PermintaanPemeriksaanLabpa(models.Model):
    noorder = models.OneToOneField(PermintaanLabpa, on_delete=models.DO_NOTHING, db_column='noorder', primary_key=True)
    kd_jenis_prw = models.ForeignKey(JnsPerawatanLab, on_delete=models.DO_NOTHING, db_column='kd_jenis_prw')
    stts_bayar = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permintaan_pemeriksaan_labpa'
        unique_together = (('noorder', 'kd_jenis_prw'),)
        
        
class DetailPeriksaLab(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    kd_jenis_prw = models.ForeignKey('JnsPerawatanLab', on_delete=models.DO_NOTHING, db_column='kd_jenis_prw')
    tgl_periksa = models.DateField()
    jam = models.TimeField()
    id_template = models.ForeignKey('TemplateLaboratorium', on_delete=models.DO_NOTHING, db_column='id_template')
    nilai = models.CharField(max_length=60)
    nilai_rujukan = models.CharField(max_length=30)
    keterangan = models.CharField(max_length=60)
    bagian_rs = models.FloatField()
    bhp = models.FloatField()
    bagian_perujuk = models.FloatField()
    bagian_dokter = models.FloatField()
    bagian_laborat = models.FloatField()
    kso = models.FloatField(blank=True, null=True)
    menejemen = models.FloatField(blank=True, null=True)
    biaya_item = models.FloatField()

    class Meta:
        managed = False
        db_table = 'detail_periksa_lab'
        unique_together = (('no_rawat', 'kd_jenis_prw', 'tgl_periksa', 'jam', 'id_template'),)


class DetailPeriksaLabpa(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    kd_jenis_prw = models.ForeignKey('JnsPerawatanLab', on_delete=models.DO_NOTHING, db_column='kd_jenis_prw')
    tgl_periksa = models.DateField()
    jam = models.TimeField()
    diagnosa_klinik = models.CharField(max_length=50, blank=True, null=True)
    makroskopik = models.CharField(max_length=1024, blank=True, null=True)
    mikroskopik = models.CharField(max_length=1024, blank=True, null=True)
    kesimpulan = models.CharField(max_length=300, blank=True, null=True)
    kesan = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detail_periksa_labpa'
        unique_together = (('no_rawat', 'kd_jenis_prw', 'tgl_periksa', 'jam'),)


class DetailPeriksaLabpaGambar(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    kd_jenis_prw = models.ForeignKey('JnsPerawatanLab', on_delete=models.DO_NOTHING, db_column='kd_jenis_prw')
    tgl_periksa = models.DateField()
    jam = models.TimeField()
    photo = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detail_periksa_labpa_gambar'
        unique_together = (('no_rawat', 'kd_jenis_prw', 'tgl_periksa', 'jam'),)


class SaranKesanLab(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    tgl_periksa = models.DateField()
    jam = models.TimeField()
    saran = models.CharField(max_length=700, blank=True, null=True)
    kesan = models.CharField(max_length=700, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'saran_kesan_lab'
        unique_together = (('no_rawat', 'tgl_periksa', 'jam'),)


