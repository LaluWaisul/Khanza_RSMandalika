# Generated by Django 4.1 on 2023-03-12 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ralan', '0001_initial'),
        ('diagnosa', '0001_initial'),
        ('pegawai', '0001_initial'),
        ('asuransi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiagnosaPasien',
            fields=[
                ('no_rawat', models.OneToOneField(db_column='no_rawat', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='ralan.regperiksa')),
                ('status', models.CharField(max_length=5)),
                ('prioritas', models.IntegerField()),
                ('status_penyakit', models.CharField(blank=True, max_length=4, null=True)),
            ],
            options={
                'db_table': 'diagnosa_pasien',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InacbgCoderNik',
            fields=[
                ('nik', models.OneToOneField(db_column='nik', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='pegawai.pegawai')),
                ('no_ik', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'inacbg_coder_nik',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InacbgDataTerkirim',
            fields=[
                ('no_sep', models.OneToOneField(db_column='no_sep', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='asuransi.bridgingsep')),
                ('nik', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'inacbg_data_terkirim',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InacbgGroupingStage1',
            fields=[
                ('no_sep', models.OneToOneField(db_column='no_sep', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='asuransi.bridgingsep')),
                ('code_cbg', models.CharField(blank=True, max_length=10, null=True)),
                ('deskripsi', models.CharField(blank=True, max_length=200, null=True)),
                ('tarif', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'inacbg_grouping_stage1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InacbgKlaimBaru',
            fields=[
                ('no_sep', models.OneToOneField(db_column='no_sep', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='asuransi.bridgingsep')),
                ('patient_id', models.CharField(blank=True, max_length=30, null=True)),
                ('admission_id', models.CharField(blank=True, max_length=30, null=True)),
                ('hospital_admission_id', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'inacbg_klaim_baru',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InacbgKlaimBaru2',
            fields=[
                ('no_rawat', models.OneToOneField(db_column='no_rawat', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='ralan.regperiksa')),
                ('no_sep', models.CharField(max_length=40, unique=True)),
                ('patient_id', models.CharField(blank=True, max_length=30, null=True)),
                ('admission_id', models.CharField(blank=True, max_length=30, null=True)),
                ('hospital_admission_id', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'inacbg_klaim_baru2',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InacbgNoklaimCorona',
            fields=[
                ('no_rawat', models.OneToOneField(db_column='no_rawat', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='ralan.regperiksa')),
                ('no_klaim', models.CharField(blank=True, max_length=40, null=True, unique=True)),
            ],
            options={
                'db_table': 'inacbg_noklaim_corona',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='KategoriPenyakit',
            fields=[
                ('kd_ktg', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('nm_kategori', models.CharField(blank=True, max_length=30, null=True)),
                ('ciri_umum', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'kategori_penyakit',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MasterMasalahKeperawatan',
            fields=[
                ('kode_masalah', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('nama_masalah', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'master_masalah_keperawatan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MasterMasalahKeperawatanAnak',
            fields=[
                ('kode_masalah', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('nama_masalah', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'master_masalah_keperawatan_anak',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MasterMasalahKeperawatanGigi',
            fields=[
                ('kode_masalah', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('nama_masalah', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'master_masalah_keperawatan_gigi',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MasterMasalahKeperawatanMata',
            fields=[
                ('kode_masalah', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('nama_masalah', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'master_masalah_keperawatan_mata',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PenilaianAwalKeperawatanMataMasalah',
            fields=[
                ('no_rawat', models.OneToOneField(db_column='no_rawat', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='ralan.regperiksa')),
            ],
            options={
                'db_table': 'penilaian_awal_keperawatan_mata_masalah',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Penyakit',
            fields=[
                ('kd_penyakit', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nm_penyakit', models.CharField(blank=True, max_length=100, null=True)),
                ('ciri_ciri', models.TextField(blank=True, null=True)),
                ('keterangan', models.CharField(blank=True, max_length=60, null=True)),
                ('status', models.CharField(max_length=13)),
            ],
            options={
                'db_table': 'penyakit',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TemporarySurveilensPenyakit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'temporary_surveilens_penyakit',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InacbgDataTerkirim2',
            fields=[
                ('no_sep', models.OneToOneField(db_column='no_sep', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='diagnosa.inacbgklaimbaru2')),
                ('nik', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'inacbg_data_terkirim2',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InacbgGroupingStage12',
            fields=[
                ('no_sep', models.OneToOneField(db_column='no_sep', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='diagnosa.inacbgklaimbaru2')),
                ('code_cbg', models.CharField(blank=True, max_length=10, null=True)),
                ('deskripsi', models.CharField(blank=True, max_length=200, null=True)),
                ('tarif', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'inacbg_grouping_stage12',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PenyakitPd3I',
            fields=[
                ('kd_penyakit', models.OneToOneField(db_column='kd_penyakit', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='diagnosa.penyakit')),
            ],
            options={
                'db_table': 'penyakit_pd3i',
                'managed': False,
            },
        ),
    ]
