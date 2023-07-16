from django.shortcuts import render
from authentication.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import auth
from rest_framework.generics import ListAPIView
from authentication.models import User
from authentication.serializers import ReadUserSerializer
from authentication.permissions import IsAdminUser, DummyPermission1, DummyPermission2
from rest_framework_simplejwt.authentication import JWTAuthentication
from authentication.authentication import ThirdPartyAuthentication
from django.conf import settings

# Create your views here.
class SignUpView(APIView):
    
    authentication_classes = []
    permission_classes = []
    
    def post(self, request):
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        if not username:
            return Response({"error": True, "msg" : "Username is required"}, status=status.HTTP_400_BAD_REQUEST)
        if not email:
            return Response({"error": True, "msg" : "Email is required"}, status=status.HTTP_400_BAD_REQUEST)
        if not password:
            return Response({"error": True, "msg" : "Password is required"}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(username=username).exists():
            return Response({"error": True, "msg" : "This username already exists"}, status=status.HTTP_400_BAD_REQUEST)            
        if User.objects.filter(email=email).exists():
            return Response({"error": True, "msg" : "This email already exists"}, status=status.HTTP_400_BAD_REQUEST)
        User.objects.create_user(username=username, email=email, password=password)
        user = auth.authenticate(username=username, password=password)
        if user:
            return Response({"success": True, "msg" : "Authentication done !, try signing back with same credentials"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": True, "msg" : "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)
            
 
class UserListView(ListAPIView):
    # Doing OR for authentication classes
    # authentication_classes = (ThirdPartyAuthentication, JWTAuthentication)
    # Doing OR for permission classes
    # permission_classes = (DummyPermission1 | DummyPermission2, )  
    authentication_classes = (ThirdPartyAuthentication, JWTAuthentication)
    permission_classes = (IsAdminUser, )
    serializer_class = ReadUserSerializer
    
    def get_queryset(self):
        print("request user id", self.request.user.id)
        print("request user username", self.request.user.username)
        queryset = User.objects.all()
        return queryset
