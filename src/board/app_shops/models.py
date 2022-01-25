from django.db import models

#from django.utils.translation import gettext_lazy as _



# Create your models here.
class Shop(models.Model):

    #name = models.CharField(max_length=100, name=_('name'))
    name = models.CharField(max_length=100, name='name')