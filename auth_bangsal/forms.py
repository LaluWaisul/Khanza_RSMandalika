from django import forms
from .models import Bangsal, Bidang, Departement


class BangsalForm(forms.ModelForm):
    class Meta:
        model = Bangsal
        fields = ('kd_bangsal','bidang', 'nama')
        
        
class BidangForm(forms.ModelForm):
    class Meta:
        model = Bidang
        fields = ('dep', 'nama')
        
        
class DepartementForm(forms.ModelForm):
    class Meta:
        model = Departement
        fields = ('nama', )