from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.core.paginator import Paginator
from django import forms

from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from ralan.models import RegPeriksa 
from ralan.serializers import RegPeriksaSerializer
from .forms import SearchForm, PengkajianKeperawatanForm
from .models import PenilaianAwalKeperawatanIgd

# Create your views here.

class RegPasienIGDView(View):
    def get(self, request):
        pasien = RegPeriksa.objects.all()
        paginator = Paginator(pasien, 10)
        
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        page_obj = paginator.get_page(page_number)
        
        
        data = request.GET.get('data')
        form = SearchForm()
        if data:
            pasien = RegPeriksa.objects.filter(
                no_rawat=data
            ) | RegPeriksa.objects.filter(
                no_rkm_medis__no_rkm_medis__icontains=data
            ) | RegPeriksa.objects.filter(
                no_rkm_medis__nm_pasien__icontains=data
            ) | RegPeriksa.objects.filter(
                kd_poli__nm_poli__icontains=data
            ) | RegPeriksa.objects.filter(
                kd_dokter__nm_dokter__icontains=data)
            paginator = Paginator(pasien, 10)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            
        context = {
            'pasien':page_obj,
            'form':form,
            'data':data,
            'igd':'active',
            'listpasien':'active'
        }
        return render(request, '1-listpasien.html', context)
    

class ListPasienAPIView(APIView):
    def get(self, request):
        data=request.query_params.get('data')
        
        pasien = RegPeriksa.objects.all() | RegPeriksa.objects.filter(
            no_rawat=data
        ) | RegPeriksa.objects.filter(
            no_rkm_medis__no_rkm_medis=data
        ) | RegPeriksa.objects.filter(
            no_rkm_medis__nm_pasien=data
        ) | RegPeriksa.objects.filter(
            kd_poli__nm_poli=data
        ) | RegPeriksa.objects.filter(
            kd_dokter__nm_dokter=data)
        
        searchdata = pasien[:10]
        serializer = RegPeriksaSerializer(searchdata, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class PengkajianKeperawatanView(View):
    form_class = PengkajianKeperawatanForm
    model = PenilaianAwalKeperawatanIgd
    
    def get_object(self, **kwargs):
        no_rawat = self.kwargs.get('norawat')
        norawat= no_rawat.replace('-','/')
        
        if no_rawat is not None:
            obj = get_object_or_404(RegPeriksa, no_rawat=norawat)
            # obj = RegPeriksa.objects.filter(no_rawat=no_rawat)
            if obj:
                return obj
        return None
    
    def get(self, request, norawat=None):
        form = self.form_class()
        obj = self.get_object()
        # obj, create=self.model.objects.get_or_create(no_rawat=pasien)
        if obj :
            form = self.form_class(instance=obj)
        # else:
        #     form = self.form_class(instance=create)
        # form.base_fields['no_rawat']=forms.ModelChoiceField(initial=obj, queryset=RegPeriksa.objects.all())
            
        context={
            'form':form,
            'obj':obj,
            'igd':'active',
            'pengkajian':'active'
        }
        return render(request, '2-pengkajian.html', context)