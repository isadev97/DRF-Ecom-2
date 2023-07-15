from rest_framework.permissions import BasePermission
from authentication.models import User

class IsUserAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return isinstance(request.user, User)