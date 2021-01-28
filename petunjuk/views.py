from django.shortcuts import render

# Create your views here.

def petunjukPerpustakaan(request):
    context = {
        'title':'Petunjuk Perpustakaan'
    }
    return render(request, 'petunjuk/petunjuk-perpustakaan.html', context)

def peminjamanBuku(request):
    context = {
        'title':'Peminjaman/Pengembalian Buku'
    }
    return render(request, 'petunjuk/peminjaman-buku.html', context)