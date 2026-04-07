from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from api import views
from .views.generics import ProductDetailAPIView, ProductListAPIView
from .views.generics import CategoryDetailAPIView, CategoryListAPIView
from .views.generics import CategoryProductsAPIView

# router = DefaultRouter()
# router.register(r'categories', views.CategoryViewSet)
# router.register(r'products', views.ProductViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    # path('products/', product_list), #FBV
    # path('products/<int:product_id>/', product_detail), #FBV
    path('products/', ProductListAPIView.as_view()), #CBV, Mixins, Generics
    path('products/<int:product_id>/', ProductDetailAPIView.as_view()), #CBV, Mixins, Generics
    path('categories/', CategoryListAPIView.as_view()), #CBV, Mixins, Generics
    path('categories/<int:category_id>/', CategoryDetailAPIView.as_view()), #CBV, Mixins, Generics
    path('categories/<int:category_id>/products/', CategoryProductsAPIView.as_view()), #CBV, Mixins, Generics
]