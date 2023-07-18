from rest_framework import permissions
from rest_framework.permissions import IsAdminUser
class IsAdminOrIsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to
    Anyone can read
    Owners of an object to edit it and cant delete article.
    Admin user can do anything
    """
    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            return True

        # Check if the request method is safe (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == "POST":
            return  bool(request.user and request.user.is_authenticated)
        elif request.method=='DELETE':
            return False
        elif request.method == "PUT" or request.method == "PATCH" :
            return bool(request.user and request.user.is_authenticated)
        
    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_staff:
            return True

        # Check if the request method is safe (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == "POST":
            return  bool(request.user and request.user.is_authenticated)
        
        elif request.method=='DELETE':
            return False
        elif request.method == "PUT" or request.method == "PATCH" :
            return  obj.author == request.user
        