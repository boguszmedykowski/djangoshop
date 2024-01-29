from django.urls import include, path
from rest_framework import routers
from app import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'carts', views.CartViewSet)
router.register(r'cartitems', views.CartItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += router.urls
