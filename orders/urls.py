from django.urls import path
from orders.views import CreateOrderView, OrderListView, OrderDetailView

urlpatterns = [
    path('create/', CreateOrderView.as_view(), name='create_product'),
    path('list/', OrderListView.as_view(), name='product_list'),
    path('detail/<int:id>/', OrderDetailView.as_view(), name='product_detail'),
]

