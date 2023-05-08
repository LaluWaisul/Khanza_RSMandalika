from django.contrib import admin

from .models import Bulan, DataIndikatorMutu, IndikatorMutu

# Register your models here.

class DataIndikatorAdmin(admin.ModelAdmin):
    list_display = ['tanggal_isi', 'bangsal', 'ind_mutu', 'numerator', 'denominator']
    
    
admin.site.register(IndikatorMutu)
admin.site.register(DataIndikatorMutu, DataIndikatorAdmin)
admin.site.register(Bulan)