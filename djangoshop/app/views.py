from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets, status
from app.models import Product
from app.serializers import GroupSerializer, UserSerializer, ProductSerializer
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Dodanie użytkownika do grupy 'customer'
        user = serializer.instance
        customer_group, created = Group.objects.get_or_create(name='customer')
        customer_group.user_set.add(user)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_permissions(self):
        """
        Zwraca uprawnienia, które będą stosowane do akcji widoku.
        Dla akcji tworzenia, zezwól wszystkim. Dla innych akcji, wymagaj autentykacji.
        """
        if self.action == 'create':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
