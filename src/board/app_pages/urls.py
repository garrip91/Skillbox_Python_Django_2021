from django.urls import path

from .views import translation_example, greetings_page



urlpatterns = [
    path('example/', translation_example, name='example'),
    path('greetings/', greetings_page, name='greetings_page'),
]