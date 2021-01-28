from django.urls import path
from profil.views import *

app_name = "profil"
urlpatterns = [
    path('profil-perpustakaan/', profilPerpustakaan, name="profil-perpustakaan"),
    path('layanan-perpustakaan/', layananPerpustakaan, name="layanan-perpustakaan"),
]