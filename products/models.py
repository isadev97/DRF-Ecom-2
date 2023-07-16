from django.db import models
from tags.models import Tags

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    description = models.TextField(null=True)
    price = models.BigIntegerField()
    quantity = models.BigIntegerField(default=0)
    tags = models.ManyToManyField(Tags)
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
     
# product = Product.objects.get(pk=id)
# [1, 2, 3, 4, 5] => list of unique tags ids 
# product.tags.set([1, 2, 3, 4, 5])
# this will create the mapping in products_product_tags table