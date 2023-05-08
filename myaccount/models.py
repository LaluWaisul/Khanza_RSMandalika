from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from PIL import Image


##################### MODIFICATION OF DJANGO USER MODEL #############################
################## THIS APP USING EMAIL BASE REGISTRATION ###########################


class MyUserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users must have an email')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        return self._create_user(email, password, first_name=first_name, last_name=last_name, **extra_fields)

    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, first_name=first_name, last_name=last_name, **extra_fields)


class Users(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email', max_length=255, unique=True)
    first_name = models.CharField(
        verbose_name='first name', max_length=30, null=True, blank=True)
    last_name = models.CharField(
        verbose_name='last name', max_length=150, null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(verbose_name='staff', default=False)
    is_active = models.BooleanField(verbose_name='active', default=True)
    is_admin = models.BooleanField(verbose_name='admin', default=False)
    is_user = models.BooleanField(verbose_name='officer', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = MyUserManager()

    def __str__(self):
        return self.email
    
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class ProfilUser(models.Model):
    user = models.OneToOneField(
        Users, on_delete=models.CASCADE, primary_key=True, related_name="profil_user")
    no_hp = models.CharField(max_length=20, null=True, blank=True)
    alamat = models.TextField(null=True, blank=True)
    pendidikan = models.CharField(max_length=50, null=True, blank=True)
    jabatan = models.CharField(max_length=50, null=True, blank=True)
    instalasi = models.ForeignKey('auth_bangsal.Bangsal', on_delete=models.SET_NULL, null=True, related_name='instalasi_user', blank=True)
    pokja = models.ForeignKey('akreditasi.PokjaAkreditasi', on_delete=models.SET_NULL, null=True)
    foto = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.foto:
            img = Image.open(self.foto.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.foto.path)


class Profil(models.Model):
    user = models.OneToOneField(
        Users, on_delete=models.CASCADE, primary_key=True, related_name="profil_pasien")
    no_hp = models.CharField(max_length=20, blank=True, null=True)
    alamat = models.TextField(null=True, blank=True)
    pendidikan = models.CharField(max_length=50, null=True, blank=True)
    no_ktp = models.CharField(max_length=20, blank=True)
    no_rkm_medis = models.CharField(max_length=6, blank=True)
    no_reg = models.CharField(max_length=8, blank=True)
    no_rawat = models.CharField(max_length=17, blank=True)
    jk = models.CharField(max_length=1, blank=True, null=True)
    tmp_lahir = models.CharField(max_length=15, blank=True, null=True)
    tgl_lahir = models.DateField(blank=True, null=True)
    nm_ibu = models.CharField(max_length=40, blank=True)
    alamat = models.CharField(max_length=200, blank=True, null=True)
    gol_darah = models.CharField(max_length=2, blank=True, null=True)
    pekerjaan = models.CharField(max_length=60, blank=True, null=True)
    stts_nikah = models.CharField(max_length=13, blank=True, null=True)
    agama = models.CharField(max_length=12, blank=True, null=True)
    foto = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.foto:
            img = Image.open(self.foto.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.foto.path)
