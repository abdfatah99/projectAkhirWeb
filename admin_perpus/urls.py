from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'admin_perpus'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name= 'admin_perpus/login.html'), name='login'),
    path('pilihanCrud/', views.pilihanCrud, name='pilihanCrud' ),
    path('formCrudCatalog/', views.formCrudCatalog, name='formCrudCatalog'),                # get and post req. insert operation
    path('formCrudCatalog/<int:id>/', views.formCrudCatalog, name='formCrudCatalogUpdate'), # get and post req. update operation
    path('catalogList/', views.catalogList, name='catalogList'),                            # get req. to retrieve and display all record
    path('catalogDelete/<int:id>/', views.catalogDelete, name='catalogDelete'),
    path('formCrudJurnal/', views.formCrudJurnal, name='formCrudJurnal'),
    path('formCrudJurnal/<int:id>', views.formCrudJurnal, name='formCrudJurnalUpdate'),
    path('jurnalList/', views.jurnalList, name='jurnalList'),
    path('jurnalDelete/<int:id>/', views.jurnalDelete, name='jurnalDelete'),
    path('formCrudRepository/', views.formCrudRepository, name='formCrudRepository'),
    path('formCrudRepository/<int:id>', views.formCrudRepository, name='formCrudRepositoryUpdate'),
    path('repositoryList/', views.repositoryList, name='repositoryList'),
    path('repositoryDelete/<int:id>/', views.repositoryDelete, name='repositoryDelete')
]