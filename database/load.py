import json
from itertools import chain

from django.db import connection, models
from database.models import Product, Nutriscore, Categorie, Prodcat, Brand, Prodbrand, Shop, Prodshop


class Load:
    def __init__(self):
        """ """
        self.connection = connection.cursor()
        self.open_json()

    def open_json(self):
        """ I open the json. """
        with open("static/database/off_data_transform.json", encoding="utf-8") as json_file:
            self.my_products = json.load(json_file)

    def load_data(self):
        """ I load all the data from transform.json to their table. """

        for prod_key in list(self.my_products.keys()):
            prod_to_load = self.my_products[prod_key]

            # Insert Product
            if Product.objects.filter(pk=prod_key).exists() is False:
                nut_id = Nutriscore.objects.get(nut_type=prod_to_load["nutriscore_grade"][0].upper())
                query = Product(prod_id=prod_key, prod_name=prod_to_load['product_name_fr'], prod_url=prod_to_load['url'], nut_id=nut_id)
                query.save()
            else:
                pass

            prod_object = Product.objects.get(pk=prod_key)

            # Insert Categories
            for n in range(len(prod_to_load["categories"])):
                # In categorie table
                if Categorie.objects.filter(cat_name=prod_to_load["categories"][n]).exists() is False:
                    query = Categorie(cat_name=prod_to_load["categories"][n])
                    query.save()

                # In prodcat table
                cat_object = Categorie.objects.get(cat_name=prod_to_load["categories"][n])
                cat_id = cat_object.cat_id
                if Prodcat.objects.filter(cat_id=cat_id, prod_id=prod_key).exists() is False:
                    query = Prodcat(cat_id=cat_object, prod_id=prod_object)
                    query.save()

            # Insert Brand
            for n in range(len(prod_to_load["brands"])):
                # In brand table
                if Brand.objects.filter(brand_name=prod_to_load["brands"][n]).exists() is False:
                    query = Brand(brand_name=prod_to_load['brands'][n])
                    query.save()

                # In prodbrand table
                brand_object = Brand.objects.get(brand_name=prod_to_load["brands"][n])
                brand_id = brand_object.brand_id
                if Prodbrand.objects.filter(brand_id=brand_id, prod_id=prod_key).exists() is False:
                    query = Prodbrand(brand_id=brand_object, prod_id=prod_object)
                    query.save()

            # Insert Shop
            for n in range(len(prod_to_load["stores"])):
                # In shop table
                if Shop.objects.filter(shop_name=prod_to_load["stores"][n]).exists() is False:
                    query = Shop(shop_name=prod_to_load['stores'][n])
                    query.save()

                # In prodshop table
                shop_object = Shop.objects.get(shop_name=prod_to_load["stores"][n])
                shop_id = shop_object.shop_id
                if Prodshop.objects.filter(shop_id=shop_id, prod_id=prod_key).exists() is False:
                    query = Prodshop(shop_id=shop_object, prod_id=prod_object)
                    query.save()

        message = "REUSSITE du chargement des produits"
        return message

    def load_nutriscore(self):
        """ I load the nutriscore and their id into the table. """
        try:
            query = "INSERT INTO database_nutriscore (nut_id, nut_type) VALUES (1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), (5, 'E')"
            self.connection.execute(query)
            message = "REUSSITE : Les différents Nutriscore ont été chargés dans la base."
            return message

        except Exception as ex:
            return ex

if __name__ == "__main__":
    loader = Load()

    # === Tests of methods ===
    # loader.open_json()
    # loader.load_nutriscore()
    # loader.load_data()
