from django.shortcuts import render
from database.models import Product, Prodcat, Categorie
from search.search import Search

def search_sub(request):
    query = "nutella"

    search = Search()
    search_product = search.find_product(query)
    result_info = search.find_substitute(search_product)

    return render(request, 'search/results.html', {'results': result_info, 'product': search_product}) 
