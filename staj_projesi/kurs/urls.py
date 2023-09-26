from django.urls import path
from .views import *


urlpatterns = [
    path('',index,name='index'),
    path('<slug:slug>',details,name='details'),
    path('kategori/<int:kategoriId>',dinamikKategoriId,name='kategoriId'),
    path('kategori/<str:kategori>',dinamikKategori,name='kategori'),
]
