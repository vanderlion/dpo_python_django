from django.forms import ModelForm
from django.contrib.auth.models import Group
from .models import Product


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ["name"]


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "name", "price", "description", "discount"


