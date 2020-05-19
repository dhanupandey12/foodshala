from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from users.models import UserProfile

# Create your models here

class RestaurantProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField("Name",blank=False,max_length = 200)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Restaurant Profile'
        verbose_name_plural = 'Restaurant Profile'

class MenuItems(models.Model):
    restaurant = models.ForeignKey(RestaurantProfile,on_delete=models.CASCADE)
    item = models.CharField(max_length = 200,blank=False)
    price = models.IntegerField(default=120)
    is_veg = models.BooleanField(default=True)

    def __str__(self):
        return self.item
    
    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'

class Cart(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    item = models.ManyToManyField(MenuItems,blank=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Cart'

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItems,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    seen = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Order'