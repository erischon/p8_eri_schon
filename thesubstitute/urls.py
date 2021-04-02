from django.contrib import admin
from django.urls import path, include
from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('database/', include('database.urls')),
    path('', views.home_page, name='home'),
    path('mentions/', views.mentions, name='mentions'),
    path('users/', include('users.urls')),
    path('search/', include('search.urls')),
]
