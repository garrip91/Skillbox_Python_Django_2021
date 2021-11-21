from django.shortcuts import render

from django.http import HttpResponse

# from django.views import View
from django.views.generic import TemplateView

from advertisements.models import Advertisement

from django.views.generic import ListView, DetailView




def advertisement_list(request, *args, **kwargs):

    advertisements = Advertisement.objects.all()

    # advertisements = [
        # 'Мастер на час',
        # 'Выведение из запоя',
        # 'Услуги экскаватора-погрузчика, гидромолота, яморуба'
    # ]
    
    # return render(request, 'advertisements/advertisement_list.html', {'advertisements': advertisements})
    return render(request, 'advertisements/advertisements.html', {'advertisements': advertisements})
    
    
def get_client_ip(request):

    ip = request.META.get('REMOTE_ADDR')
    
    return ip
    
    
# class About(View):

    # def get(self, request):
        # return render(request, 'advertisements/about.html', {})
class About(TemplateView):

    template_name = 'advertisements/about.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Бесплатные объявления в Вашем городе'
        context['title'] = 'Бесплатные объявления'
        context['description'] = """
            Вы хотите продать или купить что-либо быстро и выгодно? К Вашим услугам доска бесплатных объявлений! На нашем портале Вы найдёте всё, начиная от мелких бытовых приборов и заканчивая недвижимостью и автомобилями. А если Вы продаёте товар, услугу, сдаёте или снимаете жильё, мы поможем решить Вашу задачу быстро и эффективно. Для этого просто добавьте объявление! Это бесплатно!"""
        return context
        
        
class AdvertisementListView(ListView):

    model = Advertisement
    template_name = 'advertisements/advertisement_list.html'
    context_object_name = 'advertisement_list'
    queryset = Advertisement.objects.all()[:5]
    
    
class AdvertisementDetailView(DetailView):

    model = Advertisement