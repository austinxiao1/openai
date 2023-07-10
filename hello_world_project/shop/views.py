import json
from django.http import Http404, HttpResponse
from django.shortcuts import HttpResponseRedirect, get_object_or_404, redirect, render
from django.utils.timezone import datetime
from django.views.generic import ListView
from shop.forms import ProductAddForm

from shop.models.product import Product 


def home(request):
    return render(request, "shop/home.html")


def admin_home(request):
    print("admin_home:")
    context = {}
    # play_list=OpenAIPlay.objects.order_by("-create_date")[:50],  # :5 limits the results to the five most recent
    context["product_list"] = Product.objects.all().order_by("created_at") 

    return render(request, "shop/admin/product_list.html", context)


def admin_product_add(request):
    form = ProductAddForm(request.POST or None)
    print("admin_product_add:")
    context = {}
    # play_list=OpenAIPlay.objects.order_by("-create_date")[:50],  # :5 limits the results to the five most recent
    context["form"] =form 

    return render(request, "shop/admin/product_add.html", context)
  