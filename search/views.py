from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from database.models import Product, Prodcat, Categorie
from search.search import Search
from .forms import SearchForm

def search_results(request):
    query = request.GET['q']
    search = Search()
    result_infos = []

    search_product = search.find_product(query)

    if not search_product:
        return render(request, 'search/results.html', {'product': "None"})
    else:
        product = search.product_infos(search_product)

        for categorie in product['categories']:
            result_info = search.find_substitute(search_product)
            result_infos.extend(search.result_infos(result_info))
        
        result_infos = [i for n, i in enumerate(result_infos) if i not in result_infos[n + 1:]]

        return render(request, 'search/results.html', {'product': product, 'results': result_infos}) 

def search_sub(request):
    return render(request, 'webapp/home.html')

def saving(request):
    ''' I'm saving a Product in the User's Myproduct model. '''
    return redirect('myproducts')
