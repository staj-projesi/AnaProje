from django.db import models
from django.utils.text import slugify
# Create your models here.

class Kurs(models.Model):
    baslik = models.CharField(max_length=50)
    acıklama = models.TextField()
    resim = models.ImageField(default='kurs_resimleri')
    tarih = models.DateField()
    aktifKurs = models.BooleanField(default=False)
    fiyat = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(default="",unique=True,db_index=True)
    # max_digits: Bu, ondalık sayının toplam basamak sayısını temsil eder. Örneğin, "123.45" 
    # decimal_places: Bu, ondalık kısmın kaç basamağa sahip olduğunu belirtir. Örneğin, "123.45" gibi bir değer için decimal_places 2 olmalıdır.
    
    def formatli_fiyat(self):
        return '{:,.2f}'.format(self.fiyat)
    formatli_fiyat.short_description = 'Fiyat'
    
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.baslik)
        super().save(args,kwargs)
    
    def __str__(self):
        return self.baslik

class kategori(models.Model):
    isim = models.CharField(max_length=50)
    slug = models.SlugField()