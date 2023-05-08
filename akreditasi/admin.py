from django.contrib import admin
from .models import PokjaAkreditasi, StandarAkreditasi, FileAkreditasi, ElementPenilaian, KategoriElementPenilaian, RumahSakit

# Register your models here.
admin.site.register(RumahSakit)
admin.site.register(PokjaAkreditasi)
admin.site.register(StandarAkreditasi)
admin.site.register(ElementPenilaian)
admin.site.register(KategoriElementPenilaian)
admin.site.register(FileAkreditasi)