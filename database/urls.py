from django.urls import path
from . import views

urlpatterns = [
    path('', views.etl, name='etl'), 
]