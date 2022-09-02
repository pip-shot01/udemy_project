from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name="index"),
    path('store', views.store, name="store"),
    path('<slug:category_slug>/', views.store, name="products_by_category"),
    path('category_slug/<str:id>', views.product_detail, name="product_detail"),
]
