from django.shortcuts import render, redirect
from layanan.models import *  # import database
from django.contrib.auth import views as auth_views
from layanan.forms import *  # import form terima data
from .forms import *

# Create your views here.


def admin_perpus(request):
    context = {
        'title': 'Perpustakaan'
    }
    return render(request, 'admin_perpus/login.html', context)


def pilihanCrud(request):
    greeting = 'selamat datang'
    context = {
        'title': 'Form CRUD',
        'ucapan': greeting
    }
    return render(request, 'admin_perpus/pilihanCrud.html', context)

# ======================================================================


def catalogList(request):
    data = catalog.objects.all()
    context = {
        'catalog_list': data

    }
    return render(request, 'admin_perpus/listCatalog.html', context)


def formCrudCatalog(request, id=0):
    if request.method == 'GET':
        # input pertama user -> id data = 0
        if id == 0:
            form = formCatalog()
        # kalau datanya diambil dari db -> id data != 0
        else:
            updateCatalog = catalog.objects.get(pk=id)
            form = formCatalog(instance=updateCatalog)
        context = {
            'title': 'Catalog',
            'form': form,
            'namaMethod': "formCrudCatalog(if)"
        }
        return render(request, "admin_perpus/formCrudCatalog.html", context)

    else:
        form = formCatalog(request.POST)
        if form.is_valid():
            form.save()

        return redirect('catalogList/')


def catalogDelete(request, id):
    deleteCatalog = catalog.objects.get(pk=id)
    deleteCatalog.delete()
    return redirect('catalogList/')

# -------------------------------------------------------------------------------


def jurnalList(request):
    data = journal.objects.all()

    context = {
        'journal_list': data,
        'namaMethod': "jurnalList"
    }
    return render(request, 'admin_perpus/listJurnal.html', context)


def formCrudJurnal(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = formJournal()
        else:
            updateJurnal = journal.objects.get(pk=id)
            form = formJournal(instance=updateJurnal)

        context = {
            'title': 'Jurnal',
            'form': form,
            'namaMethod': "formCrudJurnal(if)"
        }
        return render(request, "admin_perpus/formCrudJournal.html", context)

    else:
        form = formJournal(request.POST)
        if form.is_valid():
            form.save()
            context = {
                'namaMethod': 'formCrudJurnal(else)'
            }
        return redirect('jurnalList/')


def jurnalDelete(request, id):
    deleteJurnal = jurnal.objects.get(pk=id)
    deleteJurnal.delete()
    return redirect('jurnalList/')

# --------------------------------------------------------------------------------


def repositoryList(request):
    data = repository.objects.all()

    context = {
        'repository_list': data,
        'namaMethod': "repositoryList"
    }
    return render(request, 'admin_perpus/repositoryList.html', context)


def formCrudRepository(request, id=0):
    if request.method == 'GET':
        if id == 0:  # we have an insert operation
            form = formRepository()
        else:  # update operation
            updateRepository = repository.objects.get(pk=id)
            form = formRepository(instance=updateRepository)

        context = {
            'title': 'Repository',
            'form': form,
            'namaMethod': "formRepository(if)"
        }
        return render(request, "admin_perpus/formCrudRepository.html", context)

    # post request
    else:
        if id == 0:  # masukan pertama kali
            form = formRepository(request.POST)
        else:  # update
            updateRepository = repository.objects.get(pk=id)
            form = formRepository(request.POST, instance=updateRepository)

        if form.is_valid():
            form.save()
            context = {
                'namaMethod': 'formCrudRepository(else)'
            }
        return redirect('repositoryList/')


def repositoryDelete(request, id):
    deleteRepository = catalog.objects.get(pk=id)
    deleteRepository.delete()
    return redirect('repositoryList/')
