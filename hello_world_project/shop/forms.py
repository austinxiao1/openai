from django import forms

from hello.models import LogMessage, OpenAIPlay, User
from shop.models.product import Product


class ProductAddForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name",)  # NOTE: the trailing comma is required

 
