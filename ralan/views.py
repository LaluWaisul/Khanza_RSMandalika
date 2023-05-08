from calendar import month
from itertools import count
from urllib import request
from django.http import Http404
from numbers import Number
from sys import api_version
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Max, Sum, Case, When, F, Value, ExpressionWrapper, FloatField, Count, Q
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from datetime import date, datetime
from itertools import chain
from django.views import View
from django.contrib import messages
from django.urls import reverse
from django.core.paginator import Paginator
from django.core.cache import cache

from .serializers import BookingPeriksaSerializer, BookingRegistrasiSerializer, JadwalSerializer, RegPeriksaSerializer, JadwalDokterSerializer
from .models import BookingPeriksa, BookingRegistrasi, RegPeriksa, Jadwal
from .forms import BookingPeriksaForm, RegPeriksaForm

# Create your views here.

############################################### VIEW RESTAPI #################################

class BookingPeriksaAPIView(APIView):
    def get(self, request):
        getdata = BookingPeriksa.objects.using('khanza_db').all().order_by('-no_booking')
        serializer = BookingPeriksaSerializer(getdata, many=True)
        return Response(serializer.data)
    
    
    def post(self, request):
        postdata = request.data
        
        #MENAMBAHKAN ID BOOKING BARU
        get_lastbooking = BookingPeriksa.objects.using('khanza_db').first()
        id_book = get_lastbooking.no_booking[-4:]
        add_idbook = int(id_book) + 1
        next_id = str(add_idbook).zfill(4)
        today=datetime.now()
        no_booking = f'BP{today.year}{today.month:02d}{today.day:02d}{next_id}'
        postdata["no_booking"] = no_booking
        
        #MENAMBAHKAN DATA KE DALAM DATABASE
        serializer = BookingPeriksaSerializer(data=postdata)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
            

class KunjunganView(APIView):
    def get(self, request):
        today=datetime.now()
        bulan_sekarang = today.month
        rekam_medis = request.query_params.get('rm', None)
        kunjungan = RegPeriksa.objects.using('khanza_db').filter(no_rkm_medis=rekam_medis)
        ralan = RegPeriksa.objects.using('khanza_db').filter(no_rkm_medis=rekam_medis, status_lanjut='ralan')
        ranap = RegPeriksa.objects.using('khanza_db').filter(no_rkm_medis=rekam_medis, status_lanjut='ranap')
        bulan_ini = RegPeriksa.objects.using('khanza_db').filter(no_rkm_medis=rekam_medis, tgl_registrasi__month=bulan_sekarang)
        
        serializer = RegPeriksaSerializer(kunjungan, many=True)
        status_kunjungan = len(kunjungan)
        status_ralan = len(ralan)
        status_ranap = len(ranap)
        status_bulanini = len(bulan_ini)
        
        context = {
            'status_kunjungan': status_kunjungan,
            'status_ralan': status_ralan,
            'status_ranap': status_ranap,
            'status_bulanini': status_bulanini
        }
        
        return Response(context)
    

#JADWAL RAWAT JALAN DOKTER / DOKTER SPESIALIS
class JadwalRalan(APIView):
    # UNTUK MENDAPATKAN HARI SESUAI DENGAN NAMA HARI DALAM DATABASE
    def get_day_name(self, tgl):
        tanggal = datetime.strptime(tgl, "%Y-%m-%d")
        tglhari = tanggal.strftime("%A")
        namahari = [
            {"id":"SENIN", "en":"Monday"}, 
            {"id":"SELASA", "en":"Tuesday"}, 
            {"id":"RABU", "en":"Wednesday"},
            {"id":"KAMIS", "en":"Thursday"},
            {"id":"JUMAT", "en":"Friday"},
            {"id":"SABTU", "en":"Saturday"},
            {"id":"AKHAD", "en":"Sunday"}]
        hari = ''
        for hr in namahari:
            if hr["en"] == tglhari:
                hari = hr["id"]        
        return hari
    
    # UNTUK MENDAPATKAN JADWAL PRAKTIK DOKTER SESUAI DENGAN KUOTA DAN JUMLAH REGISTRASI PASIEN SERTA STATUS DAFTAR USER SAAT INI
    def get_jadwal_dokter(self, jadwal, jadwal_reg_no_user, jadwal_reg_user):
        #dari jadwal_reg_user akan diekstrak dokter tempat user mendaftar
        #query untuk mendapatkan dokter tempat user mendaftarkan dirinya
        dokter_reg_user = jadwal_reg_user.values_list('kd_dokter', flat=True)
        
        #query untuk mendapatkan dokter dimana user tidak mendaftarkan diri
        dokter_reg = jadwal_reg_no_user.exclude(kd_dokter__in=dokter_reg_user).values_list('kd_dokter', flat=True)
        
        #query untuk mendapatkan jadwal dokter dimana user tidak mendaftar
        jadwal_no_user = jadwal_reg_no_user.exclude(kd_dokter__in=dokter_reg_user) 
        #query utk mendptkan jadwal dokter yg tdk memiliki pendaftar
        jadwal_noreg = jadwal.exclude(kd_dokter__in = dokter_reg).exclude(kd_dokter__in=dokter_reg_user) 
        
        final_jadwal = list(chain(jadwal_noreg, jadwal_no_user, jadwal_reg_user))
        return final_jadwal
    
    def get(self, request):
        tanggal = date.today()
        tgl = date.strftime(tanggal, "%Y-%m-%d")
        get_tanggal = request.query_params.get('periksa', None)
        
        if get_tanggal:
            hari = self.get_day_name(get_tanggal)
            no_rkm_medis_user=request.user.profil_user.no_rkm_medis
            # tgl = datetime.strptime(get_tanggal, "%Y-%m-%d")
            # dengan format diatas bisa mendapatkan data seperti tgl.month/tgl.day/tgl.year
            jadwal_poli = Jadwal.objects.using('khanza_db').filter(hari_kerja=hari).values('kd_dokter', 'kuota', 'jam_mulai', 'jam_selesai', 'kd_poli')
            
            jadwal = jadwal_poli.annotate(
                tanggal_periksa = Value(get_tanggal),
                nm_dokter = F('kd_dokter__nm_dokter'),
                daftar = Value(0),
                status = Case(When(Q(kuota__gt=F('daftar')), then=Value("Tersedia")),
                            When(Q(kuota__lte=F('daftar')), then=Value('Penuh'))),
            )
            
            registrasi = BookingRegistrasi.objects.using('khanza_db').filter(tanggal_periksa=get_tanggal, kd_dokter__jadwal__hari_kerja=hari).values('kd_dokter', 'kd_poli')
            jadwal_reg_without_user = registrasi.exclude(no_rkm_medis=no_rkm_medis_user).annotate(
                tanggal_periksa = Value(get_tanggal),
                kuota = F('kd_dokter__jadwal__kuota'),
                jam_mulai = F('kd_dokter__jadwal__jam_mulai'),
                jam_selesai = F('kd_dokter__jadwal__jam_selesai'),
                nm_dokter = F('kd_dokter__nm_dokter'),
                daftar = Count(F('no_rkm_medis')),
                status = Case(When(Q(kuota__gt=F('daftar')), then=Value("Tersedia")),
                            When(Q(kuota__lte=F('daftar')), then=Value('Penuh')),
                        )
            )
            
            
            data_jadwal_user = BookingRegistrasi.objects.filter(no_rkm_medis=no_rkm_medis_user, tanggal_periksa=get_tanggal)            
            jadwal_reg_user = data_jadwal_user.values('kd_dokter', 'kd_poli').annotate(
                tanggal_periksa = Value(get_tanggal),
                kuota = F('kd_dokter__jadwal__kuota'),
                jam_mulai = F('kd_dokter__jadwal__jam_mulai'),
                jam_selesai = F('kd_dokter__jadwal__jam_selesai'),
                nm_dokter = F('kd_dokter__nm_dokter'),
                daftar = Value(0),
                status = Value('Terdaftar')
            )
            
            data = self.get_jadwal_dokter(jadwal, jadwal_reg_without_user, jadwal_reg_user)
        
            serializer = JadwalSerializer(data, many=True)
        
            return Response(serializer.data)
                   
        else:
            hari = self.get_day_name(tgl)
            no_rkm_medis_user=request.user.profil_user.no_rkm_medis
            # print('ini functionhari: ',hari)
            jadwal_poli = Jadwal.objects.using('khanza_db').filter(hari_kerja=hari).values('kd_dokter', 'kuota', 'jam_mulai', 'jam_selesai', 'kd_poli')
            jadwal = jadwal_poli.annotate(
                tanggal_periksa = Value(tgl),
                nm_dokter = F('kd_dokter__nm_dokter'),
                daftar = Value(0),
                status = Case(When(Q(kuota__gt=F('daftar')), then=Value("Tersedia")),
                            When(Q(kuota__lte=F('daftar')), then=Value('Penuh'))),
            )
            
            registrasi = BookingRegistrasi.objects.using('khanza_db').filter(tanggal_periksa=tgl, kd_dokter__jadwal__hari_kerja=hari).values('kd_dokter', 'kd_poli')
            jadwal_reg_without_user = registrasi.exclude(no_rkm_medis=no_rkm_medis_user).annotate(
                tanggal_periksa= Value(tgl),
                kuota = F('kd_dokter__jadwal__kuota'),
                jam_mulai = F('kd_dokter__jadwal__jam_mulai'),
                jam_selesai = F('kd_dokter__jadwal__jam_selesai'),
                nm_dokter = F('kd_dokter__nm_dokter'),
                daftar = Count(F('no_rkm_medis')),
                status = Case(When(Q(kuota__gt=F('daftar')), then=Value("Tersedia")),
                            When(Q(kuota__lte=F('daftar')), then=Value('Penuh')),
                        )
            )
            
            data_jadwal_user = BookingRegistrasi.objects.filter(no_rkm_medis=no_rkm_medis_user, tanggal_periksa=tgl)            
            jadwal_reg_user = data_jadwal_user.values('kd_dokter', 'kd_poli').annotate(
                tanggal_periksa= Value(tgl),
                kuota = F('kd_dokter__jadwal__kuota'),
                jam_mulai = F('kd_dokter__jadwal__jam_mulai'),
                jam_selesai = F('kd_dokter__jadwal__jam_selesai'),
                nm_dokter = F('kd_dokter__nm_dokter'),
                daftar = Value(0),
                status = Value('Terdaftar')
            )
            
            data = self.get_jadwal_dokter(jadwal, jadwal_reg_without_user, jadwal_reg_user)
        
            serializer = JadwalSerializer(data, many=True)
        
            return Response(serializer.data)
    

#REGISTRASI PEMERIKSAAN
class RegistrasiPeriksaView(APIView):
    model = RegPeriksa
    serializer_class = RegPeriksaSerializer
    
    def get(self, request):
        getdata = self.model.objects.using('auth_db').all()
        serializer = self.serializer_class(getdata, many=True)
        return Response(serializer.data)
    

#BOOKING REGISTRASI
class BookingRegistrasiListView(APIView):
    model = BookingRegistrasi
    serializer_class = BookingRegistrasiSerializer
    
    def get(self, request, format=None):
        getdata = self.model.objects.using('khanza_db').all()
        
        serializer = self.serializer_class(getdata, many=True)
        
        return Response(serializer.data)
        
    
    def post(self, request, format=None):
        postdata = request.data
        kd_dokter = postdata.get('kd_dokter')
        tgl_periksa = postdata.get('tanggal_periksa')
        kd_poli = postdata.get('kd_poli')           
        
        get_lastbooking = ''
        if kd_poli and tgl_periksa:
            get_lastbooking = self.model.objects.using('khanza_db').filter(kd_poli = kd_poli, tanggal_periksa=tgl_periksa).aggregate(Max('no_reg'))
            # get_lastbooking1 = self.model.objects.using('khanza_db').order_by('-no_reg').first() --> bisa juga dengan metode ini
        elif kd_poli and tgl_periksa and kd_dokter:
            get_lastbooking = self.model.objects.using('khanza_db').filter(kd_poli = kd_poli, kd_dokter=kd_dokter, tanggal_periksa=tgl_periksa).aggregate(Max('no_reg'))
        else:
            get_lastbooking = self.model.objects.using('khanza_db').filter(kd_dokter = kd_dokter, tanggal_periksa=tgl_periksa).aggregate(Max('no_reg'))
            
            
        noreg = int(get_lastbooking['no_reg__max'])+1
        next_noreg = str(noreg).zfill(3)
        postdata['no_reg']=next_noreg
        
        serializer = self.serializer_class(data=postdata)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class BookingRegistrasiDetailView(APIView):
    model = BookingRegistrasi
    serializer_class = BookingRegistrasiSerializer
    
    def get_object(self, pk):
        try:
            return self.model.objects.using('khanza_db').get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        getdata = self.get_object(pk)
        serializer = self.serializer_class(getdata)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        putdata = request.POST
        getdata = self.get_object(pk)
        serializer = self.serializer_class(instance=getdata, data=putdata)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        getdata = self.get_object(pk)
        getdata.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
############################################### JADWAL DOKTER #################################################

class JadwalDokterRalanView(View):
    def get(self, request):
        tgl_sekarang = date.today()
        jadwal = Jadwal.objects.filter(kd_dokter__isnull=False).values('kd_dokter__nm_dokter', 'hari_kerja', 'kd_poli__nm_poli', 'jam_mulai', 'jam_selesai', 'kuota').annotate(
            pasien_terdaftar = Count(Case(When(Q(kd_poli__regperiksa__tgl_registrasi=tgl_sekarang), then=F('kd_poli__regperiksa')))),
        )
        
        context={
            'jadwal':jadwal
        }
       
        return render(request, 'jadwaldokter.html', context)
    

class JadwalDokterRalanAPIView(APIView):
    def get(self, request):
        tgl_sekarang = date.today()
        jadwal = Jadwal.objects.filter(kd_dokter__isnull=False).values('kd_dokter__nm_dokter', 'hari_kerja', 'kd_poli__nm_poli', 'jam_mulai', 'jam_selesai', 'kuota').annotate(
            pasien_terdaftar = Count(Case(When(Q(kd_poli__regperiksa__tgl_registrasi=tgl_sekarang), then=F('kd_poli__regperiksa')))),
        )
        serializer = JadwalDokterSerializer(jadwal, many=True)
               
        return Response(serializer.data)
    
    
################################### VIEW NONRESTAPI ##########################################

class BookingPeriksaView(View):
    def get(self, request):
        form = BookingPeriksaForm()
        context={
            'form':form
        }
        return render(request, 'bookingform.html', context)
    
    
    def post(self, request):
        postdata = request.POST
        today=datetime.now()
        
        #MENAMBAHKAN DATA KE DALAM DATABASE
        form = BookingPeriksaForm(postdata)
        if form.is_valid():
            # print('ini form: ',form.cleaned_data.get('tanggal'))
            status = 'Belum Dibalas'
            nama = form.cleaned_data.get('nama')
            alamat = form.cleaned_data.get('alamat')
            email = form.cleaned_data.get('email')
            kd_poli = form.cleaned_data.get('kd_poli')
            no_telp = form.cleaned_data.get('no_telp')
            tanggal = form.cleaned_data.get('tanggal')
            tambahan_pesan = form.cleaned_data.get('tambahan_pesan') 
            data_reg = BookingPeriksa.objects.filter(no_telp=no_telp, tanggal=tanggal).first()
            
            get_lastbooking = BookingPeriksa.objects.using('khanza_db').filter(tanggal=tanggal).last()
            
            no_booking = ''
            if get_lastbooking is not None:
                id_book = get_lastbooking.no_booking[-4:]
                add_idbook = int(id_book) + 1
                next_id = str(add_idbook).zfill(4)
                no_booking = f'BP{tanggal.year}{tanggal.month:02d}{tanggal.day:02d}{next_id}'
                # postdata["no_booking"] = no_booking
            else:
                add_idbook = 1
                next_id = str(add_idbook).zfill(4)
                no_booking = f'BP{tanggal.year}{tanggal.month:02d}{tanggal.day:02d}{next_id}'
                # postdata["no_booking"] = no_booking
                # print('ini nomor booking: ',no_booking)
                
            if today.day >= tanggal.day:
                messages.add_message(request, messages.ERROR,
                                     f'Maaf Registrasi paling lambat dilakukan 1 hari sebelumnya')
                
                return redirect(reverse('ralanurls:booking_view'))
            else:
                BookingPeriksa.objects.create(no_booking=no_booking, 
                                                nama=nama, tanggal=tanggal, 
                                                alamat=alamat, kd_poli=kd_poli, 
                                                no_telp=no_telp, email=email, 
                                                status=status, tambahan_pesan=tambahan_pesan)
                messages.add_message(request, messages.SUCCESS,
                                    f'Registrasi berhasil atas nama {nama}!!')
                return redirect(reverse('ralanurls:booking_view'))
            
        else:
            email = form.cleaned_data.get('email')
            no_telp = form.cleaned_data.get('no_telp')
            tanggal = form.cleaned_data.get('tanggal')
            data_reg = BookingPeriksa.objects.filter(no_telp=no_telp, tanggal=tanggal)
            
            
            if len(data_reg) != 0:
                messages.add_message(request, messages.WARNING,
                                    f'Anda telah melakukan registrasi pemeriksaan pada tanggal ini {tanggal}!!')
                
                return redirect(reverse('ralanurls:booking_view'))
            form = BookingPeriksaForm()
            context = {
                'form':form
            }
            return render(request, 'bookingform.html', context)


class RegPeriksaView(View):
    def get(self, request):
        form = RegPeriksaForm()
        pasien = RegPeriksa.objects.all()
        paginator = Paginator(pasien, 10)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'form':form,
            'pasien':page_obj
        }
        return render(request, 'registrasi.html', context)
    
    def post(self, request):
        data = request.POST
        form = RegPeriksaForm(data)
        if form.is_valid():
            form.save()
            
        return render(request)

class RegPasienView(View):
    def get(self, request):
        pasien = RegPeriksa.objects.all()
        paginator = Paginator(pasien, 10)
        
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context = {
            'pasien':page_obj
        }
        return render(request, '1-listpasien.html', context)


class RegPasienAPIView(ListAPIView):
    queryset = RegPeriksa.objects.all()
    serializer_class = RegPeriksaSerializer
    

class PemeriksaanRanapView(View):
    def get(self, request):
        
        context={}
        return render(request, '2-pengkajian.html', context)