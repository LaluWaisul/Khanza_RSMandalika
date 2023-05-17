from django import forms
from ralan.models import RegPeriksa
from .models import PenilaianAwalKeperawatanIgd


class SearchForm(forms.Form): 
    data = forms.CharField(label='')


class PengkajianKeperawatanForm(forms.ModelForm):
    class Meta:
        model=PenilaianAwalKeperawatanIgd
        fields = "__all__"
     
    def __init__(self, *args, **kwargs):
        super(PengkajianKeperawatanForm, self).__init__(*args, **kwargs)
        self.fields['tanggal'].widget = forms.TextInput(attrs={'type':'date'})
        self.fields['rpd'].label = 'Riwayat Penyakit Dahulu'
        self.fields['keluhan_utama'].widget.attrs['style'] = 'height:80px'
        self.fields['rpd'].widget.attrs['style'] = 'height:100px'
        self.fields['rpo'].label = 'Riwayat Penggunaan Obat'
        self.fields['rpo'].widget.attrs['style'] = 'height:100px'
        self.fields['jumlah_perdarahan'].help_text = 'Jumlah dalam satuan ml/cc'
        self.fields['bab'].label = 'BAB'
        self.fields['xbab'].label = 'Frek BAB'
        self.fields['kbab'].label = 'Konsist BAB'
        self.fields['wbab'].label = 'Warna BAB'
        self.fields['bak'].label = 'BAK'
        self.fields['xbak'].label = 'Frek BAK'
        self.fields['wbak'].label = 'Warna BAK'
        self.fields['lbak'].label = 'Lain-lain'
        self.fields['sebutkan'].label='Lainnya, sebutkan'
        self.fields['dilaporkan'].label='Jika ada, dilaporkan kemana'
        self.fields['ket_tinggal'].label='Jika dengan lainnya, sebutkan'
    