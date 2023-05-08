from email.policy import default
import os
from django.db import models
from django.dispatch import receiver

# Create your models here.

class RumahSakit(models.Model):
    nama = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nama
    

class PokjaAkreditasi(models.Model):
    rumah_sakit = models.ForeignKey('RumahSakit', on_delete=models.SET_NULL, null=True, blank=True)
    nama = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nama
    

class StandarAkreditasi(models.Model):
    pokja = models.ForeignKey('PokjaAkreditasi', on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nama


class ElementPenilaian(models.Model):
    standar = models.ForeignKey('StandarAkreditasi', on_delete=models.CASCADE)
    nama = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nama
    

class KategoriElementPenilaian(models.Model):
    element = models.ForeignKey('ElementPenilaian', on_delete=models.CASCADE)
    nama = models.CharField(max_length=10, blank=True)
    metode = models.CharField(max_length=50, blank=True)
    skor = models.IntegerField(default=0)
    jlh_kat_skor = models.CharField(max_length=1, default="3")
    skor_max = models.IntegerField(default=10)
    sasaran = models.CharField(max_length=200, blank=True)
    tahun = models.DateField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.element.standar} - {self.element} - {self.nama}'
    
    
class FileAkreditasi(models.Model):
    CHOICE =(
        ('Belum Dikerjakan', 'Belum Dikerjakan'),
        ('Proses', 'Proses'),
        ('Selesai', 'Selesai')
    )
    kategori = models.ForeignKey('KategoriElementPenilaian', on_delete=models.CASCADE, blank=True, null=True)
    nama = models.CharField(max_length=200, blank=True)
    file = models.FileField(upload_to='akreditasi/')
    status = models.CharField(max_length=20, default='Belum Dikerjakan', choices=CHOICE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        # if self.kategori:
        #     return f'{self.kategori.element.standar} - {self.kategori.element} - {self.kategori} - {self.nama}'
        # else:
            # return f'{self.kategori} - {self.nama}'
        return self.nama
    
    def save(self, *args, **kwargs):
        if self.nama:
            self.nama = self.nama
        else:
            self.nama = self.file.name
            
        super(FileAkreditasi, self).save(*args, **kwargs)
        
        
def _delete_file(path):
    """ Deletes file from filesystem. """
    if os.path.isfile(path):
        os.remove(path)
            
@receiver(models.signals.post_delete, sender=FileAkreditasi)
def delete_file(sender, instance, *args, **kwargs):
    """ Deletes files on `post_delete` """
    if instance.file:
        _delete_file(instance.file.path)
        
# @receiver(models.signals.pre_save, sender=FileAkreditasi)
# def file_update(sender, **kwargs):
#     upload_folder_instance = kwargs['instance']
#     print('ini data: ', upload_folder_instance)
#     if upload_folder_instance.id:
#         path = file.path
#         print('ini path: ',path)
#         os.remove(path)