from django.urls import path

from .views import items_list, update_prices, DRF_items_list



urlpatterns = [
    path('items/', items_list, name='items_list'),
    path('update_prices/', update_prices, name='update_prices'),
    path('DRF_items/', DRF_items_list, name='DRF_items_list'),
]