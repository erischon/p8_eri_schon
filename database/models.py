from django.db import models

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