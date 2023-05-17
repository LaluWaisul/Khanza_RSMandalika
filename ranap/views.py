from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import KamarInap
from .serializers import KamarInapSerializer

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
        context ={
            'pasien': pasien
        }
        return render(request, 'listpasien.html', context)

class pengkajian(View):
    def get(self, request):
        contex = {

        }
        return render(request, 'pengkajian.html', contex)
    


