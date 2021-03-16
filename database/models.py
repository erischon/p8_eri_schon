from django.db import models
from django.contrib.auth.models import User

class Categorie(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=150)

class Shops(models.Model):
    shop_id = models.AutoField(primary_key=True)
    shop_name = models.CharField(max_length=150)

class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=150)

class Nutriscore(models.Model):
    nut_id = models.AutoField(primary_key=True)
    nut_type = models.CharField(max_length=1)

class Product(models.Model):
    prod_id = models.BigIntegerField(primary_key=True)
    prod_name = models.CharField(max_length=250)
    prod_url = models.CharField(max_length=150)
    nut_id = models.ForeignKey(Nutriscore, on_delete=models.CASCADE)

class Myproduct(models.Model):
    myprod_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    prod_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    save_time = models.DateTimeField()

class Prodcat(models.Model):
    cat_id = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    prod_id = models.ForeignKey(Product, on_delete=models.CASCADE)

class Prodshop(models.Model):
    shop_id = models.ForeignKey(Shops, on_delete=models.CASCADE)
    prod_id = models.ForeignKey(Product, on_delete=models.CASCADE)

class Prodbrand(models.Model):
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE)
    prod_id = models.ForeignKey(Product, on_delete=models.CASCADE)
