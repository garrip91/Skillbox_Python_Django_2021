from django.urls import path

from .views import translation_example



urlpatterns = [
    path('example/', translation_example, name='example'),
]