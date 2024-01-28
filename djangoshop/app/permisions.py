from rest_framework import permissions


class CreateUserPermission(permissions.BasePermission):
    """
    Custom permission to only allow creation of new users without authentication.
    """

    def has_permission(self, request, view):
        if view.action == 'create':
            return True
        return request.user and request.user.is_authenticated
