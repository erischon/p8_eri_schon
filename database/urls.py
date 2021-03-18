from django.urls import path
from . import views

urlpatterns = [
    path('', views.etl, name='etl'),
    path('extract', views.etl_extract, name='etl_extract'),
    path('transform', views.etl_transform, name='etl_transform'),
    path('load', views.etl_load, name='etl_load'),
]