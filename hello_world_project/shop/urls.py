from django.urls import path
from django.views.generic import RedirectView

from shop import views 
 
urlpatterns = [
    path("",  RedirectView.as_view(url='/shop/home')), 
    path("shop/home", views.home, name="hello_there"),
    path("shop/admin/home", views.admin_home, name="admin_home"),
    path("shop/admin/product_add", views.admin_product_add, name="admin_product_add"),
]