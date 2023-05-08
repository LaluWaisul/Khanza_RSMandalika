from django.contrib import admin

from .models import Bangsal, Bidang, Departement

# Register your models here.

admin.site.register(Departement)
admin.site.register(Bidang)
admin.site.register(Bangsal)