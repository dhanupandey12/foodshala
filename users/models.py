from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField("Full Name", blank=True,max_length = 100)
    veg = models.BooleanField("Vegetarian",default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'User Profiles'
        verbose_name_plural = 'User Profiles'