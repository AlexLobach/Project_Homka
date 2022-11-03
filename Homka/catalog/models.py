from django.db import models


# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Subcategories(models.Model):
    name = models.CharField(max_length=50)
    category = models.ManyToManyField('Categories', related_name='subcategory')
    subcategories_img = models.ImageField(upload_to='img/subcategories')

    def __str__(self):
        return f'{self.category}/{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)
    subcategory = models.ForeignKey('Subcategories', on_delete=models.CASCADE)
    product_img = models.ImageField(upload_to='img/product')
    price_per_kg = models.DecimalField(decimal_places=2, help_text="In BYN/kg")
    on_stock = models.DecimalField(decimal_places=2, help_text='entered the stock, "kg.gr"')
    in_stock = models.BooleanField(help_text="in stock/ out of stock")
    description = models.TextField()
    nutritional_value = models.TextField()
    min_pack = models.DecimalField(decimal_places=2, help_text='minimum packaging "kg.gr"')

