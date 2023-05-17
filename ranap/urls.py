from django.urls import path
from .views import ListPasien, TindakanRanap


urlpatterns = [
    path('pasienranap/', ListPasien.as_view(), name='listpasien'),
    path('tindakan/', TindakanRanap.as_view(), name='tindakan'),
]
 