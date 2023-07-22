from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, ListAPIView, DestroyAPIView
from authentication.permissions import IsAdminUser
from products.serializers import WriteProductSerializer
from products.models import Product
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.utils.text import slugify
from products.serializers import ReadProductSerializer
from tags.utils import StandardResultsSetPagination

# Create your views here.
class CreateProductView(APIView):    
    
    permission_classes = (IsAdminUser, )
    
    def post(self, request):
        serializer = WriteProductSerializer(data=request.data)
        if serializer.is_valid():
            product = Product.objects.create(
                name=serializer.validated_data.get('name'),
                slug=slugify(serializer.validated_data.get('name')),
                price=serializer.validated_data.get('price'),
                quantity=serializer.validated_data.get('quantity'),
                description=serializer.validated_data.get('description'),
            )
            product.tags.set(serializer.validated_data.get('tags'))
            return Response(status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

class DetailProductView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ReadProductSerializer
    lookup_field = "slug"

class ListProductView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ReadProductSerializer
    pagination_class = StandardResultsSetPagination 
