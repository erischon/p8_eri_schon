from django.shortcuts import render

def home_page(request):
    return render(request, 'webapp/home.html') 

def mentions(request):
    return render(request, 'webapp/mentions.html') 