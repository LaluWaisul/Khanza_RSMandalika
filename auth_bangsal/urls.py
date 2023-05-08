from django.urls import path

from .views import BangsalView, BidangView, DepartementView, TambahDataBangsalView, TambahDataBidangView, TambahDataDepartementView


urlpatterns = [
    path('departement/', DepartementView.as_view(), name='departement_view'),
    path('bidang/', BidangView.as_view(), name='bidang_view'),
    path('bangsal/', BangsalView.as_view(), name='bangsal_view'),
    # path('bangsal/<int:id>', BangsalView.as_view(), name='detail_bangsalview'),
    path('tambah-dep/', TambahDataDepartementView.as_view(), name='tambah_departementview'),
    path('tambah-bidang/', TambahDataBidangView.as_view(), name='tambah_bidangview'),
    path('tambah-bangsal/', TambahDataBangsalView.as_view(), name='tambah_bangsalview'),
    path('tambah-bangsal/<str:kd>/', TambahDataBangsalView.as_view(), name='detail_bangsalview'),
    path('tambah-bidang/<int:id>/', TambahDataBidangView.as_view(), name='detail_bidangview'),
    path('tambah-dep/<int:id>/', TambahDataDepartementView.as_view(), name='detail_departementview'),
]
