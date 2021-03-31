from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_sub, name='search_sub'),
    path('result/', views.search_results, name='search_results'),
    path('saving/<int:product>', views.saving, name='saving'),
]