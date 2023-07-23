from django.urls import path, include
urlpatterns = [
    path('tags/', include('tags.urls')),
    path('authentication/', include('authentication.urls')),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
]