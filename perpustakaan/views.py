from django.shortcuts import render

def index(request):
    context = {
        'title': 'Perpustakaan'
    }
    return render(request, 'index.html', context)