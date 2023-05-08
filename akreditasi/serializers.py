from pandas import NamedAgg
from rest_framework import serializers
from .models import ElementPenilaian, KategoriElementPenilaian, FileAkreditasi, StandarAkreditasi


class StandarAkreditasiSerializerChild(serializers.ModelSerializer):
    class Meta:
        model = StandarAkreditasi
        fields = ('pokja', 'nama')
        depth=1
        

class ElementPenilaianSerializerChild(serializers.ModelSerializer):
    standar = StandarAkreditasiSerializerChild()
    class Meta:
        model = ElementPenilaian
        fields = ('standar', 'nama')

class KategoriElementPenilaianSerializerChild(serializers.ModelSerializer):
    element = ElementPenilaianSerializerChild()
    class Meta:
        model = KategoriElementPenilaian
        fields = ('id', 'element', 'nama', 'tahun')
        

class AkreditasiFileSerializer(serializers.ModelSerializer):
    kategori = KategoriElementPenilaianSerializerChild()
    class Meta:
        model = FileAkreditasi
        fields = ('id', 'kategori', 'nama', 'status', 'file')
        
        
class KategoriEPSerializer(serializers.ModelSerializer):
    class Meta:
        model = KategoriElementPenilaian
        fields = '__all__'
        depth = 1
        
class KategoriElementPenilaianSerializer(serializers.ModelSerializer):
    # fileakreditasi_set = serializers.StringRelatedField(many=True)
    fileakreditasi_set = serializers.HyperlinkedRelatedField(view_name='akreditasiurls:file_api_view', many=True, read_only=True)
    class Meta:
        model = KategoriElementPenilaian
        fields = ('id', 'element', 'nama', 'metode', 'skor', 'skor_max', 'sasaran', 'tahun', 'fileakreditasi_set')
       
        
class ProsentasePerstandarSerializer(serializers.Serializer):
    element__standar__pokja__nama = serializers.CharField()
    element__standar__nama = serializers.CharField()
    nilaitotal = serializers.FloatField()
    nilai = serializers.FloatField()
    percentage = serializers.FloatField()
    backgroundcolor=serializers.CharField()
    
class ProsentasePerpokjaSerializer(serializers.Serializer):
    element__standar__pokja__nama = serializers.CharField()
    nilaitotal = serializers.FloatField()
    nilai = serializers.FloatField()
    percentage = serializers.FloatField()
    backgroundcolor=serializers.CharField()
    

class ProsentaseAkreditasiSerializer(serializers.Serializer):
    element__standar__pokja__rumah_sakit__nama = serializers.CharField()
    nilaitotal = serializers.FloatField()
    nilai = serializers.FloatField()
    capaian = serializers.FloatField()
    sisa_target = serializers.FloatField()
    
    