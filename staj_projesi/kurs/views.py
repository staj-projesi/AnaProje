from django.http import HttpResponseNotFound
from django.shortcuts import render

# Create your views here.


data = {
    "programlama":"programlama kategorisine ait kurslar",
    "web-gelistirme":"web geliştirme kategorisine ait kurslar",
    "mobil":"mobil kategorisine ait kurslar"
}




def index(req):
    return render(req,'index.html')

def details(req,slug):
    context = {
        'kurs_adi':slug
    }
    return render(req,'details.html',context)




def dinamikKategori(req,kategori):
    try:
        kategoriler = data[kategori]
        context = {
            'kategoriler':kategoriler,
            'kategori':kategori
        }
        return render(req,'dinamik.html',context)
    except:
        return HttpResponseNotFound("yanlış kategori seçimi")



def dinamikKategoriId(req,kategoriId):
    kategori_list=list(data.keys())
    if(kategoriId > len(kategori_list)):
        return HttpResponseNotFound("yanlış kategori seçimi")
    kategori_key = kategori_list[kategoriId - 1]
    
    context={
        'kategori_key':kategori_key,
        'kategoriId':kategoriId
    }
    return render(req,'dinamik.html',context)