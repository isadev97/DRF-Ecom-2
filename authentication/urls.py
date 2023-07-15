from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path, include
from authentication.views import SignUpView


urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign_up'),
    path('sign-in/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
