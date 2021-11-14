from django.urls import path
from .views import advertisement_list, About, AdvertisementListView, AdvertisementDetailView


urlpatterns = [
    path('', advertisement_list, name='advertisement_list'),
    path('<int:pk>', AdvertisementDetailView.as_view(), name='advertisement_detail'),
    path('about/', About.as_view(), name='about'),
    path('advertisements', AdvertisementListView.as_view(), name='advertisement'),
]
