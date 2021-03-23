from database.models import Product, Prodcat, Categorie, Nutriscore
from django.db.models import F

class Search:

    def __init__(self):
        self.result_info = {}
        self.categories = []

    def find_product(self, query):
        """ """
        try:
            result = Product.objects.filter(prod_name=query)
        except Exception as error:
            exception = f"Il y a l'erreur suivante : {error}."
            return exception

        if not result:
            result = "Désolé, nous n'avons pas ce produit dans notre base de données."
            return result
        else:
            # I take the first result
            result = result[0]
            return result
    
    def find_substitute(self, product):
        """ I'm the algorithm. """
        nutriscore = product.nut_id.nut_id
        # /!\ Attention pour le moment je ne cherche que sur UNE categorie
        categorie = Prodcat.objects.filter(prod_id=product.prod_id)[0]

        product_list = Product.objects.filter(prodcat__cat_id=categorie.cat_id).filter(nut_id__lte=(nutriscore-1)).order_by('nut_id', 'prod_name').values_list()[:10]

        return product_list

    def result_infos(self, queryset):
        """ """
        result_info = []

        for product in queryset:
            prod_id = product[0]
            prod_name = product[1]
            prod_url = product[2]
            prod_image = product[3]
            nutriscore = Nutriscore.objects.get(nut_id=product[4]).nut_type

            result_info.append({'prod_id': prod_id, 'prod_name': prod_name, 'prod_url': prod_url, 'prod_image': prod_image, 'nutriscore': nutriscore})

        return result_info


    def product_infos(self, object):
        """ I extract the informations taht I need. """
        result = object
        product_info = {}
        prod_id = result.prod_id
        nutriscore = result.nut_id.nut_type 
        categorie_list = Prodcat.objects.filter(prod_id=result.prod_id)     
        for categorie in categorie_list:
            categorie = categorie.cat_id.cat_name
            self.categories.append(categorie)

        product_info = {'prod_id': prod_id, 'nutriscore': nutriscore, 'categories': self.categories}
        
        return product_info


if __name__ == "__main__":
    search = Search()