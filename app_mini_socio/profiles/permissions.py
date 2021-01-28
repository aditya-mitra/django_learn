from rest_framework import permissions

class IsOwnProfileOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS or obj.user == request.user:
            return True
        return False
