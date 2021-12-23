from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from app_users.models import Profile



class AuthForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    
# class RegisterForm(UserCreationForm):

    # #first_name = forms.CharField(max_length=30, required=False, help_text='Имя')
    # #last_name = forms.CharField(max_length=30, required=False, help_text='Фамилия')
    # date_of_birth = forms.DateField(required=True, help_text='Дата рождения')
    # city = forms.CharField(max_length=36, required=False, help_text='Город')
    # # ****** #
    # print(User._meta.fields)
    # # ****** #
    
    # class Meta:
        # model = User
        # #fields = ('username', 'first_name', 'last_name', 'password1', 'password2')
        # #fields = ('username', 'first_name', 'last_name', 'date_of_birth ', 'city')
        # fields = ('username', 'first_name', 'last_name')
        
        
class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['date_of_birth', 'city']