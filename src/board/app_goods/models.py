from django.db import models

from django.utils.translation import gettext_lazy as _



# Create your models here:
class Item(models.Model):

    code = models.CharField(max_length=100, verbose_name=_('code'))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_('price'))
    
    class Meta:
        verbose_name_plural = _('goods')
        verbose_name = _('good')
        
        
class DRF_Item(models.Model):

    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    weight = models.FloatField(verbose_name='Масса')