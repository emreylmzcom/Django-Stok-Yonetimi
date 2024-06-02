from django.contrib import admin
from django.utils.html import format_html
from .models import Kategori, Urun, UrunFoto

class UrunFotoInline(admin.TabularInline):
    model = UrunFoto
    extra = 1

    def get_formset(self, request, obj=None, **kwargs):
        formset = super().get_formset(request, obj, **kwargs)
        formset.form.base_fields['foto'].widget.attrs['style'] = 'width: 60%;'
        return formset

    def foto_thumbnail(self, instance):
        if instance.foto:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />'.format(instance.foto.url))
        return ""
    foto_thumbnail.short_description = 'Fotoğraf'

    readonly_fields = ['foto_thumbnail']

class UrunAdmin(admin.ModelAdmin):
    list_display = ('isim', 'kategori', 'fiyat', 'para_birimi', 'stok_miktari', 'birim')
    search_fields = ('isim', 'kategori__isim')
    list_filter = ('kategori', 'para_birimi')
    inlines = [UrunFotoInline]

class KategoriAdmin(admin.ModelAdmin):
    list_display = ['isim', 'parent']
    prepopulated_fields = {'slug': ('isim',)}

admin.site.register(Kategori, KategoriAdmin)
admin.site.register(Urun, UrunAdmin)
admin.site.register(UrunFoto)
