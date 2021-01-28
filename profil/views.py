from django.shortcuts import render

# Create your views here.
def profilPerpustakaan(request):
    context = {
        'title':'Profil Perpustakaan'
    }
    return render(request, 'profil/profil-perpustakaan.html', context)

def layananPerpustakaan(request):
    context = {
        'title':'Layanan Perpustakaan'
    }
    return render(request, 'profil/layanan-perpustakaan.html', context)