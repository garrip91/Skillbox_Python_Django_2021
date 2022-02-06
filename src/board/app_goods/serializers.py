from rest_framework import serializers

from .models import DRF_Item



# class ItemSerializer(serializers.Serializer):

    # name = serializers.CharField(max_length=200)
    # description = serializers.CharField(allow_blank=True)
    # weight = serializers.FloatField(min_value=0)
    
    
class DRF_ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = DRF_Item
        fields = ['id', 'name', 'description', 'weight']