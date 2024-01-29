from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    Uprawnienie, które pozwala na tworzenie produktów tylko użytkownikom należącym do grupy 'admin'.
    Wszyscy inni użytkownicy mają tylko uprawnienia do odczytu.
    """

    def has_permission(self, request, view):
        # Wszyscy użytkownicy mogą odczytywać
        if request.method in permissions.SAFE_METHODS:
            return True

        # Tylko użytkownicy należący do grupy 'admin' mogą tworzyć, modyfikować i usuwać
        return request.user.groups.filter(name='admin').exists()
