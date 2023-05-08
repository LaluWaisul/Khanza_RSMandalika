import os
import mimetypes
from django.conf import settings
from django.db.models import CharField
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.views import View
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.test import APIRequestFactory
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.utils.http import urlencode
from django.db.models import Sum, Case, When, F, Value, ExpressionWrapper, FloatField, Count, Q, Window
from django.db.models.lookups import GreaterThan, LessThan
from django.db.models.functions import Round

from .serializers import AkreditasiFileSerializer, KategoriElementPenilaianSerializer, ProsentasePerpokjaSerializer, ProsentaseAkreditasiSerializer, KategoriEPSerializer
from .models import ElementPenilaian, FileAkreditasi, KategoriElementPenilaian, PokjaAkreditasi, StandarAkreditasi
from .forms import ElementPenilaianForm, FileForm, KategoriElementPenilaianForm, PokjaForm, StandarForm

################################ CONFIG ######################################
    
def build_url(*args, **kwargs):
    params = kwargs.pop('params', {})
    url = reverse(*args, **kwargs)
    print('ini pramas: ',params)
    if params:
        url += '?' + urlencode(params)
    return url

def get_pokja_user(user):
    try:
        obj = PokjaAkreditasi.objects.get(nama = user).nama
    except:
        obj = None
        
    return obj


def get_user_profil(user):
    try:
        profil = user.profil_user.pokja.nama
    except:
        profil = None
        
    return profil
################################ DASHBOARD ####################################
class AkreditasiDashboard(View):
    def get(self, request):
        getpokja = request.GET.get('pokja')
        currentpokja = None
        if getpokja:
            currentpokja = get_object_or_404(PokjaAkreditasi, id=getpokja)
            
        pokja = PokjaAkreditasi.objects.exclude(nama='admin')
        standar = StandarAkreditasi.objects.filter(pokja=getpokja)
        context={
            "pokja":pokja,
            "currentpokja":currentpokja,
            "standar":standar,
            "dash": "active"
        }
        return render(request, 'dashboard_akre.html', context)

class NilaiPerElementAPIView(APIView):
    def get(self, request):
        pokja = request.query_params.get('pokja')
        standar = request.query_params.get('standar')
        element = request.query_params.get('element')
        elementpenilaian = KategoriElementPenilaian.objects.filter(element__standar__pokja=pokja, element__standar=standar, element=element)
        data = elementpenilaian.values('element__standar__nama', 'element__nama').distinct().annotate(
            nilaitotal = Window(expression=Sum('skor'), partition_by=[F('element__nama')])).annotate(
                nilai=Window(expression=Sum('skor'), partition_by=[F('element__nama')])).annotate(
                    percentage=Round(ExpressionWrapper(F('nilai')*100.0/F('nilaitotal'), output_field=FloatField()), 2)
                )

        serializer = KategoriElementPenilaianSerializer(data, many=True)
        return Response(serializer.data)
    

class FileAKreditasiAPIView(APIView):
    def get(self, request, pk, **kwargs):
        # data_id = kwargs['id']
        data_id = request.GET.get('id')
        data = get_object_or_404(FileAkreditasi, id=pk)
        serializer = AkreditasiFileSerializer(data)
        return Response(serializer.data)
    
    
class NilaiPerStandarAPIView(APIView):
    def get(self, request):
        getpokja = request.query_params.get('pokja')
        pokja = PokjaAkreditasi.objects.first()
        if getpokja:
            pokja = getpokja
        elementpenilaian = KategoriElementPenilaian.objects.filter(element__standar__pokja=pokja)
        datapenilaian = elementpenilaian.values('element__standar__pokja__nama', 'element__standar__nama').annotate(
            # element = F('element__standar__nama'),
            nilaitotal = Window(expression=Sum('skor_max'), partition_by=[F('element__standar')])).distinct().order_by('element__standar').annotate(
                nilai=Window(expression=Sum('skor'), partition_by=[F('element__standar')])).distinct().order_by('element__standar').annotate(
                    percentage=Round(ExpressionWrapper(F('nilai')*100.0/F('nilaitotal'), output_field=FloatField()), 2)
                ).order_by('-percentage').annotate(
                    backgroundcolor = ExpressionWrapper(Case(When(Q(percentage__gte=80), then=Value('rgba(0, 255, 0, 0.2)')), When(Q(percentage__lt=80), then=Value('rgba(255, 0, 0, 0.2)'))), output_field=CharField())
                ).order_by('-percentage')
        
        factory = APIRequestFactory()
        requestdata = factory.get('/')
        serializer_context = {
            'request': Request(requestdata),
        }
        label = datapenilaian.values_list('element__standar__nama', flat=True)
        data = datapenilaian.values_list('percentage', flat=True)
        backgroundcolor = datapenilaian.values_list('backgroundcolor', flat=True)
        # serializer = KategoriElementPenilaianSerializer(elementpenilaian, context=serializer_context, many=True)
        context={
            'label': label,
            'data': data,
            'backgroundcolor':backgroundcolor,
            # 'element': serializer.data
        }
        return Response(context)
    
    
class NilaiPerPokjaAPIView(APIView):
    def get(self, request):
        elementpenilaian = KategoriElementPenilaian.objects.all()
        datapenilaian = elementpenilaian.values('element__standar__pokja__nama').distinct().annotate(
            nilaitotal = Window(expression=Sum('skor_max'), partition_by=[F('element__standar__pokja')])).order_by('element__standar__pokja').annotate(
                nilai=Window(expression=Sum('skor'), partition_by=[F('element__standar__pokja')])).order_by('element__standar__pokja').annotate(
                    percentage=Round(ExpressionWrapper(F('nilai')*100.0/F('nilaitotal'), output_field=FloatField()), 2)
                ).order_by('percentage').annotate(
                    backgroundcolor = ExpressionWrapper(Case(When(Q(percentage__gte=80), then=Value('rgba(0, 255, 0, 0.2)')), When(Q(percentage__lt=80), then=Value('rgba(255, 0, 0, 0.2)'))), output_field=CharField())
                ).order_by('-percentage')

        label = datapenilaian.values_list('element__standar__pokja__nama', flat=True)
        data = datapenilaian.values_list('percentage', flat=True)
        backgroundcolor = datapenilaian.values_list('backgroundcolor', flat=True)
        serializer = ProsentasePerpokjaSerializer(data, many=True)
        context={
            'label': label,
            'data': data,
            'backgroundcolor':backgroundcolor,
        }
        return Response(context)


class NilaiAkreditasiAPIView(APIView):
    def get(self, request):
        elementpenilaian = KategoriElementPenilaian.objects.all()
        datapenilaian = elementpenilaian.values('element__standar__pokja__rumah_sakit__nama').annotate(
            nilaitotal = Sum(F('skor_max')),
            nilai=Sum(F('skor')),
            capaian=Round(F('nilai')*100.0/F('nilaitotal'), 2),
            sisa_target = 100-F('capaian')
        )
                

        # data = datapenilaian.values_list('capaian', flat=True)
        serializer = ProsentaseAkreditasiSerializer(datapenilaian, many=True)
        # dataserializer = KategoriElementPenilaianSerializer(elementpenilaian, many=True)
        labelgrafik = ['Sudah Tercapai', 'Belum Tercapai']
        datagrafik = [serializer.data[0]['capaian'], serializer.data[0]['sisa_target']]
        context={
            'data': datagrafik,
            'label': labelgrafik
        }
        return Response(context)

############################################# POKJA ###########################################

class PokjaView(LoginRequiredMixin, View):
    login_url = '/'
    redirect_field_name = 'redirect_to'
    
    def get(self, request):
        data_display = "list"
        opsi_display = request.GET.get("list")
        if opsi_display:
            data_display = opsi_display
        user = get_user_profil(request.user)
        pokja = PokjaAkreditasi.objects.exclude(nama='admin')
        
        data = []
        if user == 'admin':        
            data = PokjaAkreditasi.objects.exclude(nama='admin').order_by('id')
        elif get_pokja_user(user) == user:
            data = pokja.filter(nama=user)
        else:
            data = None
        
        context={
            "data": data,
            "display":data_display,
            "akreditasi": "active",
            "user": user
        }
        return render(request, 'pokja_page.html', context)
    
    
class TambahPokjaView(LoginRequiredMixin, View):
    login_url = '/'
    redirect_field_name = 'redirect_to'
    
    def get(self, request):
        form = PokjaForm                
        context={
            "form":form,
            "akreditasi": "active"
        }
        return render(request, 'formdata.html', context)
    
    def post(self, request):
        postdata = request.POST
        params=request.GET.get('list')
        form = PokjaForm(postdata)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(build_url('akreditasiurls:pokja_akreditasi', params={'list':params}))
        
        context={
            'form':form,
            "akreditasi": "active"
        }
        return render(request, 'formdata.html', context)
    
class EditPokjaView(LoginRequiredMixin, View):
    model = PokjaAkreditasi
    form_class = PokjaForm
    template = 'formdata.html'
    login_url = '/'
    redirect_field_name = 'redirect_to'
    
    def get_object(self):
        id = self.kwargs.get('id')

        if id is not None:
            obj=get_object_or_404(self.model, id=id)
            return obj
        return None
        
    def get(self, request, id=None):
        form = self.form_class()
        obj = self.get_object()
        if obj is not None:
            form = self.form_class(instance=obj)
        context={
            'form':form,
            "akreditasi": "active"
        }
        return render(request, self.template, context)
    
    def post(self, request, id=None):
        postdata = request.POST
        params=request.GET.get('list')
        obj = self.get_object()
        form = self.form_class(postdata, instance=obj)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(build_url('akreditasiurls:pokja_akreditasi', params={'list':params}))
        
        context={
            'form':form,
            "akreditasi": "active"
        }
        return render(request, self.template, context)
    
############################################ STANDAR AKREDITASI #######################################################

class StandarAkreditasiView(LoginRequiredMixin, View):
    login_url = '/'
    redirect_field_name = 'redirect_to'
    
    def get(self, request, *args, **kwargs):
        pokjaId = kwargs.get('id')
        pokja = get_object_or_404(PokjaAkreditasi, id=pokjaId)
        data_display = "list"
        opsi_display = request.GET.get("list")
        if opsi_display:
            data_display = opsi_display
        user = get_user_profil(request.user)
        
        data = []
        if user == 'admin':
            data = StandarAkreditasi.objects.filter(pokja=pokjaId).order_by('id')
        elif get_pokja_user(user) == user:
            data = StandarAkreditasi.objects.filter(pokja__nama=user).order_by('id')
        
        context={
            "data": data,
            "display":data_display,
            "item":pokja,
            "akreditasi": "active"
        }
        return render(request, 'standard_page.html', context)
    
    
class TambahStandarAkreditasiView(LoginRequiredMixin, View):
    login_url = '/'
    redirect_field_name = 'redirect_to'
    
    def get(self, request, **kwargs):
        pokjaId = kwargs.get('id')
        pokja = get_object_or_404(PokjaAkreditasi, id=pokjaId)
        standar = StandarAkreditasi.objects.filter(pokja=pokja)
        form = StandarForm({'pokja':pokja, 'nama': f'{pokja.nama} {len(standar)+1}'})       
        context={
            "form":form,
            "item": pokja,
            "akreditasi": "active"
        }
        return render(request, 'formdata_akre.html', context)
    
    def post(self, request, **kwargs):
        pokjaId = kwargs.get('id')
        params = request.GET.get('list')
        postdata = request.POST
        
        form = StandarForm(postdata)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(build_url('akreditasiurls:standar_view', kwargs={'id':pokjaId}, params={'list':params}))
        
        context={
            'form':form,
            "akreditasi": "active"
        }
        return render(request, 'formdata.html', context)
    
class EditStandarAkreditasiView(LoginRequiredMixin, View):
    model = StandarAkreditasi
    form_class = StandarForm
    template = 'formdata_akre.html'
    
    def get_object(self):
        id = self.kwargs.get('id')

        if id is not None:
            obj=get_object_or_404(self.model, id=id)
            return obj
        return None
        
    def get(self, request, id=None, **kwargs):
        form = self.form_class()
        obj = self.get_object()
        if obj is not None:
            form = self.form_class(instance=obj)
        context={
            'form':form,
            'item':obj,
            "akreditasi": "active",
        }
        return render(request, self.template, context)
    
    def post(self, request, id=None, **kwargs):
        postdata = request.POST
        params = request.GET.get('list')
        obj = self.get_object()
        form = self.form_class(data=postdata, instance=obj)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(build_url('akreditasiurls:standar_view', kwargs={'id':obj.pokja.id}, params={'list':params}))
        
        context={
            'form':form,
            "akreditasi": "active"
        }
        return render(request, self.template, context)
    
    
############################################ ELEMENT PENILAIAN #######################################################

class ElementPenilaianView(LoginRequiredMixin, View):
    login_url = '/'
    redirect_field_name = 'redirect_to'
    
    def get(self, request, *args, **kwargs):
        standarId = kwargs.get('id')
        standar = get_object_or_404(StandarAkreditasi, id=standarId)
        data_display = "list"
        opsi_display = request.GET.get("list")
        if opsi_display:
            data_display = opsi_display
        user = get_user_profil(request.user)
        
        data = []
        if user == 'admin':
            data = ElementPenilaian.objects.filter(standar=standarId).order_by('id')
        elif get_pokja_user(user) == user:
            data = ElementPenilaian.objects.filter(standar__pokja__nama=user, standar=standarId).order_by('id')
        
        idpokja = ''
        if data:
            idpokja = data[0].standar.pokja
        
        context={
            "data": data,
            "idpokja": idpokja,
            "display":data_display,
            "item":standar,
            "akreditasi": "active"
        }
        return render(request, 'element_penilaian_page.html', context)
    
    
class TambahElementPenilaianView(LoginRequiredMixin, View):
    login_url = '/'
    redirect_field_name = 'redirect_to'
    
    def get(self, request, **kwargs):
        standarId = kwargs.get('id')
        standar = get_object_or_404(StandarAkreditasi, id=standarId)
        ep = ElementPenilaian.objects.filter(standar=standar)
        form = ElementPenilaianForm({'standar':standar, 'nama':f'EP {len(ep)+1}', 'jlh_kat_skor':3, 'skor':0}) 
                    
        context={
            "form":form,
            "item": standar,
            "akreditasi": "active"
        }
        return render(request, 'formdata_akre.html', context)
    
    def post(self, request, **kwargs):
        standarId = kwargs.get('id')
        params = request.GET.get('list')
        postdata = request.POST
        
        form = ElementPenilaianForm(postdata)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(build_url('akreditasiurls:element_penilaian_view', kwargs={'id':standarId}, params={'list':params}))
        
        context={
            'form':form,
            "akreditasi": "active"
        }
        return render(request, 'formdata_akre.html', context)
    
class EditElementPenilaianView(LoginRequiredMixin, View):
    model = ElementPenilaian
    form_class = ElementPenilaianForm
    template = 'formdata_akre.html'
    login_url = '/'
    redirect_field_name = 'redirect_to'
        
    def get_object(self):
        id = self.kwargs.get('id')

        if id is not None:
            obj=get_object_or_404(self.model, id=id)
            return obj
        return None
        
    def get(self, request, id=None):
        form = self.form_class()
        obj = self.get_object()
        if obj is not None:
            form = self.form_class(instance=obj)
        context={
            'form':form,
            'item':obj,
            "akreditasi": "active"
        }
        return render(request, self.template, context)
    
    def post(self, request, id=None):
        postdata = request.POST
        params = request.GET.get('list')
        obj = self.get_object()
        form = self.form_class(data=postdata, instance=obj)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(build_url('akreditasiurls:element_penilaian_view', kwargs={'id':obj.standar.id}, params={'list':params}))
        
        context={
            'form':form,
            "akreditasi": "active"
        }
        return render(request, self.template, context)


############################################ KATEGORI ELEMENT PENILAIAN ############################################

class KategoriElementPenilaianView(LoginRequiredMixin, View):
    login_url = '/'
    redirect_field_name = 'redirect_to'
    
    def get(self, request, *args, **kwargs):
        elementId = kwargs.get('id')
        element = get_object_or_404(ElementPenilaian, id=elementId)
        data_display = "list"
        opsi_display = request.GET.get("list")
        if opsi_display:
            data_display = opsi_display
        user = get_user_profil(request.user)
        
        data = []
        if user == 'admin':
            data = KategoriElementPenilaian.objects.filter(element=elementId).order_by('id')
        elif get_pokja_user(user) == user:
            data = KategoriElementPenilaian.objects.filter(element=elementId, element__standar__pokja__nama=user).order_by('id')
        
        idstandar = ''
        if data:
            idstandar = data[0].element.standar
        context={
            "data": data,
            "idstandar": idstandar,
            "display":data_display,
            "item":element,
            "akreditasi": "active"
        }
        return render(request, 'kat_element_penilaian_page.html', context)
    
    def post(self, request, *args, **kwargs):
        id = kwargs.get('id')
        idkategori = kwargs.get('kategori')
        params=request.GET.get('list')

        obj=get_object_or_404(KategoriElementPenilaian, id=id)
        if obj:
            return HttpResponseRedirect(build_url('akreditasiurls:delete_ep', kwargs={'id':obj.id}, params={'list':params}))
    
def delete_kategori_ep(request, id):
    params=request.GET.get('list')
    return None

class DataAPI(APIView):
    def get(self, request):
        data = KategoriElementPenilaian.objects.all()
        
        serializer = KategoriElementPenilaianSerializer(instance=data, many=True, context={'request':request})
        return Response(serializer.data)

class TambahKategoriElementPenilaianView(LoginRequiredMixin, View):
    login_url = '/'
    redirect_field_name = 'redirect_to'
    
    def get(self, request, **kwargs):
        elementId = kwargs.get('id')
        element = get_object_or_404(ElementPenilaian, id=elementId)
        form = KategoriElementPenilaianForm({'element':element, 'nama':'', 'jlh_kat_skor':3, 'skor':0}) 
                    
        context={
            "form":form,
            "item": element,
            "akreditasi": "active"
        }
        return render(request, 'formdata_akre.html', context)
    
    def post(self, request, **kwargs):
        elementId = kwargs.get('id')
        params = request.GET.get('list')
        postdata = request.POST
        
        form = KategoriElementPenilaianForm(postdata)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(build_url('akreditasiurls:kat_element_penilaian_view', kwargs={'id':elementId}, params={'list':params}))
        
        context={
            'form':form,
            "akreditasi": "active"
        }
        return render(request, 'formdata_akre.html', context)
    
class EditKategoriElementPenilaianView(LoginRequiredMixin, View):
    model = KategoriElementPenilaian
    form_class = KategoriElementPenilaianForm
    template = 'formdata_akre.html'
    login_url = '/'
    redirect_field_name = 'redirect_to'
        
    def get_object(self):
        id = self.kwargs.get('id')

        if id is not None:
            obj=get_object_or_404(self.model, id=id)
            return obj
        return None
        
    def get(self, request, id=None):
        form = self.form_class()
        obj = self.get_object()
        if obj is not None:
            form = self.form_class(instance=obj)
        context={
            'form':form,
            'item':obj,
            "akreditasi": "active"
        }
        return render(request, self.template, context)
    
    def post(self, request, id=None):
        postdata = request.POST
        params = request.GET.get('list')
        obj = self.get_object()
        form = self.form_class(data=postdata, instance=obj)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(build_url('akreditasiurls:kat_element_penilaian_view', kwargs={'id':obj.element.id}, params={'list':params}))
        
        context={
            'form':form,
            "akreditasi": "active"
        }
        return render(request, self.template, context)

    
############################################ FILE AKREDITASI #######################################################

class SearchAkreditasiFileAPIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        nama=request.query_params.get('nama')
        user = get_user_profil(request.user)
        user2 = self.request.user
        # print(user)
        # print('ini user2: ',user2)
        
        data = FileAkreditasi.objects.filter(
            nama__icontains=nama) | FileAkreditasi.objects.filter(
                kategori__nama__icontains=nama) | FileAkreditasi.objects.filter(
                    kategori__element__nama__icontains=nama) | FileAkreditasi.objects.filter(
                        kategori__element__standar__nama__icontains=nama) |FileAkreditasi.objects.filter(
                            kategori__element__standar__pokja__nama__icontains=nama)
        
        limitdata = data[:20]
        serializer = AkreditasiFileSerializer(limitdata, many=True)
        context={
            'data':serializer.data,
            'user':user
        }
        return Response(context, status=status.HTTP_200_OK)

class DashboardFileAkreditasi(APIView):
    def get(self, request):
        getpokja = request.GET.get('pokja')
        pokja = PokjaAkreditasi.objects.first()
        if getpokja:
            pokja = getpokja
        else:
            pokja=pokja.id
        data = FileAkreditasi.objects.filter(kategori__element__standar__pokja__id=pokja)
        print(data)
        serializer=AkreditasiFileSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
        
class ElementPenilaianAPIView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        
        data = get_object_or_404(ElementPenilaian, id=id)
        serializer = AkreditasiFileSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
          
class ElementAkreditasiFileAPIView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        
        data = get_object_or_404(FileAkreditasi, id=id)
        serializer = AkreditasiFileSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ElementAkreditasiFileView(LoginRequiredMixin, View):
    login_url = '/'
    redirect_field_name = 'redirect_to'
    
    def get(self, request, *args, **kwargs):
        idkategori = kwargs.get('id')
        data_display = "list"
        opsi_display = request.GET.get("list")
        if opsi_display:
            data_display = opsi_display
        kategori = get_object_or_404(KategoriElementPenilaian, id=idkategori)
        data = FileAkreditasi.objects.filter(kategori=idkategori).order_by('id')
        
        idelement = kategori.element
        
        context={
            "data": data,
            "idelement": idelement,
            "display":data_display,
            "kategori":idkategori,
            "item":kategori,
            "akreditasi": "active"
        }
        return render(request, 'file_page.html', context)
    
    def post(self, request, *args, **kwargs):
        id = kwargs.get('id')
        idkategori = kwargs.get('kategori')
        params=request.GET.get('list')

        obj=get_object_or_404(FileAkreditasi, id=id)
        obj.delete()
        
        return HttpResponseRedirect(build_url('akreditasiurls:delete_file', kwargs={'id':idkategori}, params={'list':params}))


class AkreditasiFileView(LoginRequiredMixin, View):
    login_url = '/'
    redirect_field_name = 'redirect_to'
    
    def get(self, request, *args, **kwargs):
        idkategori = kwargs.get('kategori')
        id=kwargs.get('id')
        data_display = "list"
        opsi_display = request.GET.get("list")
        if opsi_display:
            data_display = opsi_display
            
        kategori = get_object_or_404(KategoriElementPenilaian, id=idkategori)
        data = FileAkreditasi.objects.filter(kategori=idkategori).order_by('id')
        obj = get_object_or_404(FileAkreditasi, id=id)
        
        idelement = ''
        idelement = kategori.element
        
        context={
            "data": data,
            "idelement": idelement,
            "display":data_display,
            "kategori":idkategori,
            "item":kategori,
            "file":obj,
            "akreditasi": "active"
        }
        return render(request, 'file_page.html', context)
    
    def post(self, request, *args, **kwargs):
        id = kwargs.get('id')
        idkategori = kwargs.get('kategori')
        params=request.GET.get('list')

        obj=get_object_or_404(FileAkreditasi, id=id)
        obj.delete()
        
        return HttpResponseRedirect(build_url('akreditasiurls:element_file_view', kwargs={'id':idkategori}, params={'list':params}))
    
 
class TambahAkreditasiFileView(LoginRequiredMixin, View):
    login_url = '/'
    redirect_field_name = 'redirect_to'
    
    def get(self, request, **kwargs):
        kategoriId = kwargs.get('id')
        kategori = get_object_or_404(KategoriElementPenilaian, id=kategoriId)
        form = FileForm({'kategori':kategori, 'status':'Belum Dikerjakan'})            
        context={
            "form":form,
            "item":kategori,
            "akreditasi": "active"
        }
        return render(request, 'formdata_akre.html', context)
    
    def post(self, request, **kwargs):
        id = kwargs.get('id')        
        params=request.GET.get('list')
        form = FileForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(build_url('akreditasiurls:element_file_view', kwargs={'id':id}, params={'list':params}))
        
        # return render(request, 'formdata.html', status=status.HTTP_400_BAD_REQUEST)
        context={
            'form':form,
            "akreditasi": "active"
        }
        return render(self.request, 'formdata_akre.html', context)
    
    
class EditAkreditasiFileView(LoginRequiredMixin, View):
    model = FileAkreditasi
    form_class = FileForm
    template = 'formdata_akre.html'
    login_url = '/'
    redirect_field_name = 'redirect_to'
    
    def get_object(self, **kwargs):
        id = self.kwargs.get('id')

        if id is not None:
            obj=get_object_or_404(self.model, id=id)
            return obj
        return None
        
    def get(self, request, id=None):
        form = self.form_class()
        obj = self.get_object()
        if obj is not None:
            form = self.form_class(instance=obj)
        context={
            'form':form,
            "akreditasi": "active"
        }
        return render(request, self.template, context)
    
    def post(self, request, id=None):
        id = self.kwargs.get('id')
        params = request.GET.get('list')
        obj = self.get_object()
        form = self.form_class(request.POST, request.FILES, instance=obj)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(build_url('akreditasiurls:element_file_view', kwargs={'id':obj.kategori.id}, params={'list':params}))
        
        context={
            'form':form,
            "akreditasi": "active"
        }
        return render(request, self.template, context)
    

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    
    if os.path.exists(file_path):
        
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_path))
            response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
            return response
    raise Http404

class DownloadAPIView(View):

    def get(self, request, **kwargs):
        idfile = kwargs.get('id')
        file = get_object_or_404(FileAkreditasi, id=idfile)
        file_path = file.file.path
        if os.path.exists(file_path):
        
            with open(file_path, 'rb') as fh:
                response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_path))
                response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
                return response
        raise Http404