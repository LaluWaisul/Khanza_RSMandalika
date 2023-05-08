# Generated by Django 4.0.6 on 2022-08-09 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bangsal',
            fields=[
                ('kd_bangsal', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nm_bangsal', models.CharField(blank=True, max_length=30, null=True)),
                ('status', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'bangsal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bidang',
            fields=[
                ('nama', models.CharField(max_length=15, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'bidang',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Departemen',
            fields=[
                ('dep_id', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'departemen',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Indekref',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n', models.FloatField()),
                ('ttl', models.FloatField()),
            ],
            options={
                'db_table': 'indekref',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Indextotal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ttl', models.FloatField()),
            ],
            options={
                'db_table': 'indextotal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Kamar',
            fields=[
                ('kd_kamar', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('trf_kamar', models.FloatField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=11, null=True)),
                ('kelas', models.CharField(blank=True, max_length=11, null=True)),
                ('statusdata', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'kamar',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Poliklinik',
            fields=[
                ('kd_poli', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nm_poli', models.CharField(blank=True, max_length=50, null=True)),
                ('registrasi', models.FloatField()),
                ('registrasilama', models.FloatField()),
                ('status', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'poliklinik',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SiranapKetersediaanKamar',
            fields=[
                ('kode_ruang_siranap', models.CharField(max_length=29, primary_key=True, serialize=False)),
                ('kelas_ruang_siranap', models.CharField(max_length=21)),
                ('kelas', models.CharField(max_length=11)),
                ('kapasitas', models.IntegerField(blank=True, null=True)),
                ('tersedia', models.IntegerField(blank=True, null=True)),
                ('tersediapria', models.IntegerField(blank=True, null=True)),
                ('tersediawanita', models.IntegerField(blank=True, null=True)),
                ('menunggu', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'siranap_ketersediaan_kamar',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Indexins',
            fields=[
                ('dep', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='bangsal.departemen')),
                ('persen', models.FloatField()),
            ],
            options={
                'db_table': 'indexins',
                'managed': False,
            },
        ),
    ]
