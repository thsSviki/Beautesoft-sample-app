from django.db import models


class Custom(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)

class Product(models.Model):
    product_n = models.CharField(max_length=255)
    price = models.FloatField()
    #image= models.ImageField(upload_to='img/',default='img/index.jpeg')

class Purchase(models.Model):
    product = models.CharField(max_length=255)
    price = models.FloatField()
    purchaser = models.EmailField(max_length=100)

class Billing(models.Model):
    address = models.CharField(max_length=250)
