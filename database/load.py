import json
from itertools import chain

from django.db import connection, models
from database.models import Product, Nutriscore


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

            # Insert Products
            if Product.objects.filter(pk=prod_key).exists() is False:
                nut_id = Nutriscore.objects.get(nut_type=prod_to_load["nutriscore_grade"][0].upper())
                query = Product(prod_id=prod_key, prod_name=prod_to_load['product_name_fr'], prod_url=prod_to_load['url'], nut_id=nut_id)
                query.save()
                return "OK"
            else:
                return "Fail"

            # Insert Categories
            for n in range(len(prod_to_load["categories"])):
                # In categories table
                if self.read_categorie(prod_to_load["categories"][n]) is False:
                    add_categorie = ("INSERT INTO database_categorie SET cat_name=%s")
                    self.connection.execute(add_categorie, (prod_to_load['categories'][n],))
                    self.connection.commit()
                # In prodcat table
                cat_id = self.read_categorie(prod_to_load["categories"][n])
                check = self.search_id(
                    f"SELECT * FROM database_prodcats WHERE cat_id='{cat_id}' AND prod_id='{prod_key}' "
                )
                if not (check):
                    add_prodcat = ("INSERT INTO database_prodcat SET cat_id=%s, prod_id=%s")
                    self.connection.execute(add_prodcat, (cat_id, prod_key))
                    # self.connection.commit()

            # Insert Brand
            for n in range(len(prod_to_load["brands"])):
                # In brand table
                if self.read_brand(prod_to_load["brands"][n]) is False:
                    add_brand = ("INSERT INTO database_brand SET brand_name=%s")
                    self.connection.execute(add_brand, (prod_to_load['brands'][n],))
                    # self.connection.commit()
                # In prodbrand table
                brand_id = self.read_brand(prod_to_load["brands"][n])
                check = self.search_id(
                    f"SELECT * FROM database_prodbrand WHERE brand_id='{brand_id}' AND prod_id='{prod_key}' "
                )
                if not (check):
                    add_prodbrand = ("INSERT INTO database_prodbrand SET brand_id=%s, prod_id=%s")
                    self.connection.execute(add_prodbrand, (brand_id, prod_key))
                    # self.connection.commit()

            # Insert Shops
            for n in range(len(prod_to_load["stores"])):
                # In shops table
                if self.read_shop(prod_to_load["stores"][n]) is False:
                    add_shop = ("INSERT INTO database_shop SET shop_name=%s")
                    self.connection.execute(add_shop, (prod_to_load['stores'][n],))
                    # self.connection.commit()
                # In prodshop table
                shop_id = self.read_shop(prod_to_load["stores"][n])
                check = self.search_id(
                    f"SELECT * FROM database_prodshop WHERE shop_id='{shop_id}' AND prod_id='{prod_key}' "
                )
                if not (check):
                    add_prodshop = ("INSERT INTO database_prodshop SET shop_id=%s, prod_id=%s")
                    self.connection.execute(add_prodshop, (shop_id, prod_key))
                    # self.connection.commit()

        message = "REUSSITE du chargement des produits"
        return message

    def read_categorie(self, value):
        """ I search if the category is already in the table. """
        query = ("SELECT cat_id FROM database_categorie WHERE cat_name LIKE %s")
        self.connection.execute(query, (value,))
        result = self.connection.fetchall()
        if len(result) < 1:
            return False
        else:
            return int(result[0][0])

    def read_brand(self, value):
        """  I search if the brand is already in the table.  """
        query = ("SELECT brand_id FROM database_brand WHERE brand_name LIKE %s")
        self.connection.execute(query, (value,))
        result = self.connection.fetchall()
        if len(result) < 1:
            return False
        else:
            return int(result[0][0])

    def read_shop(self, value):
        """  I search if the shop is already in the table. """
        query = ("SELECT shop_id FROM database_shop WHERE shop_name LIKE %s")
        self.connection.execute(query, (value,))
        result = self.connection.fetchall()
        if len(result) < 1:
            return False
        else:
            return int(result[0][0])

    def find_product(self, value):
        """  I search if the product is already in the table. """
        if Product.objects.filter(pk=value).exists():
            return True      
        else:
            return False
    
    def read_nutriscore(self, value):
        """  I search if the nutriscore is already in the table. """
        query = ("SELECT nut_id FROM database_nutriscore WHERE nut_type LIKE %s")
        self.connection.execute(query, (value,))
        result = self.connection.fetchall()
        if len(result) < 1:
            return False
        else:
            return int(result[0][0])

    def search_id(self, query):
        """ I search an ID. """
        self.connection.execute(query)
        rows = self.connection.fetchall()
        return rows

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
