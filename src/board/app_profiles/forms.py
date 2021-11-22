from django import forms


class UserForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField()
    first_name = forms.CharField()
    second_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    birthday = forms.DateField()