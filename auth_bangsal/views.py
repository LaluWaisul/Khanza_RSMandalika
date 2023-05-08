from distutils import dep_util
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.http import HttpResponseRedirect

from .forms import BangsalForm, BidangForm, DepartementForm

from .models import Departement, Bidang, Bangsal

# Create your views here.

class DepartementView(View):
    def get(self, request, *args, **kwargs):
        
        dep = Departement.objects.using('auth_db').all()
            
        context={
            'dep': dep,
            'sub1': 'active',
            'unit': 'active'
        }
        return render(request, 'departemen.html', context)
    
    
class BidangView(View):
    def get(self, request):
        bidang = Bidang.objects.using('auth_db').all()
            
        context={
            'bidang': bidang,
            'sub2': 'active',
            'unit': 'active'
        }
        return render(request, 'bidang.html', context)
    

class BangsalView(View):
    model = Bangsal
    form_class = BangsalForm
    template = 'formdata.html'    
    
    def get(self, request, id=None):
        
        bangsal = Bangsal.objects.using('auth_db').all()
        
        context={
            'bangsal': bangsal,
            'sub3': 'active',
            'unit': 'active'
        }
        return render(request, 'bangsal.html', context)
    
    # def post(self)
    

class TambahDataDepartementView(View):
    model = Departement
    form_class = DepartementForm
    template = 'formdata.html'
    
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
            'form':form
        }
        return render(request, self.template, context)
    
    def post(self, request, id=None):
        postdata = request.POST
        obj = self.get_object()
        form = self.form_class(postdata, instance=obj)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth_bangsal:departement_view'))
        
        context={
            'form':form
        }
        return render(request, self.template, context)
    
    
class TambahDataBidangView(View):
    model = Bidang
    form_class = BidangForm
    template = 'formdata.html'
    
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
            'form':form
        }
        return render(request, self.template, context)
    
    def post(self, request, id=None):
        postdata = request.POST
        obj = self.get_object()
        form = self.form_class(postdata, instance=obj)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth_bangsal:bidang_view'))
        
        context={
            'form':form
        }
        return render(request, self.template, context)
    
    
class TambahDataBangsalView(View):
    model = Bangsal
    form_class = BangsalForm
    template = 'formdata.html'
    
    def get_object(self):
        id = self.kwargs.get('kd')
        # print('ini id: ',id)
        if id is not None:
            obj=get_object_or_404(self.model, kd_bangsal=id)
            return obj
        return None
    
    def get(self, request, kd=None):
        obj = self.get_object()
        form = self.form_class()
        # print(obj)
        if obj is not None:
            form = self.form_class(instance=obj)
        context={
            'form':form
        }
        return render(request, self.template, context)
    
    def post(self, request, kd=None):
        postdata = request.POST
        obj = self.get_object()
        form = self.form_class(postdata, instance=obj)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth_bangsal:bangsal_view'))
        
        context={
            'form':form
        }
        return render(request, self.template, context)
    