from django.urls import path, include
from .views import CategoryViewSet, ProductViewSet, PrecioFinalView
from rest_framework.routers import DefaultRouter
# 1. Importar las vistas prefabricadas de simplejwt
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# products/urls.py

router = DefaultRouter()
router.register('products', ProductViewSet, basename='product')
router.register('categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('products/<int:pk>/precio-final/', PrecioFinalView.as_view(),
         name='precio_final'),
    path('', include(router.urls))
]