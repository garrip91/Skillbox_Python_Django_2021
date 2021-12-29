from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User



class ExtendedRegisterForm(UserCreationForm):

    first_name = forms.CharField(max_length=30, required=False, help_text='Имя')
    last_name = forms.CharField(max_length=30, required=False, help_text='Фамилия')
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')