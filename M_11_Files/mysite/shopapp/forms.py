from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import Group
from .models import Product


class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ["name"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "name", "price", "description", "discount", "preview"

    images = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"multiple": True})
    )
