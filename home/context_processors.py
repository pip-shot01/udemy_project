from . models import *
# from . views import _cart_id



def menuinks(request):
    links = Category.objects.all()
    return dict(links=links)

# def counter(request):
#     cart_count = 0
#     if 'admin' in request.path:
#         return{}
#     else:
#         try:
#             cart = Cart.objects.filter(cart_id=_cart_id(request))
#             cart_items = CartItem.objects.all().filter(cart=Cart[:1])
#             for cart_item in cart_items:
#                 cart_count += cart_item.quantity
#         except Cart.DoesNotExist:
#             cart_count = 0
#     return dict(cart_count=cart_count)