from django.urls import path, include
urlpatterns = [
    path('tags/', include('tags.urls'))
]