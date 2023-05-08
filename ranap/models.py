from django.db import models

# Create your models here.


class JnsPerawatanInap(models.Model):
    kd_jenis_prw = models.CharField(primary_key=True, max_length=15)
    nm_perawatan = models.CharField(max_length=80, blank=True, null=True)
    kd_kategori = models.ForeignKey('ralan.KategoriPerawatan', on_delete=models.DO_NOTHING, db_column='kd_kategori')
    material = models.FloatField(blank=True, null=True)
    bhp = models.FloatField()
    tarif_tindakandr = models.FloatField(blank=True, null=True)
    tarif_tindakanpr = models.FloatField(blank=True, null=True)
    kso = models.FloatField(blank=True, null=True)
    menejemen = models.FloatField(blank=True, null=True)
    total_byrdr = models.FloatField(blank=True, null=True)
    total_byrpr = models.FloatField(blank=True, null=True)
    total_byrdrpr = models.FloatField()
    kd_pj = models.ForeignKey('asuransi.Penjab', on_delete=models.DO_NOTHING, db_column='kd_pj')
    kd_bangsal = models.ForeignKey('bangsal.Bangsal', on_delete=models.DO_NOTHING, db_column='kd_bangsal')
    status = models.CharField(max_length=1)
    kelas = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'jns_perawatan_inap'


class PemeriksaanRanap(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    tgl_perawatan = models.DateField()
    jam_rawat = models.TimeField()
    suhu_tubuh = models.CharField(max_length=5, blank=True, null=True)
    tensi = models.CharField(max_length=8)
    nadi = models.CharField(max_length=3, blank=True, null=True)
    respirasi = models.CharField(max_length=3, blank=True, null=True)
    tinggi = models.CharField(max_length=5, blank=True, null=True)
    berat = models.CharField(max_length=5, blank=True, null=True)
    gcs = models.CharField(max_length=10, blank=True, null=True)
    kesadaran = models.CharField(max_length=13)
    keluhan = models.CharField(max_length=400, blank=True, null=True)
    pemeriksaan = models.CharField(max_length=400, blank=True, null=True)
    alergi = models.CharField(max_length=50, blank=True, null=True)
    penilaian = models.CharField(max_length=400)
    rtl = models.CharField(max_length=400)
    instruksi = models.CharField(max_length=400)
    nip = models.ForeignKey('pegawai.Pegawai', on_delete=models.DO_NOTHING, db_column='nip')

    class Meta:
        managed = False
        db_table = 'pemeriksaan_ranap'
        unique_together = (('no_rawat', 'tgl_perawatan', 'jam_rawat'),)


class PerkiraanBiayaRanap(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    kd_penyakit = models.ForeignKey('diagnosa.Penyakit', on_delete=models.DO_NOTHING, db_column='kd_penyakit')
    tarif = models.FloatField()

    class Meta:
        managed = False
        db_table = 'perkiraan_biaya_ranap'


class PermintaanRanap(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    tanggal = models.DateField()
    kd_kamar = models.ForeignKey('bangsal.Kamar', on_delete=models.DO_NOTHING, db_column='kd_kamar')
    diagnosa = models.CharField(max_length=50, blank=True, null=True)
    catatan = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permintaan_ranap'


class PenilaianAwalKeperawatanKebidananRanap(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    tanggal = models.DateTimeField()
    informasi = models.CharField(max_length=13)
    tiba_diruang_rawat = models.CharField(max_length=19)
    cara_masuk = models.CharField(max_length=9)
    keluhan = models.CharField(max_length=500)
    rpk = models.CharField(max_length=100)
    psk = models.CharField(max_length=100)
    rp = models.CharField(max_length=100)
    alergi = models.CharField(max_length=25)
    komplikasi_sebelumnya = models.CharField(max_length=15)
    keterangan_komplikasi_sebelumnya = models.CharField(max_length=30)
    riwayat_mens_umur = models.CharField(max_length=10)
    riwayat_mens_lamanya = models.CharField(max_length=10)
    riwayat_mens_banyaknya = models.CharField(max_length=10)
    riwayat_mens_siklus = models.CharField(max_length=10)
    riwayat_mens_ket_siklus = models.CharField(max_length=13)
    riwayat_mens_dirasakan = models.CharField(max_length=17)
    riwayat_perkawinan_status = models.CharField(max_length=21)
    riwayat_perkawinan_ket_status = models.CharField(max_length=5)
    riwayat_perkawinan_usia1 = models.CharField(max_length=5)
    riwayat_perkawinan_ket_usia1 = models.CharField(max_length=13)
    riwayat_perkawinan_usia2 = models.CharField(max_length=5)
    riwayat_perkawinan_ket_usia2 = models.CharField(max_length=13)
    riwayat_perkawinan_usia3 = models.CharField(max_length=5)
    riwayat_perkawinan_ket_usia3 = models.CharField(max_length=13)
    riwayat_persalinan_g = models.CharField(max_length=10)
    riwayat_persalinan_p = models.CharField(max_length=10)
    riwayat_persalinan_a = models.CharField(max_length=10)
    riwayat_persalinan_hidup = models.CharField(max_length=10)
    riwayat_hamil_hpht = models.DateField()
    riwayat_hamil_usiahamil = models.CharField(max_length=10)
    riwayat_hamil_tp = models.DateField()
    riwayat_hamil_imunisasi = models.CharField(max_length=12)
    riwayat_hamil_anc = models.CharField(max_length=5)
    riwayat_hamil_ancke = models.CharField(max_length=5)
    riwayat_hamil_ket_ancke = models.CharField(max_length=13)
    riwayat_hamil_keluhan_hamil_muda = models.CharField(max_length=10)
    riwayat_hamil_keluhan_hamil_tua = models.CharField(max_length=10)
    riwayat_kb = models.CharField(max_length=12)
    riwayat_kb_lamanya = models.CharField(max_length=10)
    riwayat_kb_komplikasi = models.CharField(max_length=9)
    riwayat_kb_ket_komplikasi = models.CharField(max_length=50)
    riwayat_kb_kapaberhenti = models.CharField(max_length=20)
    riwayat_kb_alasanberhenti = models.CharField(max_length=50)
    riwayat_genekologi = models.CharField(max_length=17)
    riwayat_kebiasaan_obat = models.CharField(max_length=11)
    riwayat_kebiasaan_ket_obat = models.CharField(max_length=100)
    riwayat_kebiasaan_merokok = models.CharField(max_length=5)
    riwayat_kebiasaan_ket_merokok = models.CharField(max_length=5)
    riwayat_kebiasaan_alkohol = models.CharField(max_length=5)
    riwayat_kebiasaan_ket_alkohol = models.CharField(max_length=5)
    riwayat_kebiasaan_narkoba = models.CharField(max_length=5)
    pemeriksaan_kebidanan_mental = models.CharField(max_length=40)
    pemeriksaan_kebidanan_keadaan_umum = models.CharField(max_length=6)
    pemeriksaan_kebidanan_gcs = models.CharField(max_length=10)
    pemeriksaan_kebidanan_td = models.CharField(max_length=8)
    pemeriksaan_kebidanan_nadi = models.CharField(max_length=5)
    pemeriksaan_kebidanan_rr = models.CharField(max_length=5)
    pemeriksaan_kebidanan_suhu = models.CharField(max_length=5)
    pemeriksaan_kebidanan_spo2 = models.CharField(max_length=5)
    pemeriksaan_kebidanan_bb = models.CharField(max_length=5)
    pemeriksaan_kebidanan_tb = models.CharField(max_length=5)
    pemeriksaan_kebidanan_lila = models.CharField(max_length=5)
    pemeriksaan_kebidanan_tfu = models.CharField(max_length=10)
    pemeriksaan_kebidanan_tbj = models.CharField(max_length=10)
    pemeriksaan_kebidanan_letak = models.CharField(max_length=10)
    pemeriksaan_kebidanan_presentasi = models.CharField(max_length=10)
    pemeriksaan_kebidanan_penurunan = models.CharField(max_length=10)
    pemeriksaan_kebidanan_his = models.CharField(max_length=10)
    pemeriksaan_kebidanan_kekuatan = models.CharField(max_length=10)
    pemeriksaan_kebidanan_lamanya = models.CharField(max_length=5)
    pemeriksaan_kebidanan_djj = models.CharField(max_length=5)
    pemeriksaan_kebidanan_ket_djj = models.CharField(max_length=13)
    pemeriksaan_kebidanan_portio = models.CharField(max_length=10)
    pemeriksaan_kebidanan_pembukaan = models.CharField(max_length=5)
    pemeriksaan_kebidanan_ketuban = models.CharField(max_length=10)
    pemeriksaan_kebidanan_hodge = models.CharField(max_length=10)
    pemeriksaan_kebidanan_panggul = models.CharField(max_length=27)
    pemeriksaan_kebidanan_inspekulo = models.CharField(max_length=9)
    pemeriksaan_kebidanan_ket_inspekulo = models.CharField(max_length=50)
    pemeriksaan_kebidanan_lakmus = models.CharField(max_length=9)
    pemeriksaan_kebidanan_ket_lakmus = models.CharField(max_length=50)
    pemeriksaan_kebidanan_ctg = models.CharField(max_length=9)
    pemeriksaan_kebidanan_ket_ctg = models.CharField(max_length=50)
    pemeriksaan_umum_kepala = models.CharField(max_length=13)
    pemeriksaan_umum_muka = models.CharField(max_length=9)
    pemeriksaan_umum_mata = models.CharField(max_length=22)
    pemeriksaan_umum_hidung = models.CharField(max_length=9)
    pemeriksaan_umum_telinga = models.CharField(max_length=9)
    pemeriksaan_umum_mulut = models.CharField(max_length=9)
    pemeriksaan_umum_leher = models.CharField(max_length=26)
    pemeriksaan_umum_dada = models.CharField(max_length=22)
    pemeriksaan_umum_perut = models.CharField(max_length=19)
    pemeriksaan_umum_genitalia = models.CharField(max_length=9)
    pemeriksaan_umum_ekstrimitas = models.CharField(max_length=19)
    pengkajian_fungsi_kemampuan_aktifitas = models.CharField(max_length=20)
    pengkajian_fungsi_berjalan = models.CharField(max_length=22)
    pengkajian_fungsi_ket_berjalan = models.CharField(max_length=50)
    pengkajian_fungsi_aktivitas = models.CharField(max_length=12)
    pengkajian_fungsi_ambulasi = models.CharField(max_length=17)
    pengkajian_fungsi_ekstrimitas_atas = models.CharField(max_length=14)
    pengkajian_fungsi_ket_ekstrimitas_atas = models.CharField(max_length=50)
    pengkajian_fungsi_ekstrimitas_bawah = models.CharField(max_length=14)
    pengkajian_fungsi_ket_ekstrimitas_bawah = models.CharField(max_length=50)
    pengkajian_fungsi_kemampuan_menggenggam = models.CharField(max_length=19)
    pengkajian_fungsi_ket_kemampuan_menggenggam = models.CharField(max_length=50)
    pengkajian_fungsi_koordinasi = models.CharField(max_length=19)
    pengkajian_fungsi_ket_koordinasi = models.CharField(max_length=50)
    pengkajian_fungsi_gangguan_fungsi = models.CharField(max_length=27)
    riwayat_psiko_kondisipsiko = models.CharField(max_length=17)
    riwayat_psiko_adakah_prilaku = models.CharField(max_length=34)
    riwayat_psiko_ket_adakah_prilaku = models.CharField(max_length=50)
    riwayat_psiko_gangguan_jiwa = models.CharField(max_length=5)
    riwayat_psiko_hubungan_pasien = models.CharField(max_length=15)
    riwayat_psiko_tinggal_dengan = models.CharField(max_length=11)
    riwayat_psiko_ket_tinggal_dengan = models.CharField(max_length=50)
    riwayat_psiko_budaya = models.CharField(max_length=9)
    riwayat_psiko_ket_budaya = models.CharField(max_length=50)
    riwayat_psiko_pend_pj = models.CharField(max_length=14)
    riwayat_psiko_edukasi_pada = models.CharField(max_length=8)
    riwayat_psiko_ket_edukasi_pada = models.CharField(max_length=50)
    penilaian_nyeri = models.CharField(max_length=15)
    penilaian_nyeri_penyebab = models.CharField(max_length=15)
    penilaian_nyeri_ket_penyebab = models.CharField(max_length=50)
    penilaian_nyeri_kualitas = models.CharField(max_length=16)
    penilaian_nyeri_ket_kualitas = models.CharField(max_length=50)
    penilaian_nyeri_lokasi = models.CharField(max_length=50)
    penilaian_nyeri_menyebar = models.CharField(max_length=5)
    penilaian_nyeri_skala = models.CharField(max_length=2)
    penilaian_nyeri_waktu = models.CharField(max_length=5)
    penilaian_nyeri_hilang = models.CharField(max_length=14)
    penilaian_nyeri_ket_hilang = models.CharField(max_length=50)
    penilaian_nyeri_diberitahukan_dokter = models.CharField(max_length=5)
    penilaian_nyeri_jam_diberitahukan_dokter = models.CharField(max_length=10)
    penilaian_jatuh_skala1 = models.CharField(max_length=5)
    penilaian_jatuh_nilai1 = models.IntegerField()
    penilaian_jatuh_skala2 = models.CharField(max_length=5)
    penilaian_jatuh_nilai2 = models.IntegerField()
    penilaian_jatuh_skala3 = models.CharField(max_length=41)
    penilaian_jatuh_nilai3 = models.IntegerField()
    penilaian_jatuh_skala4 = models.CharField(max_length=5)
    penilaian_jatuh_nilai4 = models.IntegerField()
    penilaian_jatuh_skala5 = models.CharField(max_length=31)
    penilaian_jatuh_nilai5 = models.IntegerField()
    penilaian_jatuh_skala6 = models.CharField(max_length=43)
    penilaian_jatuh_nilai6 = models.IntegerField()
    penilaian_jatuh_totalnilai = models.FloatField()
    skrining_gizi1 = models.CharField(max_length=50)
    nilai_gizi1 = models.IntegerField()
    skrining_gizi2 = models.CharField(max_length=5)
    nilai_gizi2 = models.IntegerField()
    nilai_total_gizi = models.FloatField()
    skrining_gizi_diagnosa_khusus = models.CharField(max_length=5)
    skrining_gizi_ket_diagnosa_khusus = models.CharField(max_length=50)
    skrining_gizi_diketahui_dietisen = models.CharField(max_length=5)
    skrining_gizi_jam_diketahui_dietisen = models.CharField(max_length=10)
    masalah = models.CharField(max_length=1000)
    rencana = models.CharField(max_length=1000)
    nip1 = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip1', related_name='nip1_penilaian_awal_keperawatan')
    nip2 = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip2', related_name='nip2_penilaian_awal_keperawatan')
    kd_dokter = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter')

    class Meta:
        managed = False
        db_table = 'penilaian_awal_keperawatan_kebidanan_ranap'


class PenilaianMedisRanap(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    tanggal = models.DateTimeField()
    kd_dokter = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter')
    anamnesis = models.CharField(max_length=13)
    hubungan = models.CharField(max_length=100)
    keluhan_utama = models.CharField(max_length=2000)
    rps = models.CharField(max_length=2000)
    rpd = models.CharField(max_length=1000)
    rpk = models.CharField(max_length=1000)
    rpo = models.CharField(max_length=1000)
    alergi = models.CharField(max_length=100)
    keadaan = models.CharField(max_length=12)
    gcs = models.CharField(max_length=10)
    kesadaran = models.CharField(max_length=13)
    td = models.CharField(max_length=8)
    nadi = models.CharField(max_length=5)
    rr = models.CharField(max_length=5)
    suhu = models.CharField(max_length=5)
    spo = models.CharField(max_length=5)
    bb = models.CharField(max_length=5)
    tb = models.CharField(max_length=5)
    kepala = models.CharField(max_length=15)
    mata = models.CharField(max_length=15)
    gigi = models.CharField(max_length=15)
    tht = models.CharField(max_length=15)
    thoraks = models.CharField(max_length=15)
    jantung = models.CharField(max_length=15)
    paru = models.CharField(max_length=15)
    abdomen = models.CharField(max_length=15)
    genital = models.CharField(max_length=15)
    ekstremitas = models.CharField(max_length=15)
    kulit = models.CharField(max_length=15)
    ket_fisik = models.TextField()
    ket_lokalis = models.TextField()
    lab = models.TextField()
    rad = models.TextField()
    penunjang = models.TextField()
    diagnosis = models.CharField(max_length=500)
    tata = models.TextField()
    edukasi = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'penilaian_medis_ranap'


class PenilaianMedisRanapKandungan(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    tanggal = models.DateTimeField()
    kd_dokter = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter')
    anamnesis = models.CharField(max_length=13)
    hubungan = models.CharField(max_length=100)
    keluhan_utama = models.CharField(max_length=2000)
    rps = models.CharField(max_length=2000)
    rpd = models.CharField(max_length=1000)
    rpk = models.CharField(max_length=1000)
    rpo = models.CharField(max_length=1000)
    alergi = models.CharField(max_length=100)
    keadaan = models.CharField(max_length=12)
    gcs = models.CharField(max_length=10)
    kesadaran = models.CharField(max_length=13)
    td = models.CharField(max_length=8)
    nadi = models.CharField(max_length=5)
    rr = models.CharField(max_length=5)
    suhu = models.CharField(max_length=5)
    spo = models.CharField(max_length=5)
    bb = models.CharField(max_length=5)
    tb = models.CharField(max_length=5)
    kepala = models.CharField(max_length=15)
    mata = models.CharField(max_length=15)
    gigi = models.CharField(max_length=15)
    tht = models.CharField(max_length=15)
    thoraks = models.CharField(max_length=15)
    jantung = models.CharField(max_length=15)
    paru = models.CharField(max_length=15)
    abdomen = models.CharField(max_length=15)
    genital = models.CharField(max_length=15)
    ekstremitas = models.CharField(max_length=15)
    kulit = models.CharField(max_length=15)
    ket_fisik = models.TextField()
    tfu = models.CharField(max_length=10)
    tbj = models.CharField(max_length=10)
    his = models.CharField(max_length=10)
    kontraksi = models.CharField(max_length=5)
    djj = models.CharField(max_length=10)
    inspeksi = models.TextField()
    inspekulo = models.TextField()
    vt = models.TextField()
    rt = models.TextField()
    ultra = models.TextField()
    kardio = models.TextField()
    lab = models.TextField()
    diagnosis = models.CharField(max_length=500)
    tata = models.TextField()
    edukasi = models.CharField(max_length=1000)

    class Meta:
        managed = False
        db_table = 'penilaian_medis_ranap_kandungan'


class PerawatanCorona(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    pemulasaraan_jenazah = models.CharField(max_length=5, blank=True, null=True)
    kantong_jenazah = models.CharField(max_length=5, blank=True, null=True)
    peti_jenazah = models.CharField(max_length=5, blank=True, null=True)
    plastik_erat = models.CharField(max_length=5, blank=True, null=True)
    desinfektan_jenazah = models.CharField(max_length=5, blank=True, null=True)
    mobil_jenazah = models.CharField(max_length=5, blank=True, null=True)
    desinfektan_mobil_jenazah = models.CharField(max_length=5, blank=True, null=True)
    covid19_status_cd = models.CharField(max_length=7, blank=True, null=True)
    nomor_kartu_t = models.CharField(max_length=30, blank=True, null=True)
    episodes1 = models.IntegerField(blank=True, null=True)
    episodes2 = models.IntegerField(blank=True, null=True)
    episodes3 = models.IntegerField(blank=True, null=True)
    episodes4 = models.IntegerField(blank=True, null=True)
    episodes5 = models.IntegerField(blank=True, null=True)
    episodes6 = models.IntegerField(blank=True, null=True)
    covid19_cc_ind = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'perawatan_corona'


class RanapGabung(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True, related_name='no_rawat_ranap_gabung')
    no_rawat2 = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat2', related_name='no_rawat2_ranap_gabung')

    class Meta:
        managed = False
        db_table = 'ranap_gabung'
        unique_together = (('no_rawat', 'no_rawat2'),)


class RawatInapDr(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    kd_jenis_prw = models.ForeignKey(JnsPerawatanInap, on_delete=models.DO_NOTHING, db_column='kd_jenis_prw')
    kd_dokter = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter')
    tgl_perawatan = models.DateField()
    jam_rawat = models.TimeField()
    material = models.FloatField()
    bhp = models.FloatField()
    tarif_tindakandr = models.FloatField()
    kso = models.FloatField(blank=True, null=True)
    menejemen = models.FloatField(blank=True, null=True)
    biaya_rawat = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rawat_inap_dr'
        unique_together = (('no_rawat', 'kd_jenis_prw', 'kd_dokter', 'tgl_perawatan', 'jam_rawat'),)


class RawatInapDrpr(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    kd_jenis_prw = models.ForeignKey(JnsPerawatanInap, on_delete=models.DO_NOTHING, db_column='kd_jenis_prw')
    kd_dokter = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter')
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip')
    tgl_perawatan = models.DateField()
    jam_rawat = models.TimeField()
    material = models.FloatField()
    bhp = models.FloatField()
    tarif_tindakandr = models.FloatField(blank=True, null=True)
    tarif_tindakanpr = models.FloatField(blank=True, null=True)
    kso = models.FloatField(blank=True, null=True)
    menejemen = models.FloatField(blank=True, null=True)
    biaya_rawat = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rawat_inap_drpr'
        unique_together = (('no_rawat', 'kd_jenis_prw', 'kd_dokter', 'nip', 'tgl_perawatan', 'jam_rawat'),)


class RawatInapPr(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    kd_jenis_prw = models.ForeignKey(JnsPerawatanInap, on_delete=models.DO_NOTHING, db_column='kd_jenis_prw')
    nip = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='nip')
    tgl_perawatan = models.DateField()
    jam_rawat = models.TimeField()
    material = models.FloatField()
    bhp = models.FloatField()
    tarif_tindakanpr = models.FloatField()
    kso = models.FloatField(blank=True, null=True)
    menejemen = models.FloatField(blank=True, null=True)
    biaya_rawat = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rawat_inap_pr'
        unique_together = (('no_rawat', 'kd_jenis_prw', 'nip', 'tgl_perawatan', 'jam_rawat'),)


class DataKlasifikasiPasienRanap(models.Model):
    tanggal = models.DateField(primary_key=True)
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat')
    minimal = models.CharField(db_column='Minimal', max_length=5, blank=True, null=True)  # Field name made lowercase.
    partial = models.CharField(db_column='Partial', max_length=5, blank=True, null=True)  # Field name made lowercase.
    total = models.CharField(db_column='Total', max_length=5, blank=True, null=True)  # Field name made lowercase.
    kd_kamar = models.ForeignKey('bangsal.Kamar', on_delete=models.DO_NOTHING, db_column='kd_kamar', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_klasifikasi_pasien_ranap'
        unique_together = (('tanggal', 'no_rawat'),)

class DpjpRanap(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    kd_dokter = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter')

    class Meta:
        managed = False
        db_table = 'dpjp_ranap'
        unique_together = (('no_rawat', 'kd_dokter'),)
        
        
class KamarInap(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    kd_kamar = models.ForeignKey('bangsal.Kamar', on_delete=models.DO_NOTHING, db_column='kd_kamar')
    trf_kamar = models.FloatField(blank=True, null=True)
    diagnosa_awal = models.CharField(max_length=100, blank=True, null=True)
    diagnosa_akhir = models.CharField(max_length=100, blank=True, null=True)
    tgl_masuk = models.DateField()
    jam_masuk = models.TimeField()
    tgl_keluar = models.DateField(blank=True, null=True)
    jam_keluar = models.TimeField(blank=True, null=True)
    lama = models.FloatField(blank=True, null=True)
    ttl_biaya = models.FloatField(blank=True, null=True)
    stts_pulang = models.CharField(max_length=23)

    class Meta:
        managed = False
        db_table = 'kamar_inap'
        unique_together = (('no_rawat', 'tgl_masuk', 'jam_masuk'),)
        

class Jumpasien(models.Model):
    thn = models.TextField(primary_key=True)  # This field type is a guess.
    bln = models.IntegerField()
    id = models.ForeignKey('pegawai.Pegawai', on_delete=models.DO_NOTHING, db_column='id')
    jml = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jumpasien'
        unique_together = (('thn', 'bln', 'id'),)
        
        
class CatatanPerawatan(models.Model):
    tanggal = models.DateField(blank=True, null=True)
    jam = models.TimeField(blank=True, null=True)
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', blank=True, null=True)
    kd_dokter = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter', blank=True, null=True)
    catatan = models.CharField(max_length=700, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catatan_perawatan'

        
########### OPERASI


class PaketOperasi(models.Model):
    kode_paket = models.CharField(primary_key=True, max_length=15)
    nm_perawatan = models.CharField(max_length=80)
    kategori = models.CharField(max_length=9, blank=True, null=True)
    operator1 = models.FloatField()
    operator2 = models.FloatField()
    operator3 = models.FloatField()
    asisten_operator1 = models.FloatField(blank=True, null=True)
    asisten_operator2 = models.FloatField()
    asisten_operator3 = models.FloatField(blank=True, null=True)
    instrumen = models.FloatField(blank=True, null=True)
    dokter_anak = models.FloatField()
    perawaat_resusitas = models.FloatField()
    dokter_anestesi = models.FloatField()
    asisten_anestesi = models.FloatField()
    asisten_anestesi2 = models.FloatField(blank=True, null=True)
    bidan = models.FloatField()
    bidan2 = models.FloatField(blank=True, null=True)
    bidan3 = models.FloatField(blank=True, null=True)
    perawat_luar = models.FloatField()
    sewa_ok = models.FloatField()
    alat = models.FloatField()
    akomodasi = models.FloatField(blank=True, null=True)
    bagian_rs = models.FloatField()
    omloop = models.FloatField()
    omloop2 = models.FloatField(blank=True, null=True)
    omloop3 = models.FloatField(blank=True, null=True)
    omloop4 = models.FloatField(blank=True, null=True)
    omloop5 = models.FloatField(blank=True, null=True)
    sarpras = models.FloatField(blank=True, null=True)
    dokter_pjanak = models.FloatField(blank=True, null=True)
    dokter_umum = models.FloatField(blank=True, null=True)
    kd_pj = models.ForeignKey('asuransi.Penjab', on_delete=models.DO_NOTHING, db_column='kd_pj', blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    kelas = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paket_operasi'


class BookingOperasi(models.Model):
    no_rawat = models.ForeignKey('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', blank=True, null=True)
    kode_paket = models.ForeignKey('PaketOperasi', on_delete=models.DO_NOTHING, db_column='kode_paket', blank=True, null=True)
    tanggal = models.DateField(blank=True, null=True)
    jam_mulai = models.TimeField(blank=True, null=True)
    jam_selesai = models.TimeField(blank=True, null=True)
    status = models.CharField(max_length=14, blank=True, null=True)
    kd_dokter = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='kd_dokter', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booking_operasi'
        

class Operasi(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    tgl_operasi = models.DateTimeField()
    jenis_anasthesi = models.CharField(max_length=8)
    kategori = models.CharField(max_length=9, blank=True, null=True)
    operator1 = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='operator1', related_name='operator1_operasi')
    operator2 = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='operator2', related_name='operator2_operasi')
    operator3 = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='operator3', related_name='operator3_operasi')
    asisten_operator1 = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='asisten_operator1', related_name='asisten_operator1_operasi')
    asisten_operator2 = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='asisten_operator2', related_name='asisten_operator2_operasi')
    asisten_operator3 = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='asisten_operator3', blank=True, null=True, related_name='asisten_operator3_operasi')
    instrumen = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='instrumen', blank=True, null=True, related_name='instrumen_operasi')
    dokter_anak = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='dokter_anak', related_name='dokter_anak_operasi')
    perawaat_resusitas = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='perawaat_resusitas', related_name='perawat_resusitasi_operasi')
    dokter_anestesi = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='dokter_anestesi', related_name='dokter_anestesi_operasi')
    asisten_anestesi = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='asisten_anestesi', related_name='asisten_anestesi_operasi')
    asisten_anestesi2 = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='asisten_anestesi2', blank=True, null=True, related_name='asisten_anestesi2_operasi')
    bidan = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='bidan', related_name='bidan_operasi')
    bidan2 = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='bidan2', blank=True, null=True, related_name='bidan2_operasi')
    bidan3 = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='bidan3', blank=True, null=True, related_name='bidan3_operasi')
    perawat_luar = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='perawat_luar', related_name='perawat_luar_operasi')
    omloop = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='omloop', blank=True, null=True, related_name='omloop_operasi')
    omloop2 = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='omloop2', blank=True, null=True, related_name='omloop2_operasi')
    omloop3 = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='omloop3', blank=True, null=True, related_name='omloop3_operasi')
    omloop4 = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='omloop4', blank=True, null=True, related_name='omloop4_operasi')
    omloop5 = models.ForeignKey('pegawai.Petugas', on_delete=models.DO_NOTHING, db_column='omloop5', blank=True, null=True, related_name='omloop5_operasi')
    dokter_pjanak = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='dokter_pjanak', blank=True, null=True, related_name='dokter_pjanak_operasi')
    dokter_umum = models.ForeignKey('pegawai.Dokter', on_delete=models.DO_NOTHING, db_column='dokter_umum', blank=True, null=True, related_name='dokter_umum_operasi')
    kode_paket = models.ForeignKey('PaketOperasi', on_delete=models.DO_NOTHING, db_column='kode_paket')
    biayaoperator1 = models.FloatField()
    biayaoperator2 = models.FloatField()
    biayaoperator3 = models.FloatField()
    biayaasisten_operator1 = models.FloatField()
    biayaasisten_operator2 = models.FloatField()
    biayaasisten_operator3 = models.FloatField(blank=True, null=True)
    biayainstrumen = models.FloatField(blank=True, null=True)
    biayadokter_anak = models.FloatField()
    biayaperawaat_resusitas = models.FloatField()
    biayadokter_anestesi = models.FloatField()
    biayaasisten_anestesi = models.FloatField()
    biayaasisten_anestesi2 = models.FloatField(blank=True, null=True)
    biayabidan = models.FloatField()
    biayabidan2 = models.FloatField(blank=True, null=True)
    biayabidan3 = models.FloatField(blank=True, null=True)
    biayaperawat_luar = models.FloatField()
    biayaalat = models.FloatField()
    biayasewaok = models.FloatField()
    akomodasi = models.FloatField(blank=True, null=True)
    bagian_rs = models.FloatField()
    biaya_omloop = models.FloatField(blank=True, null=True)
    biaya_omloop2 = models.FloatField(blank=True, null=True)
    biaya_omloop3 = models.FloatField(blank=True, null=True)
    biaya_omloop4 = models.FloatField(blank=True, null=True)
    biaya_omloop5 = models.FloatField(blank=True, null=True)
    biayasarpras = models.FloatField(blank=True, null=True)
    biaya_dokter_pjanak = models.FloatField(blank=True, null=True)
    biaya_dokter_umum = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operasi'
        unique_together = (('no_rawat', 'tgl_operasi', 'kode_paket'),)


class LaporanOperasi(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    tanggal = models.DateTimeField()
    diagnosa_preop = models.CharField(max_length=100)
    diagnosa_postop = models.CharField(max_length=100)
    jaringan_dieksekusi = models.CharField(max_length=100)
    selesaioperasi = models.DateTimeField()
    permintaan_pa = models.CharField(max_length=5)
    laporan_operasi = models.TextField()

    class Meta:
        managed = False
        db_table = 'laporan_operasi'
        unique_together = (('no_rawat', 'tanggal'),)


class RetensiPasien(models.Model):
    no_rkm_medis = models.ForeignKey('pasien.Pasien', on_delete=models.DO_NOTHING, db_column='no_rkm_medis', blank=True, null=True)
    terakhir_daftar = models.DateField(blank=True, null=True)
    tgl_retensi = models.DateField(blank=True, null=True)
    lokasi_pdf = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'retensi_pasien'


class PcareTindakanRanapDiberikan(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    nokunjungan = models.CharField(db_column='noKunjungan', max_length=40)  # Field name made lowercase.
    kdtindakansk = models.CharField(db_column='kdTindakanSK', max_length=15, blank=True, null=True)  # Field name made lowercase.
    tgl_perawatan = models.DateField()
    jam = models.TimeField()
    kd_jenis_prw = models.ForeignKey('asuransi.MapingTindakanRanapPcare', on_delete=models.DO_NOTHING, db_column='kd_jenis_prw')
    material = models.FloatField()
    bhp = models.FloatField()
    tarif_tindakandr = models.FloatField()
    tarif_tindakanpr = models.FloatField()
    kso = models.FloatField()
    menejemen = models.FloatField()
    biaya_rawat = models.FloatField()

    class Meta:
        managed = False
        db_table = 'pcare_tindakan_ranap_diberikan'
        unique_together = (('no_rawat', 'nokunjungan', 'tgl_perawatan', 'jam', 'kd_jenis_prw'),)


class PemeriksaanGinekologiRanap(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    tgl_perawatan = models.DateField()
    jam_rawat = models.TimeField()
    inspeksi = models.CharField(max_length=50, blank=True, null=True)
    inspeksi_vulva = models.CharField(max_length=50, blank=True, null=True)
    inspekulo_gine = models.CharField(max_length=50, blank=True, null=True)
    fluxus_gine = models.CharField(max_length=1, blank=True, null=True)
    fluor_gine = models.CharField(max_length=1, blank=True, null=True)
    vulva_inspekulo = models.CharField(max_length=50)
    portio_inspekulo = models.CharField(max_length=50, blank=True, null=True)
    sondage = models.CharField(max_length=50, blank=True, null=True)
    portio_dalam = models.CharField(max_length=50, blank=True, null=True)
    bentuk = models.CharField(max_length=50, blank=True, null=True)
    cavum_uteri = models.CharField(max_length=50, blank=True, null=True)
    mobilitas = models.CharField(max_length=1, blank=True, null=True)
    ukuran = models.CharField(max_length=50, blank=True, null=True)
    nyeri_tekan = models.CharField(max_length=1, blank=True, null=True)
    adnexa_kanan = models.CharField(max_length=50, blank=True, null=True)
    adnexa_kiri = models.CharField(max_length=50)
    cavum_douglas = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'pemeriksaan_ginekologi_ranap'
        unique_together = (('no_rawat', 'tgl_perawatan', 'jam_rawat'),)



class PemeriksaanObstetriRanap(models.Model):
    no_rawat = models.OneToOneField('ralan.RegPeriksa', on_delete=models.DO_NOTHING, db_column='no_rawat', primary_key=True)
    tgl_perawatan = models.DateField()
    jam_rawat = models.TimeField()
    tinggi_uteri = models.CharField(max_length=5, blank=True, null=True)
    janin = models.CharField(max_length=7, blank=True, null=True)
    letak = models.CharField(max_length=50, blank=True, null=True)
    panggul = models.CharField(max_length=3, blank=True, null=True)
    denyut = models.CharField(max_length=5, blank=True, null=True)
    kontraksi = models.CharField(max_length=1, blank=True, null=True)
    kualitas_mnt = models.CharField(max_length=5, blank=True, null=True)
    kualitas_dtk = models.CharField(max_length=5, blank=True, null=True)
    fluksus = models.CharField(max_length=1, blank=True, null=True)
    albus = models.CharField(max_length=1, blank=True, null=True)
    vulva = models.CharField(max_length=50, blank=True, null=True)
    portio = models.CharField(max_length=50, blank=True, null=True)
    dalam = models.CharField(max_length=6, blank=True, null=True)
    tebal = models.CharField(max_length=5, blank=True, null=True)
    arah = models.CharField(max_length=8, blank=True, null=True)
    pembukaan = models.CharField(max_length=50, blank=True, null=True)
    penurunan = models.CharField(max_length=50, blank=True, null=True)
    denominator = models.CharField(max_length=50)
    ketuban = models.CharField(max_length=1, blank=True, null=True)
    feto = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pemeriksaan_obstetri_ranap'
        unique_together = (('no_rawat', 'tgl_perawatan', 'jam_rawat'),)


