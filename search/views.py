from django.shortcuts import render

def search_sub(request):
    return render(request, 'search/results.html') 
