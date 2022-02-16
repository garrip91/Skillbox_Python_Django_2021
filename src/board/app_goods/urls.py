from django.urls import path

from .views import items_list, update_prices, DRF_items_list, DRF_ItemList, DRF_ItemDetail



urlpatterns = [
    path('items/', items_list, name='items_list'),
    path('update_prices/', update_prices, name='update_prices'),
    #path('DRF_items/', DRF_items_list, name='DRF_items_list'),
    path('DRF_items/', DRF_ItemList.as_view(), name='DRF_ItemList'),
    path('DRF_items/<int:pk>/', DRF_ItemDetail.as_view(), name='DRF_ItemDetail'),
]