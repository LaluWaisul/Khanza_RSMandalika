from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.core.paginator import Paginator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django import forms

from .models import KamarInap,PemeriksaanRanap
from .serializers import KamarInapSerializer

from .form import form_serach,formPenanganan

# Create your views here.


class ListPasienAPIView(APIView):
    def get(self, request):
        data=request.query_params.get('data')
        tgl_masuk_start = request.query_params.get('masuk-start')
        tgl_masuk_finish = request.query_params.get('masuk-finish')
        tgl_pulang_start = request.query_params.get('keluar-start')
        tgl_pulang_finish = request.query_params.get('keluar-finish')
        
        pasien = KamarInap.objects.all() | KamarInap.objects.filter(
            no_rawat__status_bayar=data
        ) | KamarInap.objects.filter(
            tgl_masuk__gte=tgl_masuk_start, tgl_masuk__lte=tgl_masuk_finish
        ) | KamarInap.objects.filter(
            tgl_keluar__gte=tgl_pulang_start, tgl_keluar__lte=tgl_pulang_finish
        ) | KamarInap.objects.filter(
            stts_pulang=data
        )
        
        serializer = KamarInapSerializer(pasien)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
class ListPasien(View):
    def get(self, request):
        pasien = KamarInap.objects.all()
        paginator = Paginator(pasien, 25)
        SearchForm = form_serach

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        page_obj = paginator.get_page(page_number)

        data = request.GET.get('data')
        form = SearchForm()
        if data:
            pasien = KamarInap.objects.filter(
                no_rawat= data
            ) | KamarInap.objects.filter(
                no_rawat__no_rkm_medis__no_rkm_medis__icontains=data
            ) | KamarInap.objects.filter(
                no_rawat__no_rkm_medis__nm_pasien__icontains=data
            ) | KamarInap.objects.filter(
                kd_kamar=data)
            paginator = Paginator(pasien, 25)
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)

        context ={
            'pasien':page_obj,
            'form':form,
            'data':data,
            'ranap':'active',
        }
        return render(request, 'listpasien.html', context)

class TindakanRanap(View):
    def get(self, request):
        context = {
            # form = formPenanganan
        }
        return render(request, 'tindakan.html',context)