# Generated by Django 4.0.6 on 2022-08-09 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PerpustakaanAnggota',
            fields=[
                ('no_anggota', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nama_anggota', models.CharField(blank=True, max_length=40, null=True)),
                ('tmp_lahir', models.CharField(blank=True, max_length=20, null=True)),
                ('tgl_lahir', models.DateField(blank=True, null=True)),
                ('j_kel', models.CharField(blank=True, max_length=1, null=True)),
                ('alamat', models.CharField(blank=True, max_length=70, null=True)),
                ('no_telp', models.CharField(blank=True, max_length=13, null=True)),
                ('email', models.CharField(blank=True, max_length=25, null=True)),
                ('tgl_gabung', models.DateField(blank=True, null=True)),
                ('masa_berlaku', models.DateField(blank=True, null=True)),
                ('jenis_anggota', models.CharField(max_length=7)),
                ('nomer_id', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'perpustakaan_anggota',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PerpustakaanBayarDenda',
            fields=[
                ('tgl_denda', models.DateField(primary_key=True, serialize=False)),
                ('besar_denda', models.FloatField(blank=True, null=True)),
                ('keterangan_denda', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'perpustakaan_bayar_denda',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PerpustakaanBayarDendaHarian',
            fields=[
                ('tgl_denda', models.DateField(primary_key=True, serialize=False)),
                ('keterlambatan', models.IntegerField(blank=True, null=True)),
                ('besar_denda', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'perpustakaan_bayar_denda_harian',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PerpustakaanBuku',
            fields=[
                ('kode_buku', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('judul_buku', models.CharField(blank=True, max_length=200, null=True)),
                ('jml_halaman', models.CharField(blank=True, max_length=5, null=True)),
                ('thn_terbit', models.TextField(blank=True, null=True)),
                ('isbn', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'perpustakaan_buku',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PerpustakaanDenda',
            fields=[
                ('kode_denda', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('jenis_denda', models.CharField(blank=True, max_length=40, null=True)),
                ('besar_denda', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'perpustakaan_denda',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PerpustakaanEbook',
            fields=[
                ('kode_ebook', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('judul_ebook', models.CharField(blank=True, max_length=200, null=True)),
                ('jml_halaman', models.CharField(blank=True, max_length=5, null=True)),
                ('thn_terbit', models.TextField(blank=True, null=True)),
                ('berkas', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'perpustakaan_ebook',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PerpustakaanInventaris',
            fields=[
                ('no_inventaris', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('asal_buku', models.CharField(blank=True, max_length=7, null=True)),
                ('tgl_pengadaan', models.DateField(blank=True, null=True)),
                ('harga', models.FloatField(blank=True, null=True)),
                ('status_buku', models.CharField(blank=True, max_length=8, null=True)),
                ('no_rak', models.CharField(blank=True, max_length=3, null=True)),
                ('no_box', models.CharField(blank=True, max_length=3, null=True)),
            ],
            options={
                'db_table': 'perpustakaan_inventaris',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PerpustakaanJenisBuku',
            fields=[
                ('id_jenis', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nama_jenis', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'perpustakaan_jenis_buku',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PerpustakaanKategori',
            fields=[
                ('id_kategori', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nama_kategori', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'perpustakaan_kategori',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PerpustakaanPeminjaman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tgl_pinjam', models.DateField(blank=True, null=True)),
                ('tgl_kembali', models.DateField(blank=True, null=True)),
                ('status_pinjam', models.CharField(blank=True, max_length=14, null=True)),
            ],
            options={
                'db_table': 'perpustakaan_peminjaman',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PerpustakaanPenerbit',
            fields=[
                ('kode_penerbit', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nama_penerbit', models.CharField(blank=True, max_length=40, null=True)),
                ('alamat_penerbit', models.CharField(blank=True, max_length=70, null=True)),
                ('no_telp', models.CharField(blank=True, max_length=13, null=True)),
                ('email', models.CharField(blank=True, max_length=25, null=True)),
                ('website_penerbit', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'perpustakaan_penerbit',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PerpustakaanPengarang',
            fields=[
                ('kode_pengarang', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('nama_pengarang', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'perpustakaan_pengarang',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PerpustakaanRuang',
            fields=[
                ('kd_ruang', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('nm_ruang', models.CharField(blank=True, max_length=40, null=True)),
            ],
            options={
                'db_table': 'perpustakaan_ruang',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PerpustakaanSetPeminjaman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_pinjam', models.IntegerField(blank=True, null=True)),
                ('lama_pinjam', models.IntegerField(blank=True, null=True)),
                ('denda_perhari', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'perpustakaan_set_peminjaman',
                'managed': False,
            },
        ),
    ]
