from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name="index"),
    path('categories/store/', views.store, name="store"),
    path('categories/<slug:category_slug>/', views.store, name="products_by_category"),
    path('categories/details/<str:id>/', views.product_detail, name="product_detail"),
    path('search/', views.search, name="search"),

    path('cart', views.cart, name='cart'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remove_cart/<str:id>/', views.remove_cart, name='remove_cart'),
    path('remove_cart_item/<str:id>/', views.remove_cart_item, name='remove_cart_item'),
]
