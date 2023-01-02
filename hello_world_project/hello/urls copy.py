from django.urls import path

from hello import views
from hello.models import LogMessage

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="hello/home.html",
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("openai/", views.openai, name="openai"),
    path("openai/models", views.openai_models, name="openai_models"),
    path("openai/play", views.openai_play, name="openai_play"),
    path("openai/play_list", views.openai_play_list, name="openai_play_list"),
    path("log/", views.log_message, name="log"),
]