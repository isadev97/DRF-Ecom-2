from rest_framework import serializers
from products.models import Product

class WriteProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description','price', 'quantity', 'tags']
        
class ReadProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description','price', 'quantity', 'slug']