from django.urls import path
from layanan.views import *

app_name = 'layanan'
urlpatterns = [
    path('catalog/', catalogListView.as_view(), name='catalog'),
    path('repository/', repositoryListView.as_view(), name="repository"),
    path('repositoryDetail/<slug:slug>/', repositoryDetailView.as_view(), name='repository_detail'),
    path('journal/', journalListView.as_view(), name="journal"),
    path('journalDetail/<slug:slug>/', journalDetailView.as_view(), name='journal_detail'),
]