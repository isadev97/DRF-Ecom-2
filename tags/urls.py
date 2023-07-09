from django.urls import path, include
from tags.views import CreateTagView, DetailTagView, ListTagView, DetailTagV2View, ListTagV2View

urlpatterns = [
    path('create/', CreateTagView.as_view(), name='create_tag'),
    path('detail/<str:slug>/', DetailTagView.as_view(), name='detail_tag'),
    path('detail/v2/<str:slug>/', DetailTagV2View.as_view(), name='detail_tag_v2'),
    path('list/', ListTagView.as_view(), name='list_tag'),
    path('list/v2/', ListTagV2View.as_view(), name='list_tag_V2'),
]