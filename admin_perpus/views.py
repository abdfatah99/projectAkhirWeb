from django.shortcuts import render, redirect
from layanan.models import * # import database
from django.contrib.auth import views as auth_views
from layanan.forms import * #import form terima data 
from .forms import *

# Create your views here.
def admin_perpus(request):
    context = {
        'title' : 'Perpustakaan'
    }
    return render(request, 'admin_perpus/login.html', context)

def pilihanCrud(request):
    context = {
        'title': 'Form CRUD'
    }
    return render(request, 'admin_perpus/pilihanCrud.html', context)

#======================================================================

def formCrudCatalog(request, id=0):
    if request.method == 'GET':
        if id==0:
            form = formCatalog()
            pesan = 'Data A'
        else:
            updateCatalog = catalog.objects.get(pk=id)
            form = catalogForm(instance=updateCatalog)
            pesanb = "data B"
        context = {
            'title': 'Catalog',
            'form': form
        }
        return render(request, "admin_perpus/formCrudCatalog.html", context)
    else:
        form = formCatalog(request.POST)
        if form.is_valid():
            form.save()
            pesanc = "Data C"
            return render(request, 'admin_perpus/formCrudCatalogList.html')

def formCrudCatalogList(request):
    data = catalog.objects.all()
    if len(data) > 0:
        pesan = "data ada di database"
    elif len(data) < 0:
        pesan = "data samadengan minus"
    else: 
        pesan = "data sama dengan noll"
    
    kartu_ucapan = 'selamat datang'

    context = {
        'catalog_list': data,
        'pesan': pesan,
        'kartu_ucapan': kartu_ucapan,
        'welcome': "selamat datang"
    }
    return render(request, 'admin_perpus/formCrudCatalogList.html', {'kata': 'selamat datang'})

#-------------------------------------------------------------------------------

def formCrudJurnal(request):
    if request.method == 'GET':
        if id==0:
            form = formJournal()
        else:
            updateJurnal = journal.objects.get(pk=id)
            form = journalForm(instance=updateJurnal)
        
        context = {
            'title': 'Jurnal',
            'form': form
        }
        return render(request, "admin_perpus/formCrudJournal.html", context)
    
    else:
        form = formJurnal(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'admin_perpus/formCrudJournalList.html')

def formCrudJurnalList(request):
    data = journal.objects.all()

    context = {
        'journal_list': data
    }
    return render(request, 'admin_perpus/formCrudJournalList.html')

#--------------------------------------------------------------------------------

def formCrudRepository(request):
    form = formRepository()

    context = {
        'title': 'Repository',
        'form': form
    }
    return render(request, 'admin_perpus/formCrudRepository.html', context)

def formCrudRepositoryList(request):
    return render(request, 'admin_perpus/formCrudRepositoryList.html')
