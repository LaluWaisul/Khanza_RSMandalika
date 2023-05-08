from django import forms
from .models import FileAkreditasi, KategoriElementPenilaian, PokjaAkreditasi, StandarAkreditasi, ElementPenilaian


class PokjaForm(forms.ModelForm):
    class Meta:
        model = PokjaAkreditasi
        fields = ('nama', )
        
        
class StandarForm(forms.ModelForm):
    pokja = forms.ModelChoiceField(queryset=PokjaAkreditasi.objects.exclude(nama='admin'))
    class Meta:
        model = StandarAkreditasi
        fields = ('pokja', 'nama', )
    
    def __init__(self, *args, **kwargs):
        super(StandarForm, self).__init__(*args, **kwargs)
        # clean_data.__init__(*args, **kwargs)
        self.fields['pokja'].help_text = 'Silahkan pilih kelompok kerja yang akan ditambahkan'


class ElementPenilaianForm(forms.ModelForm):
    class Meta:
        model = ElementPenilaian
        fields = ('standar', 'nama' )
    

class KategoriElementPenilaianForm(forms.ModelForm):
    class Meta:
        model = KategoriElementPenilaian
        fields = ('element', 'nama', 'metode', 'skor', 'jlh_kat_skor', 'sasaran', 'tahun')
        
    def __init__(self, *args, **kwargs):
        super(KategoriElementPenilaianForm, self).__init__(*args, **kwargs)
        # clean_data.__init__(*args, **kwargs)
        self.fields['nama'].label = 'Subelement Penilaian'
        self.fields['metode'].widget = forms.Select(choices=[
            ('','-- Pilih Metode Penilaian --'),
            ('Penetapan Kebijakan (PK)','Penetapan Kebijakan (PK)'),
            ('Penjelasan Petugas (PP)','Penjelasan Petugas (PP)'),
            ('Peragaan Contoh (PC)','Peragaan Contoh (PC)'),
            ('Pengamatan Lapangan (PL)','Pengamatan Lapangan (PL)'),
            ('Penggalian Informasi (PI)','Penggalian Informasi (PI)')
            ],  attrs={'class': "form-control"})
        self.fields['tahun'].widget = forms.TextInput(attrs={'type':'date'})
        self.fields['tahun'].help_text = 'Abaikan tanggal dan bulan'
        self.fields['tahun'].required = True
        self.fields['jlh_kat_skor'].help_text = '<b>Ketik 3</b> untuk 3 pilihan skor, dan <b>ketik 2</b> untuk 2 pilihan skor'
        if kwargs:
            if kwargs['instance'].jlh_kat_skor == '3':
                self.fields['skor'].widget = forms.RadioSelect(choices=[(10, '10'), (5, '5'), (0, '0')],  attrs={'class': "form-control"})
            elif kwargs['instance'].jlh_kat_skor == '2':
                self.fields['skor'].widget = forms.RadioSelect(choices=[(10, '10'), (0, '0')],  attrs={'class': "form-control"})
            else:
                self.fields['skor'].widget = forms.TextInput(attrs={'type':'hidden'})
        else:
            if self.fields['jlh_kat_skor'].initial == '3':
                self.fields['skor'].widget = forms.RadioSelect(choices=[(10, '10'), (5, '5'), (0, '0')],  attrs={'class': "form-control"})
                
                        
class FileForm(forms.ModelForm):
    class Meta:
        model = FileAkreditasi
        fields = ('kategori', 'file', 'status')
        
    def __init__(self, *args, **kwargs):
        super(FileForm, self).__init__(*args, **kwargs)
        # clean_data.__init__(*args, **kwargs)
        self.fields['status'].widget = forms.RadioSelect(choices=[('Belum Dikerjakan', 'Belum Dikerjakan'), ('Proses', 'Proses'), ('Selesai', 'Selesai')],  attrs={'class': "form-control"})
        
        
    
