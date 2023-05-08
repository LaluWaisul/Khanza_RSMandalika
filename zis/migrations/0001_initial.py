# Generated by Django 4.1 on 2023-03-12 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ZisKeteranganAtapRumahPenerimaDankes',
            fields=[
                ('kode', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('keterangan', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'zis_keterangan_atap_rumah_penerima_dankes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ZisKeteranganDapurRumahPenerimaDankes',
            fields=[
                ('kode', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('keterangan', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'zis_keterangan_dapur_rumah_penerima_dankes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ZisKeteranganDindingRumahPenerimaDankes',
            fields=[
                ('kode', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('keterangan', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'zis_keterangan_dinding_rumah_penerima_dankes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ZisKeteranganElektronikPenerimaDankes',
            fields=[
                ('kode', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('keterangan', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'zis_keterangan_elektronik_penerima_dankes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ZisKeteranganJenisSimpananPenerimaDankes',
            fields=[
                ('kode', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('keterangan', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'zis_keterangan_jenis_simpanan_penerima_dankes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ZisKeteranganKamarMandiPenerimaDankes',
            fields=[
                ('kode', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('keterangan', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'zis_keterangan_kamar_mandi_penerima_dankes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ZisKeteranganKategoriAsnafPenerimaDankes',
            fields=[
                ('kode', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('keterangan', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'zis_keterangan_kategori_asnaf_penerima_dankes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ZisKeteranganKategoriPhbsPenerimaDankes',
            fields=[
                ('kode', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('keterangan', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'zis_keterangan_kategori_phbs_penerima_dankes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ZisKeteranganKursiRumahPenerimaDankes',
            fields=[
                ('kode', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('keterangan', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'zis_keterangan_kursi_rumah_penerima_dankes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ZisKeteranganLantaiRumahPenerimaDankes',
            fields=[
                ('kode', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('keterangan', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'zis_keterangan_lantai_rumah_penerima_dankes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ZisKeteranganPatologisPenerimaDankes',
            fields=[
                ('kode', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('keterangan', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'zis_keterangan_patologis_penerima_dankes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ZisKeteranganPengeluaranPenerimaDankes',
            fields=[
                ('kode', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('keterangan', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'zis_keterangan_pengeluaran_penerima_dankes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ZisKeteranganPenghasilanPenerimaDankes',
            fields=[
                ('kode', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('keterangan', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'zis_keterangan_penghasilan_penerima_dankes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ZisKeteranganTernakPenerimaDankes',
            fields=[
                ('kode', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('keterangan', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'zis_keterangan_ternak_penerima_dankes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ZisKeteranganUkuranRumahPenerimaDankes',
            fields=[
                ('kode', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('keterangan', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'zis_keterangan_ukuran_rumah_penerima_dankes',
                'managed': False,
            },
        ),
    ]