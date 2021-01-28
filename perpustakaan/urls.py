from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('profil/', include('profil.urls')),
    path('petunjuk/', include('petunjuk.urls')),
    path('layanan/', include('layanan.urls')),
    path('admin_perpus/', include('admin_perpus.urls'))
]
