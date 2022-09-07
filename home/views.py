from django.shortcuts import render, HttpResponse, redirect
from . models import Cart, CartItem, Category, Product
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
# Create your views here.

def index(request):
    products = Product.objects.all().filter(is_available=True)
    context = {
        'products':products,
    }
    return render(request, 'home.html', context)

def store(request, category_slug=None):
    categories = None
    products = None
    
    #print products by their different categories
    if category_slug != None:
        categories = get_object_or_404(Category,slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
         #Paginator line
        paginator = Paginator(products, 2)
        page =  request.GET.get('page')
        paged_products= paginator.get_page(page)
        
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        #Paginator line
        paginator = Paginator(products, 3)
        page =  request.GET.get('page')
        paged_products= paginator.get_page(page)
        
        product_count = products.count()
    
    context = {
        'products':paged_products,
        'product_count':product_count,
    }
    
    return render(request, 'store.html', context)

def product_detail(request,id):
    try:
        single_product = Product.objects.get(pk=id)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
        # return HttpResponse(in_cart)
        # exit()
    except Exception as e:
        raise e
    context = {
        'single_product':single_product,
        'in_cart':in_cart,
    }
    return render(request, 'product_detail.html',context)


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart 

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)  #get the Product
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))  #get the cart using the cart_id present in the session
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()
    # return HttpResponse('cart_item.product')
    # exit()
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1     #cart_item.quantity = cart_item.quantity + 1
        cart_item.save()
        # return HttpResponse(cart_item.product)
        # exit()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1, 
            cart=cart,
        )
        cart_item.save()
    # return HttpResponse(cart_item.product)
    # exit()
    return redirect('cart')
    
def cart(request, total=0, quantity=0, cart_items=None):
    try:
        # tax=0
        # grand_total=0
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity 
        tax = (2 * total)/ 100
        grand_total = total + tax
    except ObjectDoesNotExist:
        pass 
    context = {
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        'tax': tax,  
        'grand_total':grand_total,        
     } 
    return render(request, 'cart.html', context)


def remove_cart(request, id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

def remove_cart_item(request, id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart')
    
    
def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(description__icontains=keyword)|Q(product_name__icontains=keyword))
            product_count = products.count()
        context = {
            'products':products,
            'product_count':product_count,
        }
        
    return render(request, 'store.html', context)