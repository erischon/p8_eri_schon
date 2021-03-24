from django.shortcuts import render
from database.models import Product, Prodcat, Categorie
from search.search import Search

def search_sub(request):
    query = "Nutella"
    search = Search()
    result_infos = []

    search_product = search.find_product(query)
    product = search.product_infos(search_product)

    for categorie in product['categories']:
        result_info = search.find_substitute(search_product)
        result_infos.extend(search.result_infos(result_info))
    
    result_infos = [i for n, i in enumerate(result_infos) if i not in result_infos[n + 1:]]

    return render(request, 'search/results.html', {'product': product, 'results': result_infos}) 
