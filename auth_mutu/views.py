from cmath import nan
from operator import index
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum, Case, When, F, Value, ExpressionWrapper, FloatField, Count, Q, Func, Aggregate
from django.urls import reverse
from django.contrib.postgres.aggregates import ArrayAgg
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date, datetime
import pandas as pd
import numpy as np

from .models import Bulan, DataIndikatorMutu, IndikatorMutu
from auth_bangsal.models import Departement, Bidang, Bangsal
from .forms import DataIndikatorMutuForm, FormMutuNasional, IndikatorMutuForm, MutuNasionalFormset
from .utils import get_chart, get_chart_instalasi, get_chart_series, get_chart_series_bulan, get_graph

# Create your views here.

def dashboard(request):
    context={
        'dash':'active'
    }
    return render(request, 'dashboard.html', context)


class TambahDataMutuView(View):
    template = 'tambahdata.html'
    model = DataIndikatorMutu
    
    def get(self, request, *args, **kwargs):
        indimut = IndikatorMutu.objects.using('auth_db').all()
        get_tanggal = kwargs['tanggal_isi']
        get_bangsal = request.GET.get('bangsal')
        tanggal = date.today()
        bangsal = None
        
        if get_bangsal:
            bangsal = get_object_or_404(Bangsal, kd_bangsal=get_bangsal)
        elif request.user.profil_user.instalasi:
            bangsal = Bangsal.objects.using('auth_db').filter(nama=request.user.profil_user.instalasi).first()
        else:
            bangsal = Bangsal.objects.using('auth_db').first()
        
        if get_tanggal:
            tanggal = datetime.strptime(get_tanggal, "%Y-%m-%d").date()
            
        # print(tanggal)
        
        datamutu=self.model.objects.using('auth_db').filter(tanggal_isi__day=tanggal.day, bangsal=bangsal)
        # print('ini datamutu: ',datamutu)
        if datamutu:
            bulan = tanggal.strftime("%d %B %Y")
        else:
            for item in indimut:
                datamutu = self.model.objects.create(
                    tanggal_isi=tanggal, bangsal=bangsal, ind_mutu=item)
            
            datamutu=self.model.objects.using('auth_db').filter(tanggal_isi__day=tanggal.day, bangsal=bangsal)
            bulan = tanggal.strftime("%d %B %Y")
        
        
        form = MutuNasionalFormset(queryset=datamutu)
        context={
            'form': form,
            'tanggal': bulan,
            'bangsal': bangsal,
            'munas': 'active'
        }
        
        return render(request, self.template, context)
    
    def post(self, request, *args, **kwargs):
        get_tanggal = kwargs['tanggal_isi']
        get_bangsal = request.GET.get('bangsal')
        tanggal = date.today()
        
        if get_bangsal:
            bangsal = get_object_or_404(Bangsal, kd_bangsal=get_bangsal)
        elif request.user.profil_user.instalasi:
            bangsal = Bangsal.objects.using('auth_db').filter(nama=request.user.profil_user.instalasi).first()
        else:
            bangsal = Bangsal.objects.using('auth_db').all().first()
        
        if get_tanggal:
            tanggal = datetime.strptime(get_tanggal, "%Y-%m-%d").date()
            
        # print(tanggal.date())
        
        postdata = request.POST
        # print('ini postdata: ',self.model.objects.using('auth_db').filter(tanggal_isi__month=tanggal.month, bangsal=bangsal))
        formset = MutuNasionalFormset(queryset=self.model.objects.using('auth_db').filter(tanggal_isi__month=tanggal.month, bangsal=bangsal), data=postdata)
        # form = formset(request.POST)
        if formset.is_valid():
            formset.save()
            # print('ini form: ',formset)
            return HttpResponseRedirect(reverse('auth_mutu:data-mutu'))
        else:
            print('data not valid')
            
        context={
            'form':formset,
            'munas': 'active'
        }
        return render(request, self.template, context)    


def div(numerator, denominator):
    return lambda row: 0.0 if row[denominator] == 0 else float(((row[numerator]/row[denominator])*100))

class CapaianMutuHari(LoginRequiredMixin, View):
    model = DataIndikatorMutu
    form_class = DataIndikatorMutuForm
    template = 'formsearch.html'
    
    def get(self, request, *args, **kwargs):
        dep = None
        bidang = None
        bangsal = None
        df = None
        displaydatamutu = None
        
        tanggal = date.today()
        form = DataIndikatorMutuForm()
        get_tanggal = request.GET.get('tanggal_isi')
        get_bangsal = request.GET.get('bangsal')
        
        allbangsal = Bangsal.objects.using('auth_db').all()
        
        if get_tanggal:
            tanggal = datetime.strptime(get_tanggal, "%Y-%m-%d").date()
            
        indikator = IndikatorMutu.objects.using('auth_db').all()

        try:
            user = request.user.profil_user.instalasi
        except:
            user = None
        print(get_bangsal)
        if get_bangsal:
            bangsal = get_object_or_404(Bangsal, kd_bangsal=get_bangsal)
            bidang = bangsal.bidang.nama
            dep = bangsal.bidang.dep.nama
        
            datamutu = self.model.objects.using('auth_db').filter(bangsal__kd_bangsal=bangsal.kd_bangsal, tanggal_isi__month=tanggal.month, tanggal_isi__year=tanggal.year).values('ind_mutu__nama', 'tanggal_isi', 'numerator', 'denominator')
            df = pd.DataFrame(datamutu)
            # print(datamutu)
            if df.empty:
                displaydatamutu = None
            else:
                #Membuat kolom mutu
                df['Mutu'] = (df['numerator']/df['denominator'])*100
                #Mengambil tanggal dalam Format tanggal
                df['date'] = pd.to_datetime(df['tanggal_isi'])
                df['Tanggal'] = df['date'].dt.strftime('%d')
                # df['Bulan'] = df['date'].dt.strftime('%B')
                
                # pivot_table = df['numerator'] / df.groupby('')['sales'].transform('sum')
                percent_perbulan = df.groupby(['ind_mutu__nama']).agg({'numerator': 'sum', 'denominator':'sum'})
                
                percent_perbulan['total_persen'] = percent_perbulan.apply(div('numerator', 'denominator'), axis=1).round(decimals=2)
                #Menggabungkan kolom numerator dengan denominator
                df['str_num'] = df['numerator'].apply(str)
                df['str_denom'] = df['denominator'].apply(str)
                df['num_denom'] = df[['str_num', 'str_denom']].T.agg('/'.join)
                #Menyesuaikan nama header
                df.rename(columns={'ind_mutu__nama':'Indikator Mutu', 'num_denom':'tgl', 'numerator':'Num', 'denominator':'Denom', 'total_persen':'Total'}, inplace=True)
                #membuat pivot tabel datamutu 
                # print(df)
                pdpivot = df.pivot(index='Indikator Mutu', columns='Tanggal').drop(['date', 'tanggal_isi', 'Mutu', 'Num', 'Denom',
                                                                                    'str_num', 'str_denom'], axis=1)
                
                #Menghitung persentase bulanan
                percent_perbulan = percent_perbulan.rename(columns={'numerator':'Num', 'denominator':'Denom', 'total_persen':'Capaian Mutu'})
                #Menggabungkan pivot table dan persentase bulanan
                datamutupivot = pd.concat([pdpivot, percent_perbulan], axis=1)
                # datamutupivot = pd.merge(pdpivot, percent_perbulan, on='Indikator Mutu')
                #Menampilkan data di HTML
                displaydatamutu = datamutupivot.to_html(classes='table', table_id="kematian")
                
            bulans = Bulan.objects.using('auth_db').all()
            tahun = tanggal.year
            bulan = tanggal.strftime("%B")
        
            
        else:
            datamutu = self.model.objects.using('auth_db').filter(tanggal_isi__month=tanggal.month, tanggal_isi__year=tanggal.year).values('ind_mutu__nama', 'tanggal_isi', 'numerator', 'denominator')
            bulans = Bulan.objects.using('auth_db').all()
            tahun = tanggal.year
            bulan = tanggal.strftime("%B")
            
            df = pd.DataFrame(datamutu)
            if df.empty:
                displaydatamutu = None
            else:
                #Membuat kolom mutu
                df['Mutu'] = (df['numerator']/df['denominator'])*100
                #Mengambil tanggal dalam Format tanggal
                df['date'] = pd.to_datetime(df['tanggal_isi'])
                df['Tanggal'] = df['date'].dt.strftime('%d')
                
                # pivot_table = df['numerator'] / df.groupby('')['sales'].transform('sum')
                percent_perbulan = df.groupby(['ind_mutu__nama']).agg({'numerator': 'sum', 'denominator':'sum'})
                
                percent_perbulan['total_persen'] = percent_perbulan.apply(div('numerator', 'denominator'), axis=1).round(decimals=2)
                # percent_perbulan['total_persen'] = ((percent_perbulan['numerator']/percent_perbulan['denominator'])*100).round(decimals=2)
               
                #Menggabungkan kolom numerator dengan denominator
                # print(percent_perbulan)
                df['str_num'] = df['numerator'].apply(str)
                df['str_denom'] = df['denominator'].apply(str)
                df['num_denom'] = df[['str_num', 'str_denom']].T.agg('/'.join)
                #Menyesuaikan nama header
                df.rename(columns={'ind_mutu__nama':'Indikator Mutu', 'num_denom':'tgl', 'numerator':'Num', 'denominator':'Denom', 'total_persen':'Total'}, inplace=True)
                #membuat pivot tabel datamutu 
                pdpivot = df.pivot(index='Indikator Mutu', columns='Tanggal').drop(['date', 'tanggal_isi', 'Mutu', 'Num', 'Denom', 
                                                                                    'str_num', 'str_denom'], axis=1)
                #Menghitung persentase bulanan
                percent_perbln = percent_perbulan.rename(columns={'numerator':'Num', 'denominator':'Denom', 'total_persen':'Capaian Mutu'})
                #Menggabungkan pivot table dan persentase bulanan
                datamutupivot = pd.concat([pdpivot, percent_perbln], axis=1)
                #Menampilkan data di HTML
                # print(datamutupivot)
                # print(pdpivot)
                displaydatamutu = datamutupivot.to_html(classes='table', table_id="kematian")

        context = {
            'dep': dep,
            'bidang': bidang,
            'bangsal':bangsal,
            'allbangsal': allbangsal,
            'bangsal1':'IGD',
            'data': displaydatamutu,
            'indikator': indikator,
            'tanggal': tanggal,
            'bulans': bulans,
            'bulan': bulan,
            'tahun': tahun,
            'form': form,
            'charttype':'bar',
            'munas': 'active'
        }
        
        return render(request, self.template, context)


class CapaianMutuPerBulan(LoginRequiredMixin, View):
    model = DataIndikatorMutu
    form_class = DataIndikatorMutuForm
    template = 'formsearch.html'
    
    def get(self, request, *args, **kwargs):
        user_unit = request.user.profil_user.instalasi
        dep = Departement.objects.using('auth_db').filter(departement_bidang__bidang_bangsal__nama=user_unit).first()
        bidang = Bidang.objects.using('auth_db').filter(bidang_bangsal__nama = user_unit).first()
        bangsal = None
        df = None
        displaydatamutu = None
        
        tanggal = date.today()
        form = DataIndikatorMutuForm()
        get_tanggal = request.GET.get('tanggal_isi')
        get_bangsal = request.GET.get('bangsal')
        
        chart_type='bar'
        
        if get_tanggal:
            tanggal = datetime.strptime(get_tanggal, "%Y-%m-%d").date()
            
        indikator = IndikatorMutu.objects.using('auth_db').all()
        
        if get_bangsal:
            bangsal = get_object_or_404(Bangsal, kd_bangsal=get_bangsal)

        # get_number = Func(F('numerator')/F('denominator'), function='ROUND')
        if get_bangsal:
            datamutu = self.model.objects.using('auth_db').filter(bangsal__kd_bangsal=bangsal.kd_bangsal, tanggal_isi__year=tanggal.year).values('ind_mutu__nama', 'tanggal_isi', 'numerator', 'denominator')
            tahun = tanggal.year
            bulan = tanggal.strftime("%B")
            
            df = pd.DataFrame(datamutu)
            
            if df.empty:
                displaydatamutu = None
            else:
                #Membuat kolom mutu
                df['Mutu'] = (df['numerator']/df['denominator'])*100
                # print('ini ditambah mutu',df)
                #Mengambil tanggal dalam Format tanggal
                df['date'] = pd.to_datetime(df['tanggal_isi'])
                df['Bulan'] = df['date'].dt.strftime('%B')
                
                # pivot_table = df['numerator'] / df.groupby('')['sales'].transform('sum')
                df.rename(columns={'ind_mutu__nama':'Indikator Mutu', 'numerator':'Numerator', 'denominator':'Denominator'}, inplace=True)
                
                percent = df.groupby(['Indikator Mutu', 'Bulan']).agg({'Numerator': 'sum', 'Denominator':'sum', })
                percent_tahun = df.groupby(['Indikator Mutu']).agg({'Numerator': 'sum', 'Denominator':'sum', })
                # percent_tahun['Pertahun(%)'] = ((percent_tahun['Numerator']/percent_tahun['Denominator'])*100).round(decimals=2)
                percent_tahun['Pertahun(%)'] = percent_tahun.apply(div('Numerator', 'Denominator'), axis=1).round(decimals=2)
                percent_tahun.drop(['Numerator','Denominator'], axis=1, inplace=True)
                # df['total'] = df.agg({'numerator': 'sum', 'denominator':'sum'})
                
                # percent['Prosentase'] = ((percent['Numerator']/percent['Denominator'])*100).round(decimals=2)
                percent['Prosentase'] = percent.apply(div('Numerator', 'Denominator'), axis=1).round(decimals=2)
                # print([x[0] for x in percent.index])
                num_denom = (percent['Numerator'].sum())+(percent['Denominator'].sum())
                # print(num_denom)
                if num_denom > 0:
                    pivotdata = percent.pivot_table(index='Indikator Mutu', columns='Bulan').drop(['Numerator','Denominator'], axis=1)
                    # mergedata = pd.merge(pivotdata, percent_tahun, on='Indikator Mutu')
                    mutudata = pd.concat([pivotdata, percent_tahun], axis=1)
                    displaydatamutu = mutudata.to_html(classes='table', table_id="kematian")
                else:
                    pivotdata = percent.pivot_table(index='Indikator Mutu', columns='Bulan')
                    displaydatamutu = pivotdata.to_html(classes='table', table_id="kematian")
        
            
        else:
            datamutu = self.model.objects.using('auth_db').filter(tanggal_isi__year=tanggal.year).values('ind_mutu__nama', 'tanggal_isi', 'numerator', 'denominator')
            tahun = tanggal.year
            bulan = tanggal.strftime("%B")
            
            df = pd.DataFrame(datamutu)
            
            if df.empty:
                displaydatamutu = None
            else:
                #Membuat kolom mutu
                df['Mutu'] = (df['numerator']/df['denominator'])*100
                # print('ini ditambah mutu',df)
                #Mengambil tanggal dalam Format tanggal
                df['date'] = pd.to_datetime(df['tanggal_isi'])
                df['Bulan'] = df['date'].dt.strftime('%B')
                
                # pivot_table = df['numerator'] / df.groupby('')['sales'].transform('sum')
                df.rename(columns={'ind_mutu__nama':'Indikator Mutu', 'numerator':'Numerator', 'denominator':'Denominator'}, inplace=True)
                
                percent = df.groupby(['Indikator Mutu', 'Bulan']).agg({'Numerator': 'sum', 'Denominator':'sum', })
                percent_tahun = df.groupby(['Indikator Mutu']).agg({'Numerator': 'sum', 'Denominator':'sum', })
                # percent_tahun['Pertahun(%)'] = ((percent_tahun['Numerator']/percent_tahun['Denominator'])*100).round(decimals=2)
                percent_tahun['Pertahun(%)'] = percent_tahun.apply(div('Numerator', 'Denominator'), axis=1).round(decimals=2)
                percent_tahun.drop(['Numerator','Denominator'], axis=1, inplace=True)
                # df['total'] = df.agg({'numerator': 'sum', 'denominator':'sum'})
                # percent['Prosentase'] = ((percent['Numerator']/percent['Denominator'])*100).round(decimals=2)
                percent['Prosentase'] = percent.apply(div('Numerator', 'Denominator'), axis=1).round(decimals=2)
                
                num_denom = (percent['Numerator'].sum())+(percent['Denominator'].sum())
                # print(num_denom)
                if num_denom > 0:
                    pivotdata = percent.pivot_table(index='Indikator Mutu', columns='Bulan').drop(['Numerator','Denominator'], axis=1)
                    # mergedata = pd.merge(pivotdata, percent_tahun, on='Indikator Mutu')
                    mutudata = pd.concat([pivotdata, percent_tahun], axis=1)
                    displaydatamutu = mutudata.to_html(classes='table', table_id="kematian")
                else:
                    pivotdata = percent.pivot_table(index='Indikator Mutu', columns='Bulan')
                    displaydatamutu = pivotdata.to_html(classes='table', table_id="kematian")

        context = {
            'dep': dep,
            'bidang': bidang,
            'bangsal':bangsal,
            'bangsal1':'IGD',
            'data': displaydatamutu,
            'indikator': indikator,
            'tanggal': tanggal,
            'tahun': tahun,
            'form': form,
            'charttype':chart_type,
            'munas': 'active'
        }
        
        return render(request, self.template, context)
    

class GrafikPerInstalasi(LoginRequiredMixin, View):
    template='chart_instalasi.html'
    model = DataIndikatorMutu
    
    def get(self, request, *args, **kwargs):
        get_ind_mutu = request.GET.get('indikator')
        kwargs_tanggal = kwargs['tanggal_isi']
        get_tanggal = request.GET.get('tanggal')
        chart_type = kwargs['charttype']
        indikator = None
       
        df = None
        displaydatamutu = None
        # Menentukan tanggal/bulan
        tanggal = date.today()
        if get_tanggal:
            tanggal = datetime.strptime(get_tanggal, "%Y-%m-%d").date()
        elif kwargs_tanggal:
            tanggal = datetime.strptime(kwargs_tanggal, "%Y-%m-%d").date()
            
        linechart = 'line'
        barchart='bar'
        
        allindikator = IndikatorMutu.objects.using('auth_db').all()
        
        if get_ind_mutu:
            indikator = get_object_or_404(IndikatorMutu, id=get_ind_mutu)
            datamutu = self.model.objects.using('auth_db').filter(ind_mutu__id = indikator.id, tanggal_isi__month=tanggal.month, tanggal_isi__year=tanggal.year).values('bangsal__nama', 'tanggal_isi', 'numerator', 'denominator')

            df = pd.DataFrame(datamutu)
            
            if df.empty:
                chart = None
            else:
                #Membuat kolom mutu
                df['Mutu'] = (df['numerator']/df['denominator'])*100
                #Mengambil tanggal dalam Format tanggal
                df['date'] = pd.to_datetime(df['tanggal_isi'])
                df['Tanggal'] = df['date'].dt.strftime('%d')
                
                # pivot_table = df['numerator'] / df.groupby('')['sales'].transform('sum')
                percent_perbulan = df.groupby(['bangsal__nama']).agg({'numerator': 'sum', 'denominator':'sum'})
                # percent_perbulan['total_persen'] = ((percent_perbulan['numerator']/percent_perbulan['denominator'])*100).round(decimals=2)
                percent_perbulan['total_persen'] = percent_perbulan.apply(div('numerator', 'denominator'), axis=1)
                percent_perbulan.drop(['numerator','denominator'], axis=1, inplace=True)
                chart = get_chart_instalasi(chart_type, percent_perbulan)
        
        else:
            datamutu = self.model.objects.using('auth_db').filter(tanggal_isi__month=tanggal.month, tanggal_isi__year=tanggal.year).values('bangsal__nama', 'tanggal_isi', 'numerator', 'denominator')
            
            linechart = 'line'
            barchart='bar'
            
            df = pd.DataFrame(datamutu)
            
            if df.empty:
                chart = None
            else:
                #Membuat kolom mutu
                df['Mutu'] = (df['numerator']/df['denominator'])*100
                #Mengambil tanggal dalam Format tanggal
                df['date'] = pd.to_datetime(df['tanggal_isi'])
                df['Tanggal'] = df['date'].dt.strftime('%d')
                
                # pivot_table = df['numerator'] / df.groupby('')['sales'].transform('sum')
                percent_perbulan = df.groupby(['bangsal__nama']).agg({'numerator': 'sum', 'denominator':'sum'})
                # percent_perbulan['total_persen'] = ((percent_perbulan['numerator']/percent_perbulan['denominator'])*100).round(decimals=2)
                percent_perbulan['total_persen'] = percent_perbulan.apply(div('numerator', 'denominator'), axis=1)
                percent_perbulan.drop(['numerator','denominator'], axis=1, inplace=True)
                chart = get_chart_instalasi(chart_type, percent_perbulan)
            
        context = {
            'indikator':indikator,
            'allindikator':allindikator,
            'chart':chart,
            'tanggal':tanggal,
            'bulan': tanggal.strftime('%B %Y'),
            'charttype':chart_type,
            'linechart':linechart,
            'barchart':barchart,
            'munas': 'active'
        }
        return render(request, self.template, context)


class GrafikPerIndikatorMutu(LoginRequiredMixin, View):
    template='chart.html'
    model = DataIndikatorMutu
    
    def get(self, request, *args, **kwargs):
        unit = request.GET.get('bangsal')
        get_tanggal = kwargs['tanggal_isi']
        get_bangsal = request.GET.get('bangsal')
        chart_type = kwargs['charttype']
        bidang = None
        detail_bangsal = Bangsal.objects.using('auth_db').filter(id=unit).first()
        df = None
        displaydatamutu = None
        
        tanggal = date.today()
        
        linechart = 'line'
        barchart='bar'
        # print('ini bangsal: ',detail_bangsal)
        
        if get_tanggal:
            tanggal = datetime.strptime(get_tanggal, "%Y-%m-%d").date()
        
        if get_bangsal:
            bangsal = Bangsal.objects.using('auth_db').get(id=get_bangsal)
            
        allbangsal = Bangsal.objects.using('auth_db').all()
            
        if unit is not None:
            datamutu = self.model.objects.using('auth_db').filter(bangsal__id=bangsal.id, tanggal_isi__month=tanggal.month, tanggal_isi__year=tanggal.year).values('ind_mutu__nama', 'tanggal_isi', 'numerator', 'denominator')
            df = pd.DataFrame(datamutu)
            # print('ini df: ',df)
            if df.empty:
                displaydatamutu = None
            else:
                #Membuat kolom mutu
                df['Mutu'] = (df['numerator']/df['denominator'])*100
                #Mengambil tanggal dalam Format tanggal
                df['date'] = pd.to_datetime(df['tanggal_isi'])
                df['Tanggal'] = df['date'].dt.strftime('%d')

                percent_perbulan = df.groupby(['ind_mutu__nama']).agg({'numerator': 'sum', 'denominator':'sum'})
                # percent_perbulan['total_persen'] = ((percent_perbulan['numerator']/percent_perbulan['denominator'])*100).round(decimals=2)
                percent_perbulan['total_persen'] = percent_perbulan.apply(div('numerator', 'denominator'), axis=1)
                #Menggabungkan kolom numerator dengan denominator
                
                chart = get_chart(chart_type, percent_perbulan)
        else:
            datamutu = self.model.objects.using('auth_db').filter(tanggal_isi__month=tanggal.month, tanggal_isi__year=tanggal.year).values('ind_mutu__nama', 'tanggal_isi', 'numerator', 'denominator')
                
            df = pd.DataFrame(datamutu)
            # print('ini df: ',df)
            if df.empty:
                displaydatamutu = None
            else:
                #Membuat kolom mutu
                df['Mutu'] = (df['numerator']/df['denominator'])*100
                #Mengambil tanggal dalam Format tanggal
                df['date'] = pd.to_datetime(df['tanggal_isi'])
                df['Tanggal'] = df['date'].dt.strftime('%d')

                percent_perbulan = df.groupby(['ind_mutu__nama']).agg({'numerator': 'sum', 'denominator':'sum'})
                # percent_perbulan['total_persen'] = ((percent_perbulan['numerator']/percent_perbulan['denominator'])*100).round(decimals=2)
                percent_perbulan['total_persen'] = percent_perbulan.apply(div('numerator', 'denominator'), axis=1)
                #Menggabungkan kolom numerator dengan denominator
                
                chart = get_chart(chart_type, percent_perbulan)
            
        context = {
            'chart':chart,
            'allbangsal':allbangsal,
            'tanggal':get_tanggal,
            'bangsal':get_bangsal,
            'detail_bangsal':detail_bangsal,
            'charttype':chart_type,
            'linechart':linechart,
            'barchart':barchart,
            'munas': 'active'
        }
        return render(request, self.template, context)
    
    
class GrafikHarienSeries(LoginRequiredMixin, View):
    model = DataIndikatorMutu
    form_class = DataIndikatorMutuForm
    template = 'chart_series.html'
    
    def get(self, request, *args, **kwargs):
        bangsal = None
        df = None
        detail_bangsal = None
        
        tanggal = date.today()
        get_tanggal = request.GET.get('tanggal')
        kwargs_tanggal = kwargs['tanggal_isi']
        set_indikator = request.GET.get('setindikator')
        get_bangsal = request.GET.get('bangsal')
        chart_type = 'line'
        linechart = 'line'
        barchart = 'bar'
        
        allbangsal = Bangsal.objects.using('auth_db').all()
        
        if get_tanggal:
            tanggal = datetime.strptime(get_tanggal, "%Y-%m-%d").date()
        else:
            tanggal = datetime.strptime(kwargs_tanggal, "%Y-%m-%d").date()
            
        # indikator = IndikatorMutu.objects.using('auth_db').all()
        
        if get_bangsal:
            # bidang = Bidang.objects.using('auth_db').get(bidang_bangsal__id=get_bangsal)
            bangsal = Bangsal.objects.using('auth_db').get(id=get_bangsal)
            # dep = Departement.objects.using('auth_db').filter(departement_bidang__bidang_bangsal__id=get_bangsal).first()
            detail_bangsal = Bangsal.objects.using('auth_db').filter(id=get_bangsal).first()

        # get_number = Func(F('numerator')/F('denominator'), function='ROUND')
        if get_bangsal:
            datamutu = self.model.objects.using('auth_db').filter(bangsal__id=bangsal.id, tanggal_isi__month=tanggal.month, tanggal_isi__year=tanggal.year).values('ind_mutu__nama', 'tanggal_isi', 'numerator', 'denominator')
            
            df = pd.DataFrame(datamutu)
            # print('ini df: ',df)
            if df.empty:
                chart = None
            else:
                #Membuat kolom mutu
               
                #Mengambil tanggal dalam Format tanggal
                df['date'] = pd.to_datetime(df['tanggal_isi'])
                df['Tanggal'] = df['date'].dt.strftime('%d')
                
                # pivot_table = df['numerator'] / df.groupby('')['sales'].transform('sum')
                percent_hari_indikator = df.groupby(['ind_mutu__nama', 'Tanggal']).agg({'numerator': 'sum', 'denominator':'sum'})
                # percent_hari_indikator.loc[(percent_hari_indikator['denominator'] != 0) | (percent_hari_indikator['denominator'] != None), 'total_hari'] = ((percent_hari_indikator['numerator']/percent_hari_indikator['denominator'])*100).round(decimals=2)
                percent_hari_indikator['total_hari'] = percent_hari_indikator.apply(div('numerator', 'denominator'), axis=1)
                percent_hari_indikator.drop(['numerator', 'denominator'], axis=1, inplace=True)
                percent_hari_indikator.rename({'ind_mutu__nama':'Indikator Mutu'}, inplace=True)
                #####
                percent_hari = df.groupby(['Tanggal']).agg({'numerator': 'sum', 'denominator':'sum'})
                # percent_hari.loc[(percent_hari['denominator'] != 0) | (percent_hari['denominator'] != None), 'total_hari'] = ((percent_hari['numerator']/percent_hari['denominator'])*100).round(decimals=2)
                percent_hari['total_hari'] = percent_hari.apply(div('numerator', 'denominator'), axis=1)
                percent_hari.drop(['numerator','denominator'], axis=1, inplace=True)
                # print(percent_hari)
                percent_hari_pivot = percent_hari_indikator.pivot_table(index='Tanggal', columns='ind_mutu__nama', fill_value=0)
                
                if set_indikator:
                    chart = get_chart_series(chart_type, percent_hari_pivot, set_indikator)
                else:
                    chart = get_chart_series(chart_type, percent_hari, set_indikator)       
            
        else:
            datamutu = self.model.objects.using('auth_db').filter(tanggal_isi__month=tanggal.month, tanggal_isi__year=tanggal.year).values('ind_mutu__nama', 'tanggal_isi', 'numerator', 'denominator')
            bulans = Bulan.objects.using('auth_db').all()
            tahun = tanggal.year
            bulan = tanggal.strftime("%B")
            
            df = pd.DataFrame(datamutu)
            if df.empty:
                displaydatamutu = None
            else:
                #Membuat kolom mutu
                df['Mutu'] = (df['numerator']/df['denominator'])*100
                #Mengambil tanggal dalam Format tanggal
                df['date'] = pd.to_datetime(df['tanggal_isi'])
                df['Tanggal'] = df['date'].dt.strftime('%d')
                
                # pivot_table = df['numerator'] / df.groupby('')['sales'].transform('sum')
                percent_hari_indikator = df.groupby(['ind_mutu__nama', 'Tanggal']).agg({'numerator': 'sum', 'denominator':'sum'})
                # percent_hari_indikator['total_hari'] = ((percent_hari_indikator['numerator']/percent_hari_indikator['denominator'])*100).round(decimals=2)
                percent_hari_indikator['total_hari'] = percent_hari_indikator.apply(div('numerator', 'denominator'), axis=1)
                percent_hari_indikator.drop(['numerator', 'denominator'], axis=1, inplace=True)
                percent_hari_indikator.rename({'ind_mutu__nama':'Indikator Mutu'}, inplace=True)
                #####
                percent_hari = df.groupby(['Tanggal']).agg({'numerator': 'sum', 'denominator':'sum'})
                # percent_hari['total_hari'] = ((percent_hari['numerator']/percent_hari['denominator'])*100).round(decimals=2)
                percent_hari['total_hari'] = percent_hari.apply(div('numerator', 'denominator'), axis=1)
                percent_hari.drop(['numerator','denominator'], axis=1, inplace=True)
                
                percent_hari_pivot = percent_hari_indikator.pivot_table(index='Tanggal', columns='ind_mutu__nama', fill_value=0)
                # print(percent_hari_pivot)
                if set_indikator:
                    chart = get_chart_series(chart_type, percent_hari_pivot, set_indikator)
                else:
                    chart = get_chart_series(chart_type, percent_hari, set_indikator)

        context = {
            'set_indikator': set_indikator,
            'chart':chart,
            'detail_bangsal':detail_bangsal,
            'allbangsal':allbangsal,
            'tanggal':get_tanggal or kwargs_tanggal,
            'bangsal':get_bangsal,
            'tahun':tanggal.strftime('%B %Y'),
            'charttype':chart_type,
            'linechart':linechart,
            'barchart':barchart,
            'munas': 'active'
        }
        
        return render(request, self.template, context)


class GrafikBulananSeries(LoginRequiredMixin, View):
    model = DataIndikatorMutu
    form_class = DataIndikatorMutuForm
    template = 'chart_series_perbulan.html'
    
    def get(self, request, *args, **kwargs):
        bangsal = None
        df = None
        detail_bangsal = None
        
        tanggal = date.today()
        get_tanggal = request.GET.get('tanggal')
        kwargs_tanggal = kwargs['tanggal_isi']
        set_indikator = request.GET.get('setindikator')
        get_bangsal = request.GET.get('bangsal')
        chart_type = 'line'
        linechart = 'line'
        barchart = 'bar'
        
        allbangsal = Bangsal.objects.using('auth_db').all()
        
        if get_tanggal:
            tanggal = datetime.strptime(get_tanggal, "%Y-%m-%d").date()
        elif kwargs_tanggal:
            tanggal = datetime.strptime(kwargs_tanggal, "%Y-%m-%d").date()
            
        # indikator = IndikatorMutu.objects.using('auth_db').all()
        
        if get_bangsal:
            # bidang = Bidang.objects.using('auth_db').get(bidang_bangsal__id=get_bangsal)
            bangsal = Bangsal.objects.using('auth_db').get(id=get_bangsal)
            # dep = Departement.objects.using('auth_db').filter(departement_bidang__bidang_bangsal__id=get_bangsal).first()
            detail_bangsal = Bangsal.objects.using('auth_db').filter(id=get_bangsal).first()

        # get_number = Func(F('numerator')/F('denominator'), function='ROUND')
        if get_bangsal:
            datamutu = self.model.objects.using('auth_db').filter(bangsal__id=bangsal.id, tanggal_isi__year=tanggal.year).values('ind_mutu__nama', 'tanggal_isi', 'numerator', 'denominator')
            
            df = pd.DataFrame(datamutu)
            # print('ini df: ',df)
            if df.empty:
                chart = None
            else:
                #Membuat kolom mutu
               
                #Mengambil bulan dalam Format tanggal
                df['date'] = pd.to_datetime(df['tanggal_isi'])
                df['Bulan'] = df['date'].dt.strftime('%m')
                
                # pivot_table = df['numerator'] / df.groupby('')['sales'].transform('sum')
                percent_bulan_indikator = df.groupby(['ind_mutu__nama', 'Bulan']).agg({'numerator': 'sum', 'denominator':'sum'})
                # percent_hari_indikator.loc[(percent_hari_indikator['denominator'] != 0) | (percent_hari_indikator['denominator'] != None), 'total_hari'] = ((percent_hari_indikator['numerator']/percent_hari_indikator['denominator'])*100).round(decimals=2)
                percent_bulan_indikator['total_hari'] = percent_bulan_indikator.apply(div('numerator', 'denominator'), axis=1)
                percent_bulan_indikator.drop(['numerator', 'denominator'], axis=1, inplace=True)
                percent_bulan_indikator.rename({'ind_mutu__nama':'Indikator Mutu'}, inplace=True)
                #####
                percent_bulan = df.groupby(['Bulan']).agg({'numerator': 'sum', 'denominator':'sum'})
                # percent_hari.loc[(percent_hari['denominator'] != 0) | (percent_hari['denominator'] != None), 'total_hari'] = ((percent_hari['numerator']/percent_hari['denominator'])*100).round(decimals=2)
                percent_bulan['total_hari'] = percent_bulan.apply(div('numerator', 'denominator'), axis=1)
                percent_bulan.drop(['numerator','denominator'], axis=1, inplace=True)
                # print(percent_hari)
                percent_bulan_pivot = percent_bulan_indikator.pivot_table(index='Bulan', columns='ind_mutu__nama', fill_value=0)
                
                if set_indikator:
                    chart = get_chart_series_bulan(chart_type, percent_bulan_pivot, set_indikator)
                else:
                    chart = get_chart_series_bulan(chart_type, percent_bulan, set_indikator)       
            
        else:
            datamutu = self.model.objects.using('auth_db').filter(tanggal_isi__year=tanggal.year).values('ind_mutu__nama', 'tanggal_isi', 'numerator', 'denominator')
            # bulans = Bulan.objects.using('auth_db').all()
            # tahun = tanggal.year
            # bulan = tanggal.strftime("%B")
            
            df = pd.DataFrame(datamutu)
            if df.empty:
                displaydatamutu = None
            else:
                #Membuat kolom mutu
                df['date'] = pd.to_datetime(df['tanggal_isi'])
                df['Bulan'] = df['date'].dt.strftime('%m')
                
                # pivot_table = df['numerator'] / df.groupby('')['sales'].transform('sum')
                percent_bulan_indikator = df.groupby(['ind_mutu__nama', 'Bulan']).agg({'numerator': 'sum', 'denominator':'sum'})
                # percent_hari_indikator.loc[(percent_hari_indikator['denominator'] != 0) | (percent_hari_indikator['denominator'] != None), 'total_hari'] = ((percent_hari_indikator['numerator']/percent_hari_indikator['denominator'])*100).round(decimals=2)
                percent_bulan_indikator['total_hari'] = percent_bulan_indikator.apply(div('numerator', 'denominator'), axis=1)
                percent_bulan_indikator.drop(['numerator', 'denominator'], axis=1, inplace=True)
                percent_bulan_indikator.rename({'ind_mutu__nama':'Indikator Mutu'}, inplace=True)
                #####
                percent_bulan = df.groupby(['Bulan']).agg({'numerator': 'sum', 'denominator':'sum'})
                # percent_hari.loc[(percent_hari['denominator'] != 0) | (percent_hari['denominator'] != None), 'total_hari'] = ((percent_hari['numerator']/percent_hari['denominator'])*100).round(decimals=2)
                percent_bulan['total_hari'] = percent_bulan.apply(div('numerator', 'denominator'), axis=1)
                percent_bulan.drop(['numerator','denominator'], axis=1, inplace=True)
                # print(percent_hari)
                percent_bulan_pivot = percent_bulan_indikator.pivot_table(index='Bulan', columns='ind_mutu__nama', fill_value=0)
                
                if set_indikator:
                    chart = get_chart_series_bulan(chart_type, percent_bulan_pivot, set_indikator)
                else:
                    chart = get_chart_series_bulan(chart_type, percent_bulan, set_indikator)       
        context = {
            'set_indikator': set_indikator,
            'chart':chart,
            'detail_bangsal':detail_bangsal,
            'allbangsal':allbangsal,
            'tanggal':tanggal,
            'bangsal':get_bangsal,
            'tahun':tanggal.strftime('%Y'),
            'charttype':chart_type,
            'linechart':linechart,
            'barchart':barchart,
            'munas': 'active'
        }
        
        return render(request, self.template, context)
