# Generated by Django 4.1 on 2023-03-12 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bangsal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AkunBayar',
            fields=[
                ('nama_bayar', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('ppn', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'akun_bayar',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AkunPiutang',
            fields=[
                ('nama_bayar', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'akun_piutang',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('namabank', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'bank',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BayarPemesanan',
            fields=[
                ('tgl_bayar', models.DateField(primary_key=True, serialize=False)),
                ('besar_bayar', models.FloatField(blank=True, null=True)),
                ('keterangan', models.CharField(blank=True, max_length=100, null=True)),
                ('no_bukti', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'bayar_pemesanan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BayarPemesananInventaris',
            fields=[
                ('tgl_bayar', models.DateField(primary_key=True, serialize=False)),
                ('besar_bayar', models.FloatField(blank=True, null=True)),
                ('keterangan', models.CharField(blank=True, max_length=100, null=True)),
                ('no_bukti', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'bayar_pemesanan_inventaris',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BayarPemesananNonMedis',
            fields=[
                ('tgl_bayar', models.DateField(primary_key=True, serialize=False)),
                ('besar_bayar', models.FloatField(blank=True, null=True)),
                ('keterangan', models.CharField(blank=True, max_length=100, null=True)),
                ('no_bukti', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'bayar_pemesanan_non_medis',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BayarPiutang',
            fields=[
                ('tgl_bayar', models.DateField(primary_key=True, serialize=False)),
                ('besar_cicilan', models.FloatField()),
                ('catatan', models.CharField(max_length=100)),
                ('no_rawat', models.CharField(max_length=17)),
            ],
            options={
                'db_table': 'bayar_piutang',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BiayaHarian',
            fields=[
                ('kd_kamar', models.OneToOneField(db_column='kd_kamar', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='bangsal.kamar')),
                ('nama_biaya', models.CharField(max_length=50)),
                ('besar_biaya', models.FloatField()),
                ('jml', models.IntegerField()),
            ],
            options={
                'db_table': 'biaya_harian',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BiayaSekali',
            fields=[
                ('kd_kamar', models.OneToOneField(db_column='kd_kamar', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='bangsal.kamar')),
                ('nama_biaya', models.CharField(max_length=50)),
                ('besar_biaya', models.FloatField()),
            ],
            options={
                'db_table': 'biaya_sekali',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noindex', models.IntegerField()),
                ('tgl_byr', models.DateField(blank=True, null=True)),
                ('no', models.CharField(max_length=50)),
                ('nm_perawatan', models.CharField(max_length=200)),
                ('pemisah', models.CharField(max_length=1)),
                ('biaya', models.FloatField()),
                ('jumlah', models.FloatField()),
                ('tambahan', models.FloatField()),
                ('totalbiaya', models.FloatField()),
                ('status', models.CharField(blank=True, max_length=22, null=True)),
            ],
            options={
                'db_table': 'billing',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClosingKasir',
            fields=[
                ('shift', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('jam_masuk', models.TimeField()),
                ('jam_pulang', models.TimeField()),
            ],
            options={
                'db_table': 'closing_kasir',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dansos',
            fields=[
                ('dana', models.FloatField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'dansos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('no_deposit', models.CharField(max_length=17, primary_key=True, serialize=False)),
                ('tgl_deposit', models.DateTimeField()),
                ('besarppn', models.FloatField()),
                ('besar_deposit', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'deposit',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetailNotaInap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('besarppn', models.FloatField(blank=True, null=True)),
                ('besar_bayar', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'detail_nota_inap',
                'managed': False,
            },
        ),
    ]