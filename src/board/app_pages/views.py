from django.shortcuts import render



# Create your views here:
def translation_example(request, *args, **kwargs):

    return render(request, 'translation_example.html')