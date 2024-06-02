from django.db import models
from django.utils.text import slugify
import itertools

class Kategori(models.Model):
    isim = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='alt_kategoriler', on_delete=models.CASCADE)

    def __str__(self):
        return self.isim

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.isim)
        super(Kategori, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategoriler'


class Urun(models.Model):
    PARA_BIRIMLERI = [
        ('TL', 'Türk Lirası'),
        ('USD', 'Dolar'),
        ('EUR', 'Euro'),
    ]

    isim = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True) 
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    aciklama = models.TextField(blank=True, null=True)
    fiyat = models.DecimalField(max_digits=10, decimal_places=2)
    eski_fiyat = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stok_miktari = models.PositiveIntegerField()
    birim = models.CharField(max_length=50, choices=[('adet', 'Adet'), ('kilo', 'Kilo')])
    para_birimi = models.CharField(max_length=3, choices=PARA_BIRIMLERI, default='TL')
    fotoğraf = models.ImageField(upload_to='urun_fotograflari/', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.isim)
            for i in itertools.count(1):
                if not Urun.objects.filter(slug=slug).exists():
                    break
                slug = f'{slug}-{i}'
            self.slug = slug
        super(Urun, self).save(*args, **kwargs)

    def __str__(self):
        return self.isim
        
    class Meta:
        verbose_name = 'Ürün'
        verbose_name_plural = 'Ürünler'


class UrunFoto(models.Model):
    urun = models.ForeignKey(Urun, related_name='fotolar', on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='urun_fotograflari/')

    def __str__(self):
        return self.urun.isim

    class Meta:
       verbose_name = 'Ürün Fotoğraf Ekleme'
       verbose_name_plural = 'Ürün Fotoğraf Ekleme'
