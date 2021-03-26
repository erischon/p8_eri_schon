from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from database.models import Product, Prodcat, Categorie
from search.search import Search
from .forms import SearchForm

def search_results(request):
    search = Search()
    query = request.GET['q']
    result_infos = []

    search_product = search.find_product(query)
    product = search.product_infos(search_product)

    for categorie in product['categories']:
        result_info = search.find_substitute(search_product)
        result_infos.extend(search.result_infos(result_info))
    
    result_infos = [i for n, i in enumerate(result_infos) if i not in result_infos[n + 1:]]

    return render(request, 'search/results.html', {'product': product, 'results': result_infos}) 

def search_sub(request):
    # query = request.GET['q']
    query = 'nutella'
    search = Search()
    result_infos = []

    search_product = search.find_product(query)
    product = search.product_infos(search_product)

    for categorie in product['categories']:
        result_info = search.find_substitute(search_product)
        result_infos.extend(search.result_infos(result_info))
        # result_infos.extend(result_info)
    
    result_infos = [i for n, i in enumerate(result_infos) if i not in result_infos[n + 1:]]

    return render(request, 'search/results.html', {'product': product, 'results': result_infos}) 
