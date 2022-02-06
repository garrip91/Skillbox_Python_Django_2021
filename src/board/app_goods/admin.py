from django.contrib import admin

from .models import Item, DRF_Item



# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('code', 'price')
    
admin.site.register(Item, ItemAdmin)


class DRF_ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
admin.site.register(DRF_Item, DRF_ItemAdmin)