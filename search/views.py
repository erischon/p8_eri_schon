from django.shortcuts import render
from database.models import Product

def search_sub(request):
    result_list = {}
    query = "nutella"
    results = Product.objects.filter(prod_name=query)
    if not results:
        results = "Désolé, nous n'avons pas ce produit dans notre base de données."
    else:
        for result in results:
            prod_id = results.values('prod_id')
            nutriscore = results.values('nut_id')

            result_list = {result: {'prod_id': prod_id, 'nutriscore': nutriscore}}

    return render(request, 'search/results.html', {'results': result_list}) 
