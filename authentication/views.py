from django.shortcuts import render
from authentication.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import auth

# Create your views here.
class SignUpView(APIView):
    
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
            
 