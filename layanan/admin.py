from django.contrib import admin
from .models import catalog, journal, repository

# Register your models here.
admin.site.register(catalog)

class journalAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']

admin.site.register(journal, journalAdmin)

class repositoryAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']
admin.site.register(repository, repositoryAdmin)