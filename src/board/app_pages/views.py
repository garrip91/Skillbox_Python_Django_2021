from django.shortcuts import render

import datetime
from django.utils.translation import gettext as _
from django.utils.formats import date_format

from django.views.decorators.cache import cache_page
from time import sleep



# Create your views here:
#@cache_page(30)
def translation_example(request, *args, **kwargs):
    
    #sleep(4)
    return render(request, 'translation_example.html')
    
    
def greetings_page(request, *args, **kwargs):

    greetings_message = _('Hello there! Today is %(date)s %(time)s') % {
        'date': date_format(datetime.datetime.now().date(), format='SHORT_DATE_FORMAT', use_l10n=True),
        'time': datetime.datetime.now().time()
    }
    return render(request, 'greetings.html', context={
        'greetings_message': greetings_message
    })