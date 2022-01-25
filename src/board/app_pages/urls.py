from django.urls import path

from .views import translation_example, greetings_page

from django.views.decorators.cache import cache_page



urlpatterns = [
    path('example/', cache_page(30)(translation_example), name='example'),
    path('greetings/', greetings_page, name='greetings_page'),
]