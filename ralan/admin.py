from django.contrib import admin

from .models import BookingPeriksa, Rawatjalan, RegPeriksa, BookingRegistrasi, Jadwal

# Register your models here.


admin.site.register(BookingPeriksa)
admin.site.register(BookingRegistrasi)
admin.site.register(RegPeriksa)
admin.site.register(Rawatjalan)
admin.site.register(Jadwal)
# admin.site.register()