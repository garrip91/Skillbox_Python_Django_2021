from django.shortcuts import render

from django.http import HttpResponse


def advertisement_list(request, *args, **kwargs):
    
    return HttpResponse('<ul><li>Мастер на час</li><li>Выведение из запоя</li><li>Услуги экскаватора-погрузчика, гидромолота, ямобура</li></ul>')