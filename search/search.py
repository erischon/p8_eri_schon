from database.models import Product, Prodcat, Categorie

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
    
    def find_substitute(self, query):
        """ I'm the algorithm. """
        result = query
        result_info = {}
        # categorie = Prodcat.objects.filter(prod_id=query.prod_id)[0]

        # prod_list = Prodcat.objects.filter(cat_id=categorie.cat_id)
        # prod_list = prod_list.prod_id

        categorie_list = Prodcat.objects.filter(prod_id=result.prod_id)
        for categorie in categorie_list:
            categorie = categorie.cat_id.cat_name
            self.categories.append(categorie)

        prod_list = self.categories
        return prod_list

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