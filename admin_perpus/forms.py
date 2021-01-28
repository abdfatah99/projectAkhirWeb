from django.forms import ModelForm
from django import forms
from layanan.models import *

class formCatalog(forms.ModelForm):
    class Meta:
        model = catalog
        fields = '__all__'  
    
    widget = {
        'judul': forms.TextInput({'class': 'form-control'})
    }
    
    def __init__(self, *args, **kwargs):
        super(formCatalog,self).__init__(*args, **kwargs)
        self.fields['bahasa'].empty_label = "Select"
        # self.fields['jumlah_buku'].required = False
 
class formJournal(forms.ModelForm):
    class Meta:
        model = journal
        fields = '__all__' 

class formRepository(forms.ModelForm):
    class Meta:
        model = repository
        fields = '__all__' 