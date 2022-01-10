from django.urls import path

from .views import upload_file, model_form_upload



urlpatterns = [
    path('upload_file/', upload_file, name='upload_file'),
    path('model_form_upload_file/', model_form_upload, name='model_form_upload_file'),
]