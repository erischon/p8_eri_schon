from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_sub, name='search_sub'),
    path('query/', views.get_query, name='get_query'),
]