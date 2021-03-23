from django.shortcuts import render
from database.models import Product, Prodcat, Categorie
from search.search import Search

def search_sub(request):
    query = "nutella"
    search = Search()

    search_product = search.find_product(query)
    product = search.product_infos(search_product)

    result_info = search.find_substitute(search_product)
    result_infos = search.result_infos(result_info)

    return render(request, 'search/results.html', {'product': product, 'results': result_infos}) 
