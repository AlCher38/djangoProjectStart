from django.urls import path
from newapps.apps import CatalogConfig
from newapps.views import index

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
]