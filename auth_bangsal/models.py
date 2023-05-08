from django.db import models

# Create your models here.

class Departement(models.Model):
    nama = models.CharField(max_length=100)
    
    class Meta:
        managed=False
        db_table = 'departement'
        
    def __str__(self):
        return self.nama
    
    
class Bidang(models.Model):
    dep = models.ForeignKey('Departement', on_delete=models.CASCADE, related_name='departement_bidang')
    nama = models.CharField(max_length=100)
    
    class Meta:
        managed = False
        db_table = 'bidang'
        
    def __str__(self):
        return self.nama        
        
class Bangsal(models.Model):
    kd_bangsal = models.CharField(max_length=5, primary_key=True) #diserver menggunakan id ini sebagai primery key
    bidang = models.ForeignKey('Bidang', on_delete=models.CASCADE, related_name='bidang_bangsal')
    nama = models.CharField(max_length=100)
    
    class Meta:
        managed = False
        db_table = 'bangsal'
        
    def __str__(self):
        return self.nama