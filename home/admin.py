from django.contrib import admin
from . models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','product_name','price','stock', 'category','modified_date','is_available',]
    prepopulated_fields = {'slug': ('product_name',)}

# @admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['quantity']

class CartAdmin(admin.ModelAdmin):
    list_display = ['date_added']
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Cart, CartAdmin)
