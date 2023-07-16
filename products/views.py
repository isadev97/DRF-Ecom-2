from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, ListAPIView, DestroyAPIView


# Create your views here.
class CreateProductView(APIView):    
    pass 

class DetailProductView(RetrieveAPIView):
    # queryset = Tags.objects.all()
    # serializer_class = ReadTagsSerializer
    # lookup_field = "slug"
    pass 

class ListProductView(ListAPIView):
    pass
