from django.contrib import admin
from .models import Kategori, Urun, UrunFoto

class UrunFotoInline(admin.TabularInline):
    model = UrunFoto
    extra = 1  # Admin panelinde başlangıçta kaç boş fotoğraf alanı göstereceğini belirtir

class UrunAdmin(admin.ModelAdmin):
    list_display = ('isim', 'kategori', 'fiyat', 'para_birimi', 'stok_miktari', 'birim')
    search_fields = ('isim', 'kategori__isim')
    list_filter = ('kategori', 'para_birimi')
    inlines = [UrunFotoInline]  # Fotoğrafları eklemek için UrunFotoInline sınıfını burada belirtin

class KategoriAdmin(admin.ModelAdmin):
    list_display = ['isim', 'parent']
    prepopulated_fields = {'slug': ('isim',)}

admin.site.register(Kategori, KategoriAdmin)
admin.site.register(Urun, UrunAdmin)
admin.site.register(UrunFoto)  # UrunFoto modelini de kaydediyoruz
