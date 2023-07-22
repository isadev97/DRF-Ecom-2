from rest_framework import serializers
from products.models import Product
from tags.serializers import ReadTagsSerializer

class WriteProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description','price', 'quantity', 'tags']
        
class ReadProductSerializer(serializers.ModelSerializer):
    
    tags = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'description','price', 'quantity', 'slug', 'tags']
    
    def get_tags(self, product):
        queryset = product.tags.all()
        return ReadTagsSerializer(queryset, many=True).data