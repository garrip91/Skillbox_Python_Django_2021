from django.contrib import admin

from app_library.models import Publisher



class PublisherAdmin(admin.ModelAdmin):
    
    list_display = ['id', 'name', 'city']


# Register your models here:
admin.site.register(Publisher, PublisherAdmin)