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
            result = result[0]
            prod_id = result.prod_id
            nutriscore = result.nut_id.nut_type 
            categorie_list = Prodcat.objects.filter(prod_id=result.prod_id)     
            for categorie in categorie_list:
                categorie = categorie.cat_id.cat_name
                self.categories.append(categorie)

            self.result_info = {'prod_id': prod_id, 'nutriscore': nutriscore, 'categories': self.categories}
            return self.result_info
    
    def find_substitute(self, query):
        pass


if __name__ == "__main__":
    search = Search()