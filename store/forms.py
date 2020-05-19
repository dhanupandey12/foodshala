from django import forms
from .models import MenuItems

class MenuForm(forms.ModelForm):
    class Meta:
        model = MenuItems
        fields = ('item','price','is_veg')