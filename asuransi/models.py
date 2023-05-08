from django.db import models

# Create your models here.


class Asuransi(models.Model):
    stts = models.CharField(primary_key=True, max_length=5)
    biaya = models.FloatField()

    class Meta:
        managed = False
        db_table = 'asuransi'


class Jamsostek(models.Model):
    stts = models.CharField(primary_key=True, max_length=5)
    biaya = models.FloatField()

    class Meta:
        managed = False
        db_table = 'jamsostek'


class Penjab(models.Model):
    kd_pj = models.CharField(primary_key=True, max_length=3)
    png_jawab = models.CharField(max_length=30)
    nama_perusahaan = models.CharField(max_length=60)
    alamat_asuransi = models.CharField(max_length=130)
    no_telp = models.CharField(max_length=40)
    attn = models.CharField(max_length=60)
    status = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'penjab'
    
    def __str__(self):
        return self.png_jawab
 
 
class PasswordAsuransi(models.Model):
    kd_pj = models.OneToOneField('Penjab', on_delete=models.DO_NOTHING, db_column='kd_pj', primary_key=True)
    usere = models.CharField(max_length=700, blank=True, null=True)
    passworde = models.CharField(max_length=700, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'password_asuransi'
        unique_together = (('usere', 'passworde'),)
       
        
class UbahPenjab(models.Model):
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat')
    tgl_ubah = models.DateTimeField()
    kd_pj1 = models.ForeignKey(Penjab, on_delete=models.DO_NOTHING, db_column='kd_pj1', related_name='kd_pj1_ubah_penjab')
    kd_pj2 = models.ForeignKey(Penjab, on_delete=models.DO_NOTHING, db_column='kd_pj2', related_name='kd_pj2_ubah_penjab')

    class Meta:
        managed = False
        db_table = 'ubah_penjab'



############ BPJS

class Gambar(models.Model):
    inde = models.IntegerField(primary_key=True)
    bpjs = models.TextField()
    nyeri = models.TextField()
    inhealth = models.TextField()
    lokalis = models.TextField()
    fisikfisio = models.TextField()

    class Meta:
        managed = False
        db_table = 'gambar'


class Bpjs(models.Model):
    stts = models.CharField(primary_key=True, max_length=5)
    biaya = models.FloatField()

    class Meta:
        managed = False
        db_table = 'bpjs'
        
        
class BridgingSep(models.Model):
    no_sep = models.CharField(primary_key=True, max_length=40)
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', blank=True, null=True)
    tglsep = models.DateField(blank=True, null=True)
    tglrujukan = models.DateField(blank=True, null=True)
    no_rujukan = models.CharField(max_length=40, blank=True, null=True)
    kdppkrujukan = models.CharField(max_length=12, blank=True, null=True)
    nmppkrujukan = models.CharField(max_length=200, blank=True, null=True)
    kdppkpelayanan = models.CharField(max_length=12, blank=True, null=True)
    nmppkpelayanan = models.CharField(max_length=200, blank=True, null=True)
    jnspelayanan = models.CharField(max_length=1, blank=True, null=True)
    catatan = models.CharField(max_length=100, blank=True, null=True)
    diagawal = models.CharField(max_length=10, blank=True, null=True)
    nmdiagnosaawal = models.CharField(max_length=400, blank=True, null=True)
    kdpolitujuan = models.CharField(max_length=15, blank=True, null=True)
    nmpolitujuan = models.CharField(max_length=50, blank=True, null=True)
    klsrawat = models.CharField(max_length=1, blank=True, null=True)
    klsnaik = models.CharField(max_length=1)
    pembiayaan = models.CharField(max_length=1)
    pjnaikkelas = models.CharField(max_length=100)
    lakalantas = models.CharField(max_length=1, blank=True, null=True)
    user = models.CharField(max_length=25, blank=True, null=True)
    nomr = models.CharField(max_length=15, blank=True, null=True)
    nama_pasien = models.CharField(max_length=100, blank=True, null=True)
    tanggal_lahir = models.DateField(blank=True, null=True)
    peserta = models.CharField(max_length=100, blank=True, null=True)
    jkel = models.CharField(max_length=1, blank=True, null=True)
    no_kartu = models.CharField(max_length=25, blank=True, null=True)
    tglpulang = models.DateTimeField(blank=True, null=True)
    asal_rujukan = models.CharField(max_length=15)
    eksekutif = models.CharField(max_length=8)
    cob = models.CharField(max_length=8)
    notelep = models.CharField(max_length=40)
    katarak = models.CharField(max_length=8)
    tglkkl = models.DateField()
    keterangankkl = models.CharField(max_length=100)
    suplesi = models.CharField(max_length=8)
    no_sep_suplesi = models.CharField(max_length=40)
    kdprop = models.CharField(max_length=10)
    nmprop = models.CharField(max_length=50)
    kdkab = models.CharField(max_length=10)
    nmkab = models.CharField(max_length=50)
    kdkec = models.CharField(max_length=10)
    nmkec = models.CharField(max_length=50)
    noskdp = models.CharField(max_length=40)
    kddpjp = models.CharField(max_length=10)
    nmdpdjp = models.CharField(max_length=100)
    tujuankunjungan = models.CharField(max_length=1)
    flagprosedur = models.CharField(max_length=1)
    penunjang = models.CharField(max_length=2)
    asesmenpelayanan = models.CharField(max_length=1)
    kddpjplayanan = models.CharField(max_length=10)
    nmdpjplayanan = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'bridging_sep'


class BpjsPrb(models.Model):
    no_sep = models.OneToOneField('BridgingSep', on_delete=models.DO_NOTHING, db_column='no_sep', primary_key=True)
    prb = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bpjs_prb'


class BridgingRujukanBpjs(models.Model):
    no_sep = models.ForeignKey('BridgingSep', on_delete=models.DO_NOTHING, db_column='no_sep')
    tglrujukan = models.DateField(db_column='tglRujukan', blank=True, null=True)  # Field name made lowercase.
    tglrencanakunjungan = models.DateField(db_column='tglRencanaKunjungan')  # Field name made lowercase.
    ppkdirujuk = models.CharField(db_column='ppkDirujuk', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nm_ppkdirujuk = models.CharField(db_column='nm_ppkDirujuk', max_length=100, blank=True, null=True)  # Field name made lowercase.
    jnspelayanan = models.CharField(db_column='jnsPelayanan', max_length=1, blank=True, null=True)  # Field name made lowercase.
    catatan = models.CharField(max_length=200, blank=True, null=True)
    diagrujukan = models.CharField(db_column='diagRujukan', max_length=10, blank=True, null=True)  # Field name made lowercase.
    nama_diagrujukan = models.CharField(db_column='nama_diagRujukan', max_length=400, blank=True, null=True)  # Field name made lowercase.
    tiperujukan = models.CharField(db_column='tipeRujukan', max_length=14, blank=True, null=True)  # Field name made lowercase.
    polirujukan = models.CharField(db_column='poliRujukan', max_length=15, blank=True, null=True)  # Field name made lowercase.
    nama_polirujukan = models.CharField(db_column='nama_poliRujukan', max_length=50, blank=True, null=True)  # Field name made lowercase.
    no_rujukan = models.CharField(primary_key=True, max_length=40)
    user = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bridging_rujukan_bpjs'


class BridgingRujukanBpjsKhusus(models.Model):
    no_rujukan = models.OneToOneField(BridgingRujukanBpjs, on_delete=models.DO_NOTHING, db_column='no_rujukan', primary_key=True)
    nokapst = models.CharField(max_length=25, blank=True, null=True)
    nmpst = models.CharField(max_length=100, blank=True, null=True)
    tglrujukan_awal = models.DateField(blank=True, null=True)
    tglrujukan_berakhir = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bridging_rujukan_bpjs_khusus'


class BridgingRujukanBpjsKhususDiagnosa(models.Model):
    no_rujukan = models.OneToOneField(BridgingRujukanBpjs, on_delete=models.DO_NOTHING, db_column='no_rujukan', primary_key=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    kode_diagnosa = models.CharField(max_length=10)
    nama_diagnosa = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bridging_rujukan_bpjs_khusus_diagnosa'
        unique_together = (('no_rujukan', 'kode_diagnosa'),)


class BridgingRujukanBpjsKhususProsedur(models.Model):
    no_rujukan = models.OneToOneField(BridgingRujukanBpjs, on_delete=models.DO_NOTHING, db_column='no_rujukan', primary_key=True)
    kode_prosedur = models.CharField(max_length=10)
    nama_prosedur = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bridging_rujukan_bpjs_khusus_prosedur'
        unique_together = (('no_rujukan', 'kode_prosedur'),)


class BridgingSepInternal(models.Model):
    no_sep = models.ForeignKey(BridgingSep, on_delete=models.DO_NOTHING, db_column='no_sep')
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', blank=True, null=True)
    tglsep = models.DateField(blank=True, null=True)
    tglrujukan = models.DateField(blank=True, null=True)
    no_rujukan = models.CharField(max_length=40, blank=True, null=True)
    kdppkrujukan = models.CharField(max_length=12, blank=True, null=True)
    nmppkrujukan = models.CharField(max_length=200, blank=True, null=True)
    kdppkpelayanan = models.CharField(max_length=12, blank=True, null=True)
    nmppkpelayanan = models.CharField(max_length=200, blank=True, null=True)
    jnspelayanan = models.CharField(max_length=1, blank=True, null=True)
    catatan = models.CharField(max_length=100, blank=True, null=True)
    diagawal = models.CharField(max_length=10, blank=True, null=True)
    nmdiagnosaawal = models.CharField(max_length=400, blank=True, null=True)
    kdpolitujuan = models.CharField(max_length=15, blank=True, null=True)
    nmpolitujuan = models.CharField(max_length=50, blank=True, null=True)
    klsrawat = models.CharField(max_length=1, blank=True, null=True)
    klsnaik = models.CharField(max_length=1)
    pembiayaan = models.CharField(max_length=1)
    pjnaikkelas = models.CharField(max_length=100)
    lakalantas = models.CharField(max_length=1, blank=True, null=True)
    user = models.CharField(max_length=25, blank=True, null=True)
    nomr = models.CharField(max_length=15, blank=True, null=True)
    nama_pasien = models.CharField(max_length=100, blank=True, null=True)
    tanggal_lahir = models.DateField(blank=True, null=True)
    peserta = models.CharField(max_length=100, blank=True, null=True)
    jkel = models.CharField(max_length=1, blank=True, null=True)
    no_kartu = models.CharField(max_length=25, blank=True, null=True)
    tglpulang = models.DateTimeField(blank=True, null=True)
    asal_rujukan = models.CharField(max_length=15)
    eksekutif = models.CharField(max_length=8)
    cob = models.CharField(max_length=8)
    notelep = models.CharField(max_length=40)
    katarak = models.CharField(max_length=8)
    tglkkl = models.DateField()
    keterangankkl = models.CharField(max_length=100)
    suplesi = models.CharField(max_length=8)
    no_sep_suplesi = models.CharField(max_length=40)
    kdprop = models.CharField(max_length=10)
    nmprop = models.CharField(max_length=50)
    kdkab = models.CharField(max_length=10)
    nmkab = models.CharField(max_length=50)
    kdkec = models.CharField(max_length=10)
    nmkec = models.CharField(max_length=50)
    noskdp = models.CharField(max_length=40)
    kddpjp = models.CharField(max_length=10)
    nmdpdjp = models.CharField(max_length=100)
    tujuankunjungan = models.CharField(max_length=1)
    flagprosedur = models.CharField(max_length=1)
    penunjang = models.CharField(max_length=2)
    asesmenpelayanan = models.CharField(max_length=1)
    kddpjplayanan = models.CharField(max_length=10)
    nmdpjplayanan = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'bridging_sep_internal'


class BridgingSrbBpjs(models.Model):
    no_sep = models.OneToOneField(BridgingSep, on_delete=models.DO_NOTHING, db_column='no_sep', primary_key=True)
    no_srb = models.CharField(max_length=10)
    tgl_srb = models.DateField(blank=True, null=True)
    alamat = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    kodeprogram = models.CharField(max_length=3, blank=True, null=True)
    namaprogram = models.CharField(max_length=70, blank=True, null=True)
    kodedpjp = models.CharField(max_length=10, blank=True, null=True)
    nmdpjp = models.CharField(max_length=100, blank=True, null=True)
    user = models.CharField(max_length=25, blank=True, null=True)
    keterangan = models.CharField(max_length=100, blank=True, null=True)
    saran = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bridging_srb_bpjs'
        unique_together = (('no_sep', 'no_srb'),)


class BridgingSrbBpjsObat(models.Model):
    no_sep = models.ForeignKey(BridgingSep, on_delete=models.DO_NOTHING, db_column='no_sep', blank=True, null=True)
    no_srb = models.CharField(max_length=10, blank=True, null=True)
    kd_obat = models.CharField(max_length=15, blank=True, null=True)
    nm_obat = models.CharField(max_length=80, blank=True, null=True)
    jumlah = models.FloatField(blank=True, null=True)
    signa1 = models.CharField(max_length=30, blank=True, null=True)
    signa2 = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bridging_srb_bpjs_obat'


class BridgingSuratKontrolBpjs(models.Model):
    no_sep = models.ForeignKey(BridgingSep, on_delete=models.DO_NOTHING, db_column='no_sep', blank=True, null=True)
    tgl_surat = models.DateField()
    no_surat = models.CharField(primary_key=True, max_length=40)
    tgl_rencana = models.DateField(blank=True, null=True)
    kd_dokter_bpjs = models.CharField(max_length=20, blank=True, null=True)
    nm_dokter_bpjs = models.CharField(max_length=50, blank=True, null=True)
    kd_poli_bpjs = models.CharField(max_length=15, blank=True, null=True)
    nm_poli_bpjs = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bridging_surat_kontrol_bpjs'


class BridgingSuratPriBpjs(models.Model):
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', blank=True, null=True)
    no_kartu = models.CharField(max_length=25, blank=True, null=True)
    tgl_surat = models.DateField()
    no_surat = models.CharField(primary_key=True, max_length=40)
    tgl_rencana = models.DateField(blank=True, null=True)
    kd_dokter_bpjs = models.CharField(max_length=20, blank=True, null=True)
    nm_dokter_bpjs = models.CharField(max_length=50, blank=True, null=True)
    kd_poli_bpjs = models.CharField(max_length=15, blank=True, null=True)
    nm_poli_bpjs = models.CharField(max_length=40, blank=True, null=True)
    diagnosa = models.CharField(max_length=130)
    no_sep = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'bridging_surat_pri_bpjs'


class MapingDokterDpjpvclaim(models.Model):
    kd_dokter = models.OneToOneField('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter', primary_key=True)
    kd_dokter_bpjs = models.CharField(max_length=20, blank=True, null=True)
    nm_dokter_bpjs = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maping_dokter_dpjpvclaim'


class MapingDokterPcare(models.Model):
    kd_dokter = models.OneToOneField('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter', primary_key=True)
    kd_dokter_pcare = models.CharField(max_length=20, blank=True, null=True)
    nm_dokter_pcare = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maping_dokter_pcare'


class MapingPoliBpjs(models.Model):
    kd_poli_rs = models.OneToOneField('bangsal.Poliklinik', on_delete=models.DO_NOTHING, db_column='kd_poli_rs', primary_key=True)
    kd_poli_bpjs = models.CharField(unique=True, max_length=15)
    nm_poli_bpjs = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'maping_poli_bpjs'


class MapingPoliklinikPcare(models.Model):
    kd_poli_rs = models.OneToOneField('bangsal.Poliklinik', on_delete=models.DO_NOTHING, db_column='kd_poli_rs', primary_key=True)
    kd_poli_pcare = models.CharField(max_length=5, blank=True, null=True)
    nm_poli_pcare = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maping_poliklinik_pcare'


class MapingTindakanPcare(models.Model):
    kd_jenis_prw = models.OneToOneField('ralan.JnsPerawatan', on_delete=models.DO_NOTHING, db_column='kd_jenis_prw', primary_key=True)
    kd_tindakan_pcare = models.CharField(max_length=15, blank=True, null=True)
    nm_tindakan_pcare = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maping_tindakan_pcare'


class MapingTindakanRanapPcare(models.Model):
    kd_jenis_prw = models.OneToOneField('ranap.JnsPerawatanInap', on_delete=models.DO_NOTHING, db_column='kd_jenis_prw', primary_key=True)
    kd_tindakan_pcare = models.CharField(max_length=15, blank=True, null=True)
    nm_tindakan_pcare = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maping_tindakan_ranap_pcare'


class ReferensiMobilejknBpjs(models.Model):
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', blank=True, null=True)
    nomorkartu = models.CharField(max_length=25, blank=True, null=True)
    nik = models.CharField(max_length=30, blank=True, null=True)
    nohp = models.CharField(max_length=15, blank=True, null=True)
    kodepoli = models.CharField(max_length=15, blank=True, null=True)
    pasienbaru = models.CharField(max_length=1)
    norm = models.CharField(max_length=15, blank=True, null=True)
    tanggalperiksa = models.DateField(blank=True, null=True)
    kodedokter = models.CharField(max_length=20, blank=True, null=True)
    jampraktek = models.CharField(max_length=12, blank=True, null=True)
    jeniskunjungan = models.CharField(max_length=20, blank=True, null=True)
    nomorreferensi = models.CharField(primary_key=True, max_length=40)
    nomorantrean = models.CharField(max_length=15)
    angkaantrean = models.CharField(max_length=5)
    estimasidilayani = models.CharField(max_length=15)
    sisakuotajkn = models.IntegerField()
    kuotajkn = models.IntegerField()
    sisakuotanonjkn = models.IntegerField()
    kuotanonjkn = models.IntegerField()
    status = models.CharField(max_length=7)
    validasi = models.DateTimeField()
    statuskirim = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'referensi_mobilejkn_bpjs'


class ReferensiMobilejknBpjsBatal(models.Model):
    no_rkm_medis = models.ForeignKey('pasien.Pasien', on_delete=models.DO_NOTHING, db_column='no_rkm_medis')
    no_rawat_batal = models.CharField(max_length=17, blank=True, null=True)
    nomorreferensi = models.CharField(primary_key=True, max_length=40)
    tanggalbatal = models.DateTimeField(blank=True, null=True)
    keterangan = models.CharField(max_length=200, blank=True, null=True)
    statuskirim = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'referensi_mobilejkn_bpjs_batal'


class ReferensiMobilejknBpjsTaskid(models.Model):
    no_rawat = models.OneToOneField(ReferensiMobilejknBpjs, on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    taskid = models.CharField(max_length=1)
    waktu = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'referensi_mobilejkn_bpjs_taskid'
        unique_together = (('no_rawat', 'taskid'),)


class RvpKlaimBpjs(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    tanggal_rvp = models.DateField(blank=True, null=True)
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip', blank=True, null=True)
    totalpiutang = models.FloatField(blank=True, null=True)
    uangmuka = models.FloatField(blank=True, null=True)
    sudahdibayar = models.FloatField(blank=True, null=True)
    sisapiutang = models.FloatField(blank=True, null=True)
    tarifinacbg = models.FloatField(blank=True, null=True)
    dibayarbpjs = models.FloatField(blank=True, null=True)
    persenbayar = models.FloatField(blank=True, null=True)
    rugi = models.FloatField(blank=True, null=True)
    lebih = models.FloatField(blank=True, null=True)
    materialralan = models.FloatField(blank=True, null=True)
    bhpralan = models.FloatField(blank=True, null=True)
    tarif_tindakandrralan = models.FloatField(blank=True, null=True)
    tarif_tindakanprralan = models.FloatField(blank=True, null=True)
    ksoralan = models.FloatField(blank=True, null=True)
    menejemenralan = models.FloatField(blank=True, null=True)
    biaya_rawatralan = models.FloatField(blank=True, null=True)
    materialranap = models.FloatField(blank=True, null=True)
    bhpranap = models.FloatField(blank=True, null=True)
    tarif_tindakandrranap = models.FloatField(blank=True, null=True)
    tarif_tindakanprranap = models.FloatField(blank=True, null=True)
    ksoranap = models.FloatField(blank=True, null=True)
    menejemenranap = models.FloatField(blank=True, null=True)
    biaya_rawatranap = models.FloatField(blank=True, null=True)
    bagian_rslabralan = models.FloatField(blank=True, null=True)
    bhplabralan = models.FloatField(blank=True, null=True)
    tarif_perujuklabralan = models.FloatField(blank=True, null=True)
    tarif_tindakan_dokterlabralan = models.FloatField(blank=True, null=True)
    tarif_tindakan_petugaslabralan = models.FloatField(blank=True, null=True)
    ksolabralan = models.FloatField(blank=True, null=True)
    menejemenlabralan = models.FloatField(blank=True, null=True)
    biayalabralan = models.FloatField(blank=True, null=True)
    bagian_rslabranap = models.FloatField(blank=True, null=True)
    bhplabranap = models.FloatField(blank=True, null=True)
    tarif_perujuklabranap = models.FloatField(blank=True, null=True)
    tarif_tindakan_dokterlabranap = models.FloatField(blank=True, null=True)
    tarif_tindakan_petugaslabranap = models.FloatField(blank=True, null=True)
    ksolabranap = models.FloatField(blank=True, null=True)
    menejemenlabranap = models.FloatField(blank=True, null=True)
    biayalabranap = models.FloatField(blank=True, null=True)
    bagian_rsradiologiralan = models.FloatField(blank=True, null=True)
    bhpradiologiralan = models.FloatField(blank=True, null=True)
    tarif_perujukradiologiralan = models.FloatField(blank=True, null=True)
    tarif_tindakan_dokterradiologiralan = models.FloatField(blank=True, null=True)
    tarif_tindakan_petugasradiologiralan = models.FloatField(blank=True, null=True)
    ksoradiologiralan = models.FloatField(blank=True, null=True)
    menejemenradiologiralan = models.FloatField(blank=True, null=True)
    biayaradiologiralan = models.FloatField(blank=True, null=True)
    bagian_rsradiologiranap = models.FloatField(blank=True, null=True)
    bhpradiologiranap = models.FloatField(blank=True, null=True)
    tarif_perujukradiologiranap = models.FloatField(blank=True, null=True)
    tarif_tindakan_dokterradiologiranap = models.FloatField(blank=True, null=True)
    tarif_tindakan_petugasradiologiranap = models.FloatField(blank=True, null=True)
    ksoradiologiranap = models.FloatField(blank=True, null=True)
    menejemenradiologiranap = models.FloatField(blank=True, null=True)
    biayaradiologiranap = models.FloatField(blank=True, null=True)
    jmdokteroperasiralan = models.FloatField(blank=True, null=True)
    jmparamedisoperasiralan = models.FloatField(blank=True, null=True)
    bhpoperasiralan = models.FloatField(blank=True, null=True)
    pendapatanoperasiralan = models.FloatField(blank=True, null=True)
    jmdokteroperasiranap = models.FloatField(blank=True, null=True)
    jmparamedisoperasiranap = models.FloatField(blank=True, null=True)
    bhpoperasiranap = models.FloatField(blank=True, null=True)
    pendapatanoperasiranap = models.FloatField(blank=True, null=True)
    obatlangsung = models.FloatField(blank=True, null=True)
    obatralan = models.FloatField(blank=True, null=True)
    hppobatralan = models.FloatField(blank=True, null=True)
    obatranap = models.FloatField(blank=True, null=True)
    hppobatranap = models.FloatField(blank=True, null=True)
    returobat = models.FloatField(blank=True, null=True)
    tambahanbiaya = models.FloatField(blank=True, null=True)
    potonganbiaya = models.FloatField(blank=True, null=True)
    kamar = models.FloatField(blank=True, null=True)
    reseppulang = models.FloatField(blank=True, null=True)
    harianranap = models.FloatField(blank=True, null=True)
    registrasi = models.FloatField(blank=True, null=True)
    no_sep = models.CharField(max_length=40)
    kd_rek = models.ForeignKey('keuangan.Rekening', on_delete=models.DO_NOTHING, db_column='kd_rek', related_name='kd_rek_rvp_klaim_bpjs')
    kd_rek_kontra = models.ForeignKey('keuangan.Rekening', on_delete=models.DO_NOTHING, db_column='kd_rek_kontra', related_name='kd_rek_kontra_rvp_klaim_bpjs')
    service = models.FloatField()

    class Meta:
        managed = False
        db_table = 'rvp_klaim_bpjs'


class SkdpBpjs(models.Model):
    tahun = models.TextField(primary_key=True)  # This field type is a guess.
    no_rkm_medis = models.ForeignKey('pasien.Pasien', on_delete=models.DO_NOTHING, db_column='no_rkm_medis', blank=True, null=True)
    diagnosa = models.CharField(max_length=50)
    terapi = models.CharField(max_length=50)
    alasan1 = models.CharField(max_length=50, blank=True, null=True)
    alasan2 = models.CharField(max_length=50, blank=True, null=True)
    rtl1 = models.CharField(max_length=50, blank=True, null=True)
    rtl2 = models.CharField(max_length=50, blank=True, null=True)
    tanggal_datang = models.DateField(blank=True, null=True)
    tanggal_rujukan = models.DateField()
    no_antrian = models.CharField(max_length=6)
    kd_dokter = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter', blank=True, null=True)
    status = models.CharField(max_length=13)

    class Meta:
        managed = False
        db_table = 'skdp_bpjs'
        unique_together = (('tahun', 'no_antrian'),)


############ INHEALTH

class BridgingInhealth(models.Model):
    no_sjp = models.CharField(primary_key=True, max_length=40)
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', blank=True, null=True)
    tglsep = models.DateTimeField(blank=True, null=True)
    tglrujukan = models.DateTimeField(blank=True, null=True)
    no_rujukan = models.CharField(max_length=30, blank=True, null=True)
    kdppkrujukan = models.CharField(max_length=12, blank=True, null=True)
    nmppkrujukan = models.CharField(max_length=200, blank=True, null=True)
    kdppkpelayanan = models.CharField(max_length=12, blank=True, null=True)
    nmppkpelayanan = models.CharField(max_length=200, blank=True, null=True)
    jnspelayanan = models.CharField(max_length=1, blank=True, null=True)
    catatan = models.CharField(max_length=100, blank=True, null=True)
    diagawal = models.CharField(max_length=10, blank=True, null=True)
    nmdiagnosaawal = models.CharField(max_length=100, blank=True, null=True)
    diagawal2 = models.CharField(max_length=10)
    nmdiagnosaawal2 = models.CharField(max_length=100)
    kdpolitujuan = models.CharField(max_length=5, blank=True, null=True)
    nmpolitujuan = models.CharField(max_length=50, blank=True, null=True)
    klsrawat = models.CharField(max_length=3, blank=True, null=True)
    klsdesc = models.CharField(max_length=50, blank=True, null=True)
    kdbu = models.CharField(max_length=12, blank=True, null=True)
    nmbu = models.CharField(max_length=200, blank=True, null=True)
    lakalantas = models.CharField(max_length=1, blank=True, null=True)
    lokasilaka = models.CharField(max_length=100, blank=True, null=True)
    user = models.CharField(max_length=25, blank=True, null=True)
    nomr = models.CharField(max_length=15, blank=True, null=True)
    nama_pasien = models.CharField(max_length=100, blank=True, null=True)
    tanggal_lahir = models.DateField(blank=True, null=True)
    jkel = models.CharField(max_length=9, blank=True, null=True)
    no_kartu = models.CharField(max_length=25, blank=True, null=True)
    tglpulang = models.DateTimeField(blank=True, null=True)
    plan = models.CharField(max_length=35)
    plandesc = models.CharField(max_length=100)
    idakomodasi = models.CharField(max_length=20, blank=True, null=True)
    tipesjp = models.CharField(max_length=35, blank=True, null=True)
    tipecob = models.CharField(max_length=35, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bridging_inhealth'


class InhealthJenpelRuangRawat(models.Model):
    kd_kamar = models.OneToOneField('bangsal.Kamar', on_delete=models.DO_NOTHING, db_column='kd_kamar', primary_key=True)
    kode_jenpel_ruang_rawat = models.CharField(max_length=20)
    nama_jenpel_ruang_rawat = models.CharField(max_length=100, blank=True, null=True)
    tarif = models.FloatField()

    class Meta:
        managed = False
        db_table = 'inhealth_jenpel_ruang_rawat'


class InhealthMapingDokter(models.Model):
    kd_dokter = models.OneToOneField('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter', primary_key=True)
    kd_inhealth = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inhealth_maping_dokter'


class InhealthMapingPoli(models.Model):
    kd_poli_rs = models.OneToOneField('bangsal.Poliklinik', on_delete=models.DO_NOTHING, db_column='kd_poli_rs', primary_key=True)
    kd_poli_inhealth = models.CharField(max_length=15, blank=True, null=True)
    nm_poli_inhealth = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inhealth_maping_poli'


class InhealthTindakanLaborat(models.Model):
    kd_jenis_prw = models.OneToOneField('laboratorium.JnsPerawatanLab', on_delete=models.DO_NOTHING, db_column='kd_jenis_prw', primary_key=True)
    kd_inhealth = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inhealth_tindakan_laborat'


class InhealthTindakanOperasi(models.Model):
    kode_paket = models.OneToOneField('ranap.PaketOperasi', on_delete=models.DO_NOTHING, db_column='kode_paket', primary_key=True)
    kd_inhealth = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inhealth_tindakan_operasi'


class InhealthTindakanRadiologi(models.Model):
    kd_jenis_prw = models.OneToOneField('radiologi.JnsPerawatanRadiologi', on_delete=models.DO_NOTHING, db_column='kd_jenis_prw', primary_key=True)
    kd_inhealth = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inhealth_tindakan_radiologi'


class InhealthTindakanRalan(models.Model):
    kd_jenis_prw = models.OneToOneField('ralan.JnsPerawatan', on_delete=models.DO_NOTHING, db_column='kd_jenis_prw', primary_key=True)
    kd_inhealth = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inhealth_tindakan_ralan'


class InhealthTindakanRanap(models.Model):
    kd_jenis_prw = models.OneToOneField('ranap.JnsPerawatanInap', on_delete=models.DO_NOTHING, db_column='kd_jenis_prw', primary_key=True)
    kd_inhealth = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inhealth_tindakan_ranap'

