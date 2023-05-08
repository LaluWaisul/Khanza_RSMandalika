from django.urls import path
from .views import ListPasien


urlpatterns = [
    path('pasienranap/', ListPasien.as_view(), name='listpasien'),
]
