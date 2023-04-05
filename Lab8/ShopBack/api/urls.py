from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.getProductList),
    path('products/<id>/', views.getProduct),
    path('categories/', views.getCategories),
    path('categories/<id>/', views.getCategory),
    path('categories/<id>/products/', views.getByCategory)
]