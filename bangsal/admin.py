from django.contrib import admin

from .models import Bangsal, Bidang, Departemen, Poliklinik, Kamar

# Register your models here.

class KamarAdmin(admin.ModelAdmin):
    list_display =  ('kd_kamar', 'kd_bangsal', 'trf_kamar', 'status', 'kelas', 'statusdata')

admin.site.register(Poliklinik)
admin.site.register(Departemen)
admin.site.register(Bidang)
admin.site.register(Bangsal)
admin.site.register(Kamar, KamarAdmin)