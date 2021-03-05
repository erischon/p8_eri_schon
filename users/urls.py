from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signupuser, name='signupuser'),
    path('moncompte/', views.moncompte, name='moncompte'),  
]