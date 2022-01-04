from django import forms



class UploadPriceForm(forms.Form):

    file = forms.FileField()