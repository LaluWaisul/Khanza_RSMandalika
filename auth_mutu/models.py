from tarfile import BLKTYPE
from django.db import models
import datetime

# Create your models here.

class IndikatorMutu(models.Model):
    nama = models.CharField(max_length=250, verbose_name='Indikator Mutu')
    target = models.IntegerField(blank=True, null=True)
    
    class Meta:
        db_table = 'indikator_mutu'
        
    def __str__(self):
        return self.nama
    

class Bulan(models.Model):
    id = models.IntegerField(primary_key=True)
    nama = models.CharField(max_length=50)
    singkatan = models.CharField(max_length=3, blank=True)
    
    def __str__(self):
        return self.nama
    
    
class DataIndikatorMutu(models.Model):
    tanggal_isi = models.DateField(blank=True, null=True)
    bangsal = models.ForeignKey('auth_bangsal.Bangsal', on_delete=models.CASCADE, related_name='bangsal_indikatormutu')
    ind_mutu = models.ForeignKey('IndikatorMutu', on_delete=models.CASCADE, related_name='indikator_mutu_data')
    numerator = models.IntegerField(blank=True, null=True)
    denominator = models.IntegerField(blank=True, null=True)
    
    class Meta:
        db_table = 'data_indikator_mutu'
        
        
    @property
    def bulan(self):
        # bln =  datetime.datetime.strptime(self.tanggal_isi, "%Y-%m-%d")
        # self.tanggal_isi.strftime("%b")
        if self.tanggal_isi == None:
            return None
        else:
            return self.tanggal_isi.month
    
    def __str__(self):
        return f'{self.tanggal_isi} - {self.bangsal}'
    