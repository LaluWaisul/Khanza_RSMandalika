# Generated by Django 4.1 on 2023-03-12 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pegawai', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmbilDankes',
            fields=[
                ('id', models.OneToOneField(db_column='id', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='pegawai.pegawai')),
                ('tanggal', models.DateField()),
                ('ktg', models.CharField(max_length=50)),
                ('dankes', models.FloatField()),
            ],
            options={
                'db_table': 'ambil_dankes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Antriloket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loket', models.IntegerField()),
                ('antrian', models.IntegerField()),
            ],
            options={
                'db_table': 'antriloket',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AplicareKetersediaanKamar',
            fields=[
                ('kode_kelas_aplicare', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('kelas', models.CharField(max_length=11)),
                ('kapasitas', models.IntegerField(blank=True, null=True)),
                ('tersedia', models.IntegerField(blank=True, null=True)),
                ('tersediapria', models.IntegerField(blank=True, null=True)),
                ('tersediawanita', models.IntegerField(blank=True, null=True)),
                ('tersediapriawanita', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'aplicare_ketersediaan_kamar',
                'managed': False,
            },
        ),
    ]
