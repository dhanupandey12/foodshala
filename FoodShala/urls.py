from django.contrib import admin
from django.urls import path
from django.conf import settings

from django.contrib.auth import views as auth_views
from store import views as store_view
from users import views as users_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',store_view.index,name='index'),
    path('restaurant/',store_view.restaurant,name='restaurant'),
    path('restaurant/register/',store_view.RestaurantRegister,name='RestaurantRegister'),
    path('restaurant/orders/',store_view.orders,name='orders'),
    path('order-done/<int:id>/',store_view.order_done,name='order_done'),
    path('users/',users_view.users,name='users'),
    path('users/register/',users_view.UserRegister,name='UserRegister'),
    path('dashboard/',users_view.dashboard,name='dashboard'),
    path('login/',auth_views.LoginView.as_view(template_name = 'users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL),name='logout'),
    path('add-item/',store_view.addMenu,name='add-item'),
    path('add-cart/<int:id>/',users_view.add_cart,name='add_cart'),
    path('cart/',users_view.cart,name='cart'),
    path('remove-cart/<int:id>/',users_view.remove_cart,name='remove_cart'),
    path('order-now/<int:id>/',users_view.order_now,name='order_now'),
    path('orders/',users_view.myorder,name='myorder'),
    path('menu/',store_view.menu,name='menu')
]
