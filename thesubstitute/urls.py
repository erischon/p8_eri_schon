from django.contrib import admin
from django.urls import path, include, re_path
from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls')),
    path('database/', include('database.urls')),
    path('users/', include('users.urls')),
    path('search/', include('search.urls')),
]

handler404 = 'webapp.views.error_404'
handler400 = 'webapp.views.error_404'
