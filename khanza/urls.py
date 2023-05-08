from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static

urlpatterns = [
    path('', include(('myaccount.urls', 'myaccount'), namespace='myaccount')),
    path('admin/', admin.site.urls),
    path('mutu/', include(('auth_mutu.urls', 'auth_mutu'), namespace='auth_mutu')),
    path('departement/', include(('auth_bangsal.urls', 'auth_bangsal'), namespace='auth_bangsal')),
    path('ralan/', include(('ralan.urls', 'ralanurls'), namespace='ralanurls')),
    path('bangsal/', include(('bangsal.urls', 'ranapurl'), namespace='ranapurl')),
    path('pegawai/', include(('pegawai.urls', 'pegawaiurl'), namespace='pegawaiurl')),
    path('ranap/', include(('ranap.urls', 'ranap'), namespace='ranap')),
    path('igd/', include(('igd.urls', 'igd'), namespace='igd')),
    
    path('akreditasi/', include(('akreditasi.urls', 'akreditasiurls'), namespace='akreditasiurls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)