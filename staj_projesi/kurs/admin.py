from django.contrib import admin
from .models import *
# Register your models here.


class KursAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)

admin.site.register(Kurs,KursAdmin)

admin.site.register(kategori)