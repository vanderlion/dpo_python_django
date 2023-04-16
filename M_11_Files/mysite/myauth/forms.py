from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import Group
from .models import Account


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = "user", "avatar"

    images = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"multiple": True})
    )
