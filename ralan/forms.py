from django import forms

from .models import BookingPeriksa, RegPeriksa
from bangsal.models import Poliklinik


class BookingPeriksaForm(forms.ModelForm):
    kd_poli = forms.ModelChoiceField(queryset=Poliklinik.objects.all())
    
    class Meta:
        model = BookingPeriksa
        fields = ('tanggal', 'nama', 'alamat', 'no_telp', 'email', 'kd_poli', 'tambahan_pesan')
        
    def __init__(self, *args, **kwargs):
        super(BookingPeriksaForm, self).__init__(*args, **kwargs)
        self.fields['nama'].label = 'Nama Pasien'
        self.fields['kd_poli'].label = 'Poliklinik Tujuan'
        self.fields['tanggal'].widget = forms.TextInput(attrs={'type':'date'})
        self.fields['tambahan_pesan'].widget = forms.Textarea(attrs={'type':'text'})
        
class RegPeriksaForm(forms.ModelForm):
    class Meta:
        model = RegPeriksa
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super(RegPeriksaForm, self).__init__(*args, **kwargs)
        self.fields['no_reg'].widget = forms.TextInput(attrs={'class':'form-control'})
        self.fields['no_rawat'].widget = forms.TextInput(attrs={'class':'form-control'})
        self.fields['tgl_registrasi'].widget = forms.TextInput(attrs={'type':'date', 'class':'form-control', 'style':'width:30%'})
        self.fields['jam_reg'].widget = forms.TextInput(attrs={'type':'time', 'class':'form-control', 'style':'width:30%'})
        self.fields['kd_dokter'].widget.attrs['class'] = 'form-control'
        self.fields['no_rkm_medis'].widget.attrs['class'] = 'form-control'
        self.fields['no_rkm_medis'].widget.attrs['style'] = 'width:90%'
        self.fields['kd_poli'].widget = forms.TextInput(attrs={'class':'form-control'})
        self.fields['p_jawab'].widget = forms.TextInput(attrs={'class':'form-control'})
        self.fields['almt_pj'].widget = forms.TextInput(attrs={'class':'form-control'})
        self.fields['hubunganpj'].widget = forms.TextInput(attrs={'class':'form-control'})
        self.fields['biaya_reg'].widget = forms.TextInput(attrs={'class':'form-control'})
        self.fields['stts'].widget.attrs['class'] = 'form-control'
        self.fields['stts_daftar'].widget.attrs['class'] = 'form-control'
        self.fields['status_lanjut'].widget = forms.TextInput(attrs={'class':'form-control'})
        self.fields['kd_pj'].widget.attrs['class'] = 'form-control'
        self.fields['umurdaftar'].widget = forms.TextInput(attrs={'class':'form-control'})
        self.fields['sttsumur'].widget = forms.TextInput(attrs={'class':'form-control'})
        self.fields['status_bayar'].widget = forms.TextInput(attrs={'class':'form-control'})
        self.fields['status_poli'].widget = forms.TextInput(attrs={'class':'form-control'})
        
        
        
