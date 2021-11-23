from django import forms

#from app_profiles.models import User
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'