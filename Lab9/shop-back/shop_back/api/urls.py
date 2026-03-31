from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'products', views.ProductViewSet)

urlpatterns = [
#     path('products/', views.products),
#     path('products/<int:id>/', views.product),
#     path('categories/', views.categories),
#     path('categories/<int:id>/', views.category),
#     path('categories/<int:id>/products/', views.CategoryViewSet.products_by_category),
    path('', include(router.urls)),
]