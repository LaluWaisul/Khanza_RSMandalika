from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Dokter
from .serializers import DokterSerializer

# Create your views here.

class DokterAPIView(APIView):
    def get(self, request):
        data = Dokter.objects.filter(kd_sps__isnull=False).values('kd_dokter', 'nm_dokter', 'kd_sps__nm_sps', 'jadwal__kd_poli__nm_poli')
        
        
        serializer = DokterSerializer(data, many=True)
        return Response(serializer.data)