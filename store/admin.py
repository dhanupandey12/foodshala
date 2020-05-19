from django.contrib import admin
from .models import RestaurantProfile,MenuItems,Cart,Order
# Register your models here.

admin.site.register(RestaurantProfile)
admin.site.register(MenuItems)
admin.site.register(Cart)
admin.site.register(Order)