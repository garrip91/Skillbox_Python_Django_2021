from django.shortcuts import render

from .models import Item
from .forms import UploadPriceForm
from csv import reader
from decimal import Decimal
from django.http import HttpResponse

from django.http import JsonResponse
from .entities import Item

from .serializers import ItemSerializer



# Create your views here:
def items_list(request):

    items = Item.objects.all()
    
    return render(request, 'goods/items_list.html', {'items_list': items})
    
    
def update_prices(request):

    if request.method == 'POST':
        upload_file_form = UploadPriceForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            price_file = upload_file_form.cleaned_data['file'].read()
            price_str = price_file.decode('utf-8').split('\n')
            csv_reader = reader(price_str, delimiter=',', quotechar='"')
            for row in csv_reader:
                Item.objects.filter(code=row[0]).update(price=Decimal(row[1]))
                # print(row[0], Item.objects.filter(code=str(row[0]))) ### ОТДЕЛЬНО ДОБАВЛЕНО
                print(row[0], Item.objects.filter(code='A123123')) ### ОТДЕЛЬНО ДОБАВЛЕНО
            return HttpResponse(content='Цены были успешно обновлены!', status=200)
    else:
        upload_file_form = UploadPriceForm()
        
    context = {
        'form': upload_file_form
    }
    return render(request, 'media/upload_file.html', context=context)
    
    
def DRF_items_list(request):
    
    if request.method == 'GET':
        items_for_sale = [
            Item(
                name='Кофеварка',
                description='Варит отличный кофе',
                weight=100
            ),
            Item(
                name='Беспроводные наушники',
                description='Отличный звук',
                weight=150
            ),
        ]
        #return JsonResponse(ItemSerializer(items_for_sale, many=True).data, safe=False)
        return JsonResponse(ItemSerializer(Item(
            name='Кофеварка',
            description='Варит отличный кофе',
            weight=100
        )).data, safe=False)