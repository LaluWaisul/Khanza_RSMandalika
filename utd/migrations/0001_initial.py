# Generated by Django 4.1 on 2023-03-12 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        # ('farmasi', '0002_initial'),
        ('aset', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JnsPerawatanUtd',
            fields=[
                ('kd_jenis_prw', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('nm_perawatan', models.CharField(blank=True, max_length=80, null=True)),
                ('bagian_rs', models.FloatField(blank=True, null=True)),
                ('bhp', models.FloatField(blank=True, null=True)),
                ('tarif_perujuk', models.FloatField(blank=True, null=True)),
                ('tarif_tindakan_dokter', models.FloatField(blank=True, null=True)),
                ('tarif_tindakan_petugas', models.FloatField(blank=True, null=True)),
                ('kso', models.FloatField(blank=True, null=True)),
                ('manajemen', models.FloatField(blank=True, null=True)),
                ('total_byr', models.FloatField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'jns_perawatan_utd',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TemplateUtd',
            fields=[
                ('id_template', models.AutoField(primary_key=True, serialize=False)),
                ('pemeriksaan', models.CharField(blank=True, max_length=200, null=True)),
                ('nilai_rujukan', models.CharField(max_length=30)),
                ('bagian_rs', models.FloatField(blank=True, null=True)),
                ('bhp', models.FloatField(blank=True, null=True)),
                ('bagian_perujuk', models.FloatField(blank=True, null=True)),
                ('bagian_dokter', models.FloatField(blank=True, null=True)),
                ('petugas_utd', models.FloatField(blank=True, null=True)),
                ('kso', models.FloatField(blank=True, null=True)),
                ('menejemen', models.FloatField(blank=True, null=True)),
                ('biaya_item', models.FloatField(blank=True, null=True)),
                ('urut', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'template_utd',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UtdDetailPemisahanKomponen',
            fields=[
                ('no_kantong', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('kode_komponen', models.CharField(blank=True, max_length=5, null=True)),
                ('tanggal_kadaluarsa', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'utd_detail_pemisahan_komponen',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UtdDonor',
            fields=[
                ('no_donor', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('tanggal', models.DateField(blank=True, null=True)),
                ('dinas', models.CharField(blank=True, max_length=5, null=True)),
                ('tensi', models.CharField(blank=True, max_length=7, null=True)),
                ('no_bag', models.IntegerField(blank=True, null=True)),
                ('jenis_bag', models.CharField(blank=True, max_length=2, null=True)),
                ('jenis_donor', models.CharField(blank=True, max_length=2, null=True)),
                ('tempat_aftap', models.CharField(blank=True, max_length=12, null=True)),
                ('hbsag', models.CharField(blank=True, max_length=7, null=True)),
                ('hcv', models.CharField(blank=True, max_length=7, null=True)),
                ('hiv', models.CharField(blank=True, max_length=7, null=True)),
                ('spilis', models.CharField(blank=True, max_length=7, null=True)),
                ('malaria', models.CharField(blank=True, max_length=7, null=True)),
                ('status', models.CharField(blank=True, max_length=5, null=True)),
            ],
            options={
                'db_table': 'utd_donor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UtdKomponenDarah',
            fields=[
                ('kode', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nama', models.CharField(blank=True, max_length=70, null=True)),
                ('lama', models.SmallIntegerField(blank=True, null=True)),
                ('jasa_sarana', models.FloatField(blank=True, null=True)),
                ('paket_bhp', models.FloatField(blank=True, null=True)),
                ('kso', models.FloatField(blank=True, null=True)),
                ('manajemen', models.FloatField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('pembatalan', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'utd_komponen_darah',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UtdMedisRusak',
            fields=[
                ('kode_brng', models.OneToOneField(db_column='kode_brng', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='farmasi.databarang')),
                ('jml', models.FloatField(blank=True, null=True)),
                ('hargabeli', models.FloatField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('tanggal', models.DateTimeField()),
                ('keterangan', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'db_table': 'utd_medis_rusak',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UtdPendonor',
            fields=[
                ('no_pendonor', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=40)),
                ('no_ktp', models.CharField(max_length=20)),
                ('jk', models.CharField(max_length=1)),
                ('tmp_lahir', models.CharField(max_length=15)),
                ('tgl_lahir', models.DateField()),
                ('alamat', models.CharField(max_length=100)),
                ('golongan_darah', models.CharField(max_length=2)),
                ('resus', models.CharField(max_length=3)),
                ('no_telp', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'utd_pendonor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UtdPengambilanMedis',
            fields=[
                ('kode_brng', models.OneToOneField(db_column='kode_brng', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='farmasi.databarang')),
                ('jml', models.FloatField(blank=True, null=True)),
                ('hargabeli', models.FloatField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('tanggal', models.DateTimeField()),
                ('keterangan', models.CharField(blank=True, max_length=60, null=True)),
                ('no_batch', models.CharField(max_length=20)),
                ('no_faktur', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'utd_pengambilan_medis',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UtdPengambilanPenunjang',
            fields=[
                ('kode_brng', models.OneToOneField(db_column='kode_brng', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='aset.ipsrsbarang')),
                ('jml', models.FloatField(blank=True, null=True)),
                ('harga', models.FloatField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('tanggal', models.DateTimeField()),
                ('keterangan', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'db_table': 'utd_pengambilan_penunjang',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UtdPenunjangRusak',
            fields=[
                ('kode_brng', models.OneToOneField(db_column='kode_brng', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='aset.ipsrsbarang')),
                ('jml', models.FloatField(blank=True, null=True)),
                ('harga', models.FloatField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('tanggal', models.DateTimeField()),
                ('keterangan', models.CharField(blank=True, max_length=60, null=True)),
            ],
            options={
                'db_table': 'utd_penunjang_rusak',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UtdPenyerahanDarah',
            fields=[
                ('no_penyerahan', models.CharField(max_length=17, primary_key=True, serialize=False)),
                ('tanggal', models.DateField(blank=True, null=True)),
                ('dinas', models.CharField(blank=True, max_length=5, null=True)),
                ('keterangan', models.CharField(blank=True, max_length=40, null=True)),
                ('status', models.CharField(blank=True, max_length=13, null=True)),
                ('pengambil_darah', models.CharField(blank=True, max_length=70, null=True)),
                ('alamat_pengambil_darah', models.CharField(blank=True, max_length=120, null=True)),
                ('nip_pj', models.CharField(blank=True, max_length=20, null=True)),
                ('besarppn', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'utd_penyerahan_darah',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UtdStokDarah',
            fields=[
                ('no_kantong', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('golongan_darah', models.CharField(blank=True, max_length=2, null=True)),
                ('resus', models.CharField(blank=True, max_length=3, null=True)),
                ('tanggal_aftap', models.DateField(blank=True, null=True)),
                ('tanggal_kadaluarsa', models.DateField(blank=True, null=True)),
                ('asal_darah', models.CharField(blank=True, max_length=16, null=True)),
                ('status', models.CharField(blank=True, max_length=11, null=True)),
            ],
            options={
                'db_table': 'utd_stok_darah',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UtdStokMedis',
            fields=[
                ('kode_brng', models.OneToOneField(db_column='kode_brng', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='farmasi.databarang')),
                ('stok', models.FloatField(blank=True, null=True)),
                ('hargaterakhir', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'utd_stok_medis',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UtdStokPenunjang',
            fields=[
                ('kode_brng', models.OneToOneField(db_column='kode_brng', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='aset.ipsrsbarang')),
                ('stok', models.FloatField(blank=True, null=True)),
                ('hargaterakhir', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'utd_stok_penunjang',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UtdCekalDarah',
            fields=[
                ('no_donor', models.OneToOneField(db_column='no_donor', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='utd.utddonor')),
                ('tanggal', models.DateField(blank=True, null=True)),
                ('dinas', models.CharField(blank=True, max_length=5, null=True)),
                ('keterangan', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'utd_cekal_darah',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UtdPemisahanKomponen',
            fields=[
                ('no_donor', models.OneToOneField(db_column='no_donor', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='utd.utddonor')),
                ('tanggal', models.DateField(blank=True, null=True)),
                ('dinas', models.CharField(blank=True, max_length=5, null=True)),
            ],
            options={
                'db_table': 'utd_pemisahan_komponen',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UtdPenggunaanMedisDonor',
            fields=[
                ('no_donor', models.OneToOneField(db_column='no_donor', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='utd.utddonor')),
                ('jml', models.FloatField(blank=True, null=True)),
                ('harga', models.FloatField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'utd_penggunaan_medis_donor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UtdPenggunaanMedisPenyerahanDarah',
            fields=[
                ('no_penyerahan', models.OneToOneField(db_column='no_penyerahan', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='utd.utdpenyerahandarah')),
                ('jml', models.FloatField(blank=True, null=True)),
                ('harga', models.FloatField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'utd_penggunaan_medis_penyerahan_darah',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UtdPenggunaanPenunjangDonor',
            fields=[
                ('no_donor', models.OneToOneField(db_column='no_donor', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='utd.utddonor')),
                ('jml', models.FloatField(blank=True, null=True)),
                ('harga', models.FloatField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'utd_penggunaan_penunjang_donor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UtdPenggunaanPenunjangPenyerahanDarah',
            fields=[
                ('no_penyerahan', models.OneToOneField(db_column='no_penyerahan', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='utd.utdpenyerahandarah')),
                ('jml', models.FloatField(blank=True, null=True)),
                ('harga', models.FloatField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'utd_penggunaan_penunjang_penyerahan_darah',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UtdPenyerahanDarahDetail',
            fields=[
                ('no_penyerahan', models.OneToOneField(db_column='no_penyerahan', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='utd.utdpenyerahandarah')),
                ('jasa_sarana', models.FloatField(blank=True, null=True)),
                ('paket_bhp', models.FloatField(blank=True, null=True)),
                ('kso', models.FloatField(blank=True, null=True)),
                ('manajemen', models.FloatField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'utd_penyerahan_darah_detail',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UtdPenggunaanMedisPemisahanKomponen',
            fields=[
                ('no_donor', models.OneToOneField(db_column='no_donor', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='utd.utdpemisahankomponen')),
                ('jml', models.FloatField(blank=True, null=True)),
                ('harga', models.FloatField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'utd_penggunaan_medis_pemisahan_komponen',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UtdPenggunaanPenunjangPemisahanKomponen',
            fields=[
                ('no_donor', models.OneToOneField(db_column='no_donor', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='utd.utdpemisahankomponen')),
                ('jml', models.FloatField(blank=True, null=True)),
                ('harga', models.FloatField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'utd_penggunaan_penunjang_pemisahan_komponen',
                'managed': False,
            },
        ),
    ]
