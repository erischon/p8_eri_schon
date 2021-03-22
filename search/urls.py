from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_sub, name='search_sub'),
]