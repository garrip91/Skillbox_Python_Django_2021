from django.urls import path

from .views import page_with_cached_fragments



urlpatterns = [
    path('page_with_cached_fragments/', page_with_cached_fragments, name='page_with_cached_fragments'),
]