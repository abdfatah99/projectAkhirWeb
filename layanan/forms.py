from django.forms import ModelForm
from django import forms
from layanan.models import catalog, journal, repository

class catalogForm(forms.ModelForm):
    class Meta:
        model = catalog
        fields = '__all__'
            
        widgets = {
            'lokasi' : forms.Select({'class':'form-select', 'type':'search','name':'lokasi'}),
            'judul' : forms.TextInput({'class':'form-control', 'type':'search', 'name':'judul', 'placeholder':'Judul'}),
            'penulis' : forms.TextInput({'class':'form-control', 'type':'search' ,'name':'penulis', 'placeholder':'Penulis'}),
            'keyword' : forms.TextInput({'class':'form-control', 'type':'search' ,'name':'keyword', 'placeholder':'Keyword'}),
        }


class journalForm(forms.ModelForm):
    class Meta:
        model = journal
        fields = [
            'judul_artikel',
            'kata_kunci',
            'penulis',
            'lokasi',
        ]

        widgets = {
            'judul_artikel' : forms.TextInput({'class':'form-control', 'type':'search','name':'judul_artikel', 'placeholder':'Judul'}),
            'kata_kunci' : forms.TextInput({'class':'form-control', 'type':'search','name':'kata_kunci', 'placeholder':'Keyword'}),
            'penulis' : forms.TextInput({'class':'form-control', 'type':'search','name':'penulis', 'placeholder':'Penulis'}),
            'lokasi' : forms.TextInput({'class':'form-control', 'type':'search','name':'lokasi', 'placeholder':'Lokasi'}),
        }

class repositoryForm(forms.ModelForm):
    class Meta:
        model = repository
        fields = [
            'jenis_penulisan',
            'judul',
            'penulis',
            'keyword',
            'lokasi',
        ]

        widgets = {
            'jenis_penulisan' : forms.Select({'class':'form-select', 'type':'search','name':'jenis'}),
            'judul' : forms.TextInput({'class':'form-control', 'type':'search','name':'judul', 'placeholder':'Judul'}),
            'penulis' : forms.TextInput({'class':'form-control', 'type':'search','name':'penulis', 'placeholder':'Penulis'}),
            'keyword' : forms.TextInput({'class':'form-control', 'type':'search','name':'keyword', 'placeholder':'Keyword'}),
            'lokasi' : forms.Select({'class':'form-select', 'type':'search','name':'lokasi'})    
        }

