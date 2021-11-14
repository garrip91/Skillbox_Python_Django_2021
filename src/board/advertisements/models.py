from django.db import models


# Create your models here.
class Advertisement(models.Model):

    title = models.CharField(max_length=1000, db_index=True, verbose_name='Заголовок')
    description = models.CharField(max_length=1000, default='', verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.FloatField(verbose_name='Цена', default=0)
    views_count = models.IntegerField(verbose_name='Количество просмотров', default=0)
    status = models.ForeignKey('AdvertisementStatus', default=None, null=True, on_delete=models.CASCADE, related_name='advertisements', verbose_name='Статус')
    
    def __str__(self):
        return self.title
        
    class Meta:
        db_table = 'advertisements'
        ordering = ['title']
        
        
class AdvertisementStatus(models.Model):

    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name