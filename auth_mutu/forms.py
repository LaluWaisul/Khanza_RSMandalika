from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from auth_bangsal.models import Bangsal
from .models import DataIndikatorMutu, IndikatorMutu


class DataIndikatorMutuForm(forms.ModelForm):
    tanggal_isi = forms.DateField(required=False)
    bangsal = forms.ModelChoiceField(queryset=Bangsal.objects.using('auth_db').all(), required=False)
    class Meta:
        model = DataIndikatorMutu
        fields = ('tanggal_isi', 'bangsal')
        
    def __init__(self, *args, **kwargs):
        super(DataIndikatorMutuForm, self).__init__(*args, *kwargs)
        
        self.fields['tanggal_isi'].widget = forms.TextInput(
            attrs={'type': 'date'})
        self.fields['tanggal_isi'].label = ''
        self.fields['bangsal'].label=''

class IndikatorMutuForm(forms.ModelForm):
    class Meta:
        model = IndikatorMutu
        fields = ('nama', )
        
        
class FormMutuNasional(forms.ModelForm):
    # numerator = forms.BooleanField(widget=forms.RadioSelect(choices=[(False, 'Tidak'), (True, 'Iya')],  attrs={'class': "form-control"}))
    # ind_mutu = forms.CharField(widget=forms.TextInput(attrs={'disabled':'disabled', 'hidden':'hidden'}))
    class Meta:
        model = DataIndikatorMutu
        fields = ('numerator', 'denominator')

    def __init__(self, *args, **kwargs):
        indikator = kwargs['instance']
        super().__init__(*args, **kwargs)
        self.fields['numerator'].label = f'{indikator.ind_mutu.nama} - {"Numerator"}'
        self.fields['numerator'].required = False
        self.fields['denominator'].label = f'{indikator.ind_mutu.nama} - {"Denominator"}'
        self.fields['denominator'].required = False
       
        
        

MutuNasionalFormset = forms.modelformset_factory(
    DataIndikatorMutu, FormMutuNasional, extra=0)
