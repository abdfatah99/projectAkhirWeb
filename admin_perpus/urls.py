from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'admin_perpus'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name= 'admin_perpus/login.html'), name='login'),
    path('pilihanCrud/', views.pilihanCrud, name='pilihanCrud' ),
    path('formCrudCatalog/', views.formCrudCatalog, name='formCrudCatalog'),
    path('formCrudCatalogList/', views.formCrudCatalogList, name='formCrudCatalogList'),
    path('formCrudCatalog/<int:id>/', views.formCrudCatalog, name='formCrudCatalogUpdate'),
    path('formCrudJurnal/', views.formCrudJurnal, name='formCrudJurnal'),
    path('formCrudJurnalList/', views.formCrudJurnalList, name='formCrudJurnalList'),
    path('formCrudRepository/', views.formCrudRepository, name='formCrudRepository'),
    path('formCrudRepositoryList/', views.formCrudRepositoryList, name='formCrudRepositoryList')
]