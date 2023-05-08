from django.urls import path
from .views import GrafikBulananSeries, GrafikPerInstalasi, TambahDataMutuView, dashboard, GrafikPerIndikatorMutu, CapaianMutuPerBulan, GrafikHarienSeries, CapaianMutuHari
# from auth_mutu.views import Grafik


urlpatterns = [
    path('dashboard/', dashboard, name='dashboard_view'),
    path('mutu-nasional/', CapaianMutuHari.as_view(), name='data-mutu'),
    path('mutu-nasional-tahun/', CapaianMutuPerBulan.as_view(), name='data-mutu-tahun'),
    # path('tambah-data-mutu/<str:tanggal_isi>/<str:bangsal>/', TambahDataMutuView.as_view(), name='tambah_datamutu'),
    path('tambah-data-mutu/<str:tanggal_isi>/', TambahDataMutuView.as_view(), name='tambah_datamutu'),
    path('chart-indikator/<str:charttype>/<str:tanggal_isi>/', GrafikPerIndikatorMutu.as_view(), name='chart_view'),
    path('chart-instalasi/<str:charttype>/<str:tanggal_isi>/', GrafikPerInstalasi.as_view(), name='chart_instalasi_view'),
    path('chart-series-perhari/<str:charttype>/<str:tanggal_isi>/', GrafikHarienSeries.as_view(), name='chart_series_perhari_view'),
    path('chart-series-perbulan/<str:charttype>/<str:tanggal_isi>/', GrafikBulananSeries.as_view(), name='chart_series_perbulan_view'),
]
