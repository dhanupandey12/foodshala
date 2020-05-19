from django.shortcuts import render,HttpResponseRedirect,redirect
from .models import UserProfile
from django.contrib.auth.models import User
from store.models import Cart,Order,MenuItems
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.

def users(request):
    return render(request,'users/users.html')

def UserRegister(request):
    if request.method == 'POST':
        user = User.objects.create_user(username=request.POST.get('username'),password=request.POST.get('password'))
        user.save()
        if 'veg' in request.POST:
            veg = True
        else:
            veg = False
        profile = UserProfile.objects.create(user=user,name='None',veg=veg)
        cart = Cart.objects.create(user=user)
        cart.save()
        profile.save()
    return render(request,'users/register.html')

def dashboard(request):
    
    return render(request,'users/dashboard.html')

def login(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request,'users/login.html')

@login_required
def add_cart(request,id):
    item = MenuItems.objects.get(id=id)
    cart_obj = Cart.objects.get(user = request.user)
    cart_obj.item.add(item)
    cart_obj.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def cart(request):
    cart = Cart.objects.get(user = request.user)
    context = {
        'menu' : cart.item.all()
    }
    return render(request,'users/cart.html',context)

@login_required
def remove_cart(request,id):
    item = MenuItems.objects.get(id=id)
    cart_obj = Cart.objects.get(user = request.user)
    cart_obj.item.remove(item)
    cart_obj.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def order_now(request,id):
    item = MenuItems.objects.get(id=id)
    print(item)
    order_obj = Order.objects.create(user=request.user,item=item)
    order_obj.save()
    return render(request,'users/success.html')

@login_required
def myorder(request):
    orders = Order.objects.all().filter(user=request.user)
    context = {
        'orders' : orders
    }
    return render(request,'users/order.html',context)