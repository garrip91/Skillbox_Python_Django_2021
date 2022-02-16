from django.shortcuts import render

from .models import Item
from .forms import UploadPriceForm
from csv import reader
from decimal import Decimal
from django.http import HttpResponse

from django.http import JsonResponse
from .entities import Item

#from .serializers import ItemSerializer

from rest_framework.views import APIView

from rest_framework import status
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.response import Response
from .models import DRF_Item
from .serializers import DRF_ItemSerializer
from rest_framework.generics import GenericAPIView



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
        
        
# class DRF_ItemList(APIView):
class DRF_ItemList(ListModelMixin, CreateModelMixin, GenericAPIView):
    """Представление для получения списка товаров и создания нового товара"""

    # queryset = DRF_Item.objects.all()
    serializer_class = DRF_ItemSerializer
    
    def get_queryset(self):
        queryset = DRF_Item.objects.all()
        item_name = self.request.query_params.get('name')
        if item_name:
            queryset = queryset.filter(name=item_name)
        return queryset

    def get(self, request):
        # items = DRF_Item.objects.all()
        # serializer = DRF_ItemSerializer(items, many=True)
        # return Response(serializer.data)
        return self.list(request)
        
    def post(self, request, format=None):
        # serializer = DRF_ItemSerializer(data=request.data)
        # if serializer.is_valid():
            # serializer.save()
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
            # return Response(status=status.HTTP_400_BAD_REQUEST)
        return self.create(request)
        
        
class DRF_ItemDetail(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
    """Представление для получения детальной информации о товаре, а также для его редактирования и удаления"""

    queryset = DRF_Item.objects.all()
    serializer_class = DRF_ItemSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
        
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
        
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)