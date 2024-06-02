from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from envanter import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.anasayfa, name='anasayfa'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),
    path('urunler/', views.urun_listesi, name='urun_listesi'),
    path('kategori/<slug:slug>/', views.kategori_urun_listesi, name='kategori_urun_listesi'),
    path('urun/<slug:slug>/', views.urun_detay, name='urun_detay'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
