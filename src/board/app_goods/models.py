from django.db import models



# Create your models here:
class Item(models.Model):

    code = models.CharField(max_length=100, verbose_name='Код товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')