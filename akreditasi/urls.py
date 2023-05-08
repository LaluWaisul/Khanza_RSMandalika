from django.urls import path

from .views import (
    AkreditasiDashboard, DashboardFileAkreditasi, DownloadAPIView, EditKategoriElementPenilaianView, FileAKreditasiAPIView, KategoriElementPenilaianView, NilaiPerStandarAPIView, NilaiAkreditasiAPIView, EditAkreditasiFileView, PokjaView, SearchAkreditasiFileAPIView, 
    StandarAkreditasiView, TambahAkreditasiFileView, TambahKategoriElementPenilaianView, TambahPokjaView, EditPokjaView, TambahStandarAkreditasiView,
    EditStandarAkreditasiView, ElementAkreditasiFileAPIView, ElementAkreditasiFileView, ElementPenilaianView, EditElementPenilaianView,
    TambahElementPenilaianView, NilaiPerPokjaAPIView, AkreditasiFileView, download,
    delete_kategori_ep, DataAPI
    )


urlpatterns = [
    #### pokja url ####
    path('pokja/', PokjaView.as_view(), name='pokja_akreditasi'),
    path('tambahpokja/', TambahPokjaView.as_view(), name='tambah_pokja'),
    path('editpokja/<int:id>/', EditPokjaView.as_view(), name='edit_pokja'),
    #### standar url ####
    path('pokja/<int:id>/', StandarAkreditasiView.as_view(), name='standar_view'),
    path('tambahstandar/<int:id>/', TambahStandarAkreditasiView.as_view(), name='tambah_standar'),
    path('editstandar/<int:id>/', EditStandarAkreditasiView.as_view(), name='edit_standar'),
    #### element penilaian url ####
    path('standar/<int:id>/', ElementPenilaianView.as_view(), name='element_penilaian_view'),
    path('tambah-element-penilaian/<int:id>/', TambahElementPenilaianView.as_view(), name='tambah_element_penilaian_view'),
    path('edit-element-penilaian/<int:id>/', EditElementPenilaianView.as_view(), name='edit_element_penilaian_view'),
    #### kategori element penilaian ####
    path('element/<int:id>/', KategoriElementPenilaianView.as_view(), name='kat_element_penilaian_view'),
    path('tambah-kat-element-penilaian/<int:id>/', TambahKategoriElementPenilaianView.as_view(), name='tambah_kat_element_penilaian_view'),
    path('edit-kat-element-penilaian/<int:id>/', EditKategoriElementPenilaianView.as_view(), name='edit_kat_element_penilaian_view'),
    path('delete/<int:id>/', delete_kategori_ep, name='delete_ep'),
    #### file url ####
    path('elementfile/<int:id>/', ElementAkreditasiFileView.as_view(), name='element_file_view'),
    path('tambahfile/<int:id>/', TambahAkreditasiFileView.as_view(), name='tambah_file'),
    path('editfile/<int:id>/', EditAkreditasiFileView.as_view(), name='edit_file'),
    path('deletefile/<int:kategori>/<int:id>/', AkreditasiFileView.as_view(), name='delete_file'),
    #### API url ####
    path('apistandarfileakreditasi/<int:id>/', ElementAkreditasiFileAPIView.as_view()),
    path('searchfile/', SearchAkreditasiFileAPIView.as_view()),
    path('dataapi/', DataAPI.as_view()),
    
    #### DASHBOARD
    path('dashboard/', AkreditasiDashboard.as_view(), name='dash_view'),
    path('nilaiakreditasi/', NilaiAkreditasiAPIView.as_view()),
    path('nilaipokja/', NilaiPerPokjaAPIView.as_view()),
    path('apidashboard/', NilaiPerStandarAPIView.as_view(), name='standar_view'),   
    path('fileakreditasi/<int:pk>/', FileAKreditasiAPIView.as_view(), name='file_api_view'),
    path('dashboardfile/', DashboardFileAkreditasi.as_view(), name='dashboard_file_view'),
    
    #### Download file
    path('download/<str:path>/', download, name='download_file'),
    path('downloadfile/<int:id>/', DownloadAPIView.as_view(), name='download_file_class')
]
