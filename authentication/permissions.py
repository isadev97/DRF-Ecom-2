from rest_framework.permissions import BasePermission
from authentication.models import User
from django.conf import settings

class IsUserAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return isinstance(request.user, User)
    
class IsActiveUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_active == True
    
class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser == True

class DummyPermission1(BasePermission):
    
    # adding a custom message in your permission
    message = "coming from permission 1"
    
    def has_permission(self, request, view):
        return True
    
class DummyPermission2(BasePermission):
    
    # adding a custom message in your permission
    message = "coming from permission 2"
    
    def has_permission(self, request, view):
        return False

