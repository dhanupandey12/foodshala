from django.shortcuts import render, redirect, HttpResponseRedirect
from users.models import UserProfile
from .models import RestaurantProfile,MenuItems,Order
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import MenuForm
from django.contrib.auth.decorators import login_required

def index(request):
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            context = {
                'menu' : MenuItems.objects.all()
            }
            return render(request,'users/homepage.html',context)
        except:
            profile = RestaurantProfile.objects.get(user=request.user)
            menu = MenuItems.objects.all().filter(restaurant=profile)
            print(menu)
            context = {
                'menu' : menu
            }
            return render(request,'store/homepage.html',context)
    else:
        return render(request,'store/index.html')

def restaurant(request):
    return render(request,'store/restaurant.html')


def RestaurantRegister(request):
    if request.method == 'POST':
        user = User.objects.create_user(username=request.POST.get('username'),password=request.POST.get('password'))
        user.save()
        print(request.POST)
        profile = RestaurantProfile.objects.create(user=user,name='None')
        profile.save()
        return redirect('/login/')
    return render(request,'store/register.html')

@login_required
def addMenu(request):
    try:
        profile = RestaurantProfile.objects.get(user=request.user)
        if request.method == 'POST':
            formData = MenuForm(request.POST)
            if formData.is_valid():
                data = formData.save(commit=False)
                data.restaurant = RestaurantProfile.objects.get(user=request.user)
                data.save()
        form = MenuForm()
        return render(request,'store/addMenu.html',{'form':form})
    except:
        return redirect('/')

def menu(request):
    items = MenuItems.objects.all()
    return render(request,'store/menu.html',{'items':items})

@login_required
def orders(request):
    orders = Order.objects.all()
    restaurant = RestaurantProfile.objects.get(user = request.user)
    final_data = []
    for data in orders:
        if str(data.item.restaurant) == str(restaurant):
            final_data.append(data)
    context = {
        'orders' : final_data
    }
    return render(request,'store/orders.html',context)

@login_required
def order_done(request,id):
    order_obj = Order.objects.get(id=id)
    order_obj.seen = True
    order_obj.save()  
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))