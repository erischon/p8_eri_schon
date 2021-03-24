from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from database.models import Product, Prodcat, Categorie
from search.search import Search
from .forms import SearchForm

def get_query(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()
    return render(request, 'search/test.html', {'form': form})

def search_sub(request):
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
