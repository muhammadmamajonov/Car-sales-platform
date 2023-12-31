from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    def has_permission(self, request, view):
        if request.user:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        
        # Instance must have an attribute named `owner`.
        return obj.owner == request.user
    

class IsSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)