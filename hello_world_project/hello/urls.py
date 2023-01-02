from django.urls import path

from hello import views
from hello.models import LogMessage
 
urlpatterns = [
    path("",  views.openai_play_list, name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("openai/", views.openai, name="openai"),
    path("openai/models", views.openai_models, name="openai_models"),
    path("openai/play", views.openai_play_list, name="openai_play"),
    path("openai/play/<id>", views.openai_play_detail, name="openai_play_detail"),
    path("openai/play/<id>/delete", views.openai_play_delete, name="openai_play_delete"),
    path("openai/play_create", views.openai_play_create, name="openai_play"),
    path("openai/play_list", views.openai_play_list, name="openai_play_list"),
    path("log/", views.log_message, name="log"),
]