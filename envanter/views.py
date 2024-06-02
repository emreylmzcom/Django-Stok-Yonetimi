from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Kategori, Urun


def urun_listesi(request):
    kategoriler = Kategori.objects.filter(parent__isnull=True)
    urunler = Urun.objects.all()
    kategori_slug = request.GET.get('kategori_slug')
    if kategori_slug:
        urunler = urunler.filter(kategori__slug=kategori_slug)
    return render(request, 'envanter/urun_listesi.html', {'urunler': urunler, 'kategoriler': kategoriler})


def kategori_urun_listesi(request, slug):
    kategori = get_object_or_404(Kategori, slug=slug)
    urunler = Urun.objects.filter(kategori=kategori)
    kategoriler = Kategori.objects.all()
    return render(request, 'envanter/kategori_urun_listesi.html', {'kategori': kategori, 'urunler': urunler, 'kategoriler': kategoriler})

def urun_detay(request, slug):
    urun = get_object_or_404(Urun, slug=slug)
    kategoriler = Kategori.objects.all()
    return render(request, 'envanter/urun_detay.html', {'urun': urun, 'kategoriler': kategoriler})

def anasayfa(request):
    kategoriler = Kategori.objects.all()
    return render(request, 'envanter/anasayfa.html', {'kategoriler': kategoriler})

def iletisim(request):
    kategoriler = Kategori.objects.all()
    return render(request, 'envanter/iletisim.html', {'kategoriler': kategoriler})

def hakkimizda(request):
    kategoriler = Kategori.objects.all()
    return render(request, 'envanter/hakkimizda.html', {'kategoriler': kategoriler})
