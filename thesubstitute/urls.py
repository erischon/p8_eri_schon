from django.contrib import admin
from django.urls import path, include
from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls')),
    path('database/', include('database.urls')),
    path('users/', include('users.urls')),
    path('search/', include('search.urls')),
]
