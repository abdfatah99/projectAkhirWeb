from django.urls import path
from petunjuk.views import *

app_name = 'petunjuk'
urlpatterns = [
    path('petunjuk-perpustakaan', petunjukPerpustakaan, name="petunjuk-perpustakaan"),
    path('peminjamanpengembalian-buku', peminjamanBuku, name="peminjaman-buku"),
]