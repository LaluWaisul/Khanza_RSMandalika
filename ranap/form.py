from django import forms

class form_serach(forms.Form) :
    data = forms.CharField(label='')

class formPemberianObat(forms.Form) :
    no_rawat        = forms.CharField(label='No. Rawat')
    no_RM           = forms.CharField(label='Nomor RM')
    Nama_Pasien     = forms.CharField()
    Tahun = range(2018,2100,1)
    Tgl_pemberian   = forms.DateField(
        widget= forms.SelectDateWidget(years=Tahun)
    )
    waktu           = forms.TimeField()
    kode_obat       = forms.CharField()
    nama_obat       = forms.CharField()

class formUpdataPerawatan(forms.Form) :
    kode_dokter     = forms.CharField()
    nama_dokter     = forms.CharField()
    kode_perawa     = forms.CharField()
    nama_perawa     = forms.CharField()
    kode_tidakan    = forms.CharField()
    nama_tidakan    = forms.CharField()

class formPenanganan(forms.Form) :
    subjek          = forms.CharField(
        widget=forms.Textarea,
    )
    objek           = forms.CharField(
        widget=forms.Textarea,
    )
    suhu            = forms.IntegerField()
    tensi           = forms.IntegerField()
    tinggi_badan    = forms.IntegerField()
    respirasi       = forms.IntegerField()
    berat_badan     = forms.IntegerField()
    nadi            = forms.IntegerField()
    gcs =(
        ('E', 'E'),
        ('V', 'V'),
        ('M', 'M'),
    )
    nilaiGCS        = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=gcs,
        label='GCS'
        )
    alergi          = forms.CharField()
    asesmen         = forms.CharField()
    plan            = forms.CharField()
    Kesadaran = (
        ('','')
    )
    status_kesadaran= forms.ChoiceField(choices=Kesadaran, label='Kesadaran')
