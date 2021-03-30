from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signupuser, name='signupuser'),
    path('moncompte/', views.moncompte, name='moncompte'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),  
    path('myproducts/', views.myproducts, name='myproducts'),  
]