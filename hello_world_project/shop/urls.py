from django.urls import path
from django.views.generic import RedirectView

from shop import views 
 
urlpatterns = [
    path("",  RedirectView.as_view(url='/shop/home')), 
    path("shop/home", views.home, name="hello_there"),
]