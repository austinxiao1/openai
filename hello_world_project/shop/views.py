import json
from django.http import Http404, HttpResponse
from django.shortcuts import HttpResponseRedirect, get_object_or_404, redirect, render
from django.utils.timezone import datetime
from django.views.generic import ListView 


def home(request):
    return render(request, "shop/home.html")
  