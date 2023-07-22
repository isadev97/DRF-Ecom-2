from django.urls import path
from products.views import CreateProductView, DetailProductView, ListProductView

urlpatterns = [
    path('create/', CreateProductView.as_view(), name='create_product'),
    path('list/', ListProductView.as_view(), name='product_list'),
    path('detail/<str:slug>/', DetailProductView.as_view(), name='product_detail'),
]

