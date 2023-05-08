from django.shortcuts import render
from django.views import View
from django.db.models import Sum, Case, When, F, Value, ExpressionWrapper, FloatField, Count, Q
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Kamar, Bangsal
from .serializers import InformasiTempatTidurSerializer

# Create your views here.


class InformasiTempatTidur(View):
    def get(self, request):
        data = Kamar.objects.filter(status='')
        kamar = Kamar.objects.filter(statusdata=1).values('kd_bangsal__nm_bangsal', 'trf_kamar').annotate(
            jlh_total_kamar = Count(Case(When(Q(statusdata=1), then=F('kd_kamar')))),
            jlh_kamar_kosong = Count(Case(When(Q(status='KOSONG'), then=F('kd_kamar')))),
            jlh_kamar_isi = Count(Case(When(Q(status='ISI'), then=F('kd_kamar')))),
            jlh_kamar_booking = Count(Case(When(Q(status='DIBOOKING'), then=F('kd_kamar')))),
        )
        # print('datakamar: ', kamar)
        context={
            'kamar':kamar
        }
        return render(request, 'kamar.html', context)
    
class InformasiTempatTidurAPIView(APIView):
    def get(self, request):
        kamar = Kamar.objects.filter(statusdata=1).values('kd_bangsal__nm_bangsal', 'trf_kamar').annotate(
            jlh_total_kamar = Count(Case(When(Q(statusdata=1), then=F('kd_kamar')))),
            jlh_kamar_kosong = Count(Case(When(Q(status='KOSONG'), then=F('kd_kamar')))),
            jlh_kamar_isi = Count(Case(When(Q(status='ISI'), then=F('kd_kamar')))),
            jlh_kamar_booking = Count(Case(When(Q(status='DIBOOKING'), then=F('kd_kamar')))),
        )
        serializer = InformasiTempatTidurSerializer(kamar, many=True)
        return Response(serializer.data)