from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import RetrieveAPIView, ListAPIView, DestroyAPIView
from tags.models import Tags
from tags.serializers import WriteTagsSerializer, ReadTagsSerializer
from django.utils.text import slugify
from django.core.cache import cache
from tags.utils import StandardResultsSetPagination
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from authentication.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from products.models import Product
from django.db import transaction
from orders.models import Order, OrderItems
from orders.serializers import ReadOrderSerializer

# Create your views here.
class CreateOrderView(APIView):    

    def post(self, request):
        orders = request.data.get('orders')
        payment_mode = request.data.get('payment_mode')
        payment_status = request.data.get('payment_status')
        user_id = request.user.id 
        with transaction.atomic():
            order = Order.objects.create(
                user_id=user_id,
                payment_mode=payment_mode,
                payment_status=payment_status,
                payment_amount=0 # doing this to 0 
            )
            total_amount = 0
            for product_id, qty in orders.items():
                product_id = int(product_id)
                product = Product.objects.get(pk=product_id)
                # inventory 100 placing 20 
                # min (20, 100 ) => 20 eligible or legitimate
                # inventory 200 placing 400 
                # min(200, 400) => 200 we make it eligible or legitimate
                qty = min(product.quantity, int(qty))
                total_amount += product.price * qty
                OrderItems.objects.create(
                    product_id=product_id,
                    order_id=order.id,
                    # price and quantity at the time of order
                    # these price and quantity does not belong to price and quantity at the time of inventory
                    # this price can have discount too 
                    # this quantity should be eligible or legitimate as done above
                    price=product.price,
                    quantity=qty
                )
            order.payment_amount = total_amount
            order.save()
        response_data = ReadOrderSerializer(instance=order).data
        return Response(response_data, status=status.HTTP_200_OK)
        
        
        

class OrderDetailView(RetrieveAPIView):
    pass

class OrderListView(ListAPIView):
    pass