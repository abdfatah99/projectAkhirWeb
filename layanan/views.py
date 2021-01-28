from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView, DetailView
from .models import *
from .forms import *

# Create your views here.


class catalogListView(ListView, FormView):
    model = catalog
    form_class = catalogForm
    template_name = "layanan/catalog.html"
    paginate_by = 1
    context_object_name = 'catalog_list'

    def get_queryset(self):
        lokasi = self.request.GET.get('lokasi')
        judul = self.request.GET.get('judul')
        penulis = self.request.GET.get('penulis')
        keyword = self.request.GET.get('keyword')
        if lokasi:
            catalog_list = self.model.objects.filter(lokasi__icontains=lokasi)
        elif judul:
            catalog_list = self.model.objects.filter(judul__icontains=judul)
        elif penulis:
            catalog_list = self.model.objects.filter(penulis__icontains=penulis)
        elif keyword:
            catalog_list = self.model.objects.filter(keyword__icontains=keyword)
        else:
            catalog_list = self.model.objects.all()
        
        return catalog_list

    


class repositoryListView(ListView, FormView):
    model = repository
    form_class = repositoryForm
    template_name = "layanan/repository.html"
    context_object_name = "repository_list"
    ordering = ["judul"]
    paginate_by = 1

    def get_queryset(self):
        jenis_penulisan = self.request.GET.get('jenis_penulisan')
        judul = self.request.GET.get('judul')
        penulis = self.request.GET.get('penulis')
        keyword = self.request.GET.get('keyword')
        lokasi = self.request.GET.get('lokasi')
        if jenis_penulisan:
            repository_list = self.model.objects.filter(jenis_penulisan__icontains=jenis_penulisan).order_by('id')
        elif judul:
            repository_list = self.model.objects.filter(judul__icontains=judul)
        elif penulis:
            repository_list = self.model.objects.filter(penulis__icontains=penulis)
        elif keyword:
            repository_list = self.model.objects.filter(keyword__icontains=keyword)
        elif lokasi:
            repository_list = self.model.objects.filter(lokasi__icontains=lokasi)
        else:
            repository_list = self.model.objects.all()
        
        return repository_list
    
class repositoryDetailView(DetailView):
    model = repository
    template_name = 'layanan/repositoryDetail.html'
    context_object_name = 'repository'

class journalListView(ListView, FormView):
    model = journal
    form_class = journalForm
    template_name = "layanan/journal.html"
    context_object_name = 'journal_list'
    ordering = ['judul_artikel']
    paginate_by = 1
    

    def get_queryset(self):
        judul_query = self.request.GET.get('judul_artikel')
        kata_kunci_query = self.request.GET.get('kata_kunci')
        penulis = self.request.GET.get('penulis')
        lokasi = self.request.GET.get('lokasi')
        if judul_query:
            journal_list = self.model.objects.filter(judul_artikel__icontains=judul_query)
        elif kata_kunci_query:
            journal_list = self.model.objects.filter(kata_kunci__icontains=kata_kunci_query)
        elif penulis:
            journal_list = self.model.objects.filter(penulis__icontains=penulis)
        elif lokasi:
            journal_list = self.model.objects.filter(lokasi__icontains=lokasi)
        else:
            journal_list = self.model.objects.all()
        
        return journal_list
 
class journalDetailView(DetailView):
    model = journal
    template_name = "layanan/journalDetail.html"
    context_object_name = 'journal'