from django.shortcuts import render
from database.models import Product, Prodcat, Categorie

def search_sub(request):
    query = "nutella"
    result_info = {}
    result = Product.objects.filter(prod_name=query)[0]

    if not result:
        result = "Désolé, nous n'avons pas ce produit dans notre base de données."
    else:
        prod_id = result.prod_id
        nutriscore = result.nut_id.nut_type
        categorie = Prodcat.objects.filter(prod_id=result.prod_id)

        result_info = {'prod_id': prod_id, 'nutriscore': nutriscore, 'categorie': categorie}

    return render(request, 'search/results.html', {'results': result_info}) 
