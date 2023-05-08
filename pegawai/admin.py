from django.contrib import admin
from .models import Dokter, Pegawai, Petugas, RiwayatJabatan, Tambahjaga, Spesialis

# Register your models here.

admin.site.register(Pegawai)
admin.site.register(Tambahjaga)
admin.site.register(Dokter)
admin.site.register(Petugas)
admin.site.register(RiwayatJabatan)
admin.site.register(Spesialis)