import json
from django.http import Http404, HttpResponse
from django.shortcuts import HttpResponseRedirect, get_object_or_404, redirect, render
from django.utils.timezone import datetime
from django.views.generic import ListView
from hello import openai_api

from hello.forms import LogMessageForm, LoginForm, OpenAIPlayForm
from hello.models import LogMessage, OpenAIPlay, User


class HomeListView(ListView):
    """Renders the home page, with a list of all polls."""

    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context


def openai(request):
    return render(request, "hello/openai.html")


def openai_models(request):
    model_list = openai_api.get_model_list()
    # print("model_list:", model_list["data"])
    return render(request, "hello/openai_models.html", {'model_list': model_list["data"]})


def about(request):
    """Renders the about page."""
    return render(request, "hello/about.html")


def contact(request):
    """Renders the contact page."""
    return render(request, "hello/contact.html")


def hello_there(request, name):
    """Renders the hello_there page.
    Args:
        name: Name to say hello to
    """
    return render(
        request, "hello/hello_there.html", {"name": name,
                                            "date": datetime.now()}
    )


def openai_play_create(request):
    if not validate_login(request):
        return HttpResponseRedirect("/login")
    form = OpenAIPlayForm(request.POST or None)
    print("openai_play:")

    if request.method == "POST":
        if form.is_valid():
            play = form.save(commit=False)

            answer_in_db = OpenAIPlay.objects.filter(
                question__iexact=play.question)
            if len(answer_in_db) > 0:
                return redirect("play/"+str(answer_in_db[0].id))

            play.create_date = datetime.now()

            print("asking question:", play.question)
            if play.category == "Q&A":
                response = openai_api.get_answer(play.question, play.model)
            elif play.category=="Summarize for a 2nd grader":
                response = openai_api.get_summarization(play.question, play.model) 
            elif play.category=="Code Generation":
                response = openai_api.get_code(play.question, play.model)
            elif play.category=="Keyword":
                response = openai_api.get_answer(play.question, play.model)
            else: 
                response = openai_api.get_answer(play.question, play.model)

            answer = response.choices[0]
            play.model = response.model
            play.answer = answer.text
            play.full_response = str(response)
            print("response:", response)
            play.save()
            context = {"form": form, "response": response, "answer": answer}
            return redirect("play/"+str(play.id))
        else:
            print("form is invalid")
    return render(request, "hello/openai_play.html", {"form": form})


def openai_play_list(request):
    print("openai_play_list:")
    context = {}
    # play_list=OpenAIPlay.objects.order_by("-create_date")[:50],  # :5 limits the results to the five most recent
    context["play_list"] = OpenAIPlay.objects.all().order_by("-create_date")
    # context["play_list",play_list]

    return render(request, "hello/openai_play_list.html", context)


def openai_play_detail(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = OpenAIPlay.objects.get(id=id)

    return render(request, "hello/openai_play_detail.html", context)


def openai_play_delete(request, id):
    if not validate_login(request):
        return HttpResponseRedirect("/login")
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(OpenAIPlay, id=id)
    context["data"] = obj

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/openai/play_list")

    return render(request, "hello/openai_play_delete.html", context)

def validate_login(request):
    try:
        if request.session['user_id'] is not None: 
            return True 
    except KeyError: 
        pass
    return False 

def login(request):
    form = LoginForm(request.POST or None)
    context = {}  
    if request.method == "POST":
        try:
            if request.POST['username'] == "admin" and request.POST['password'] == "admin123":
                request.session['user_id'] = 123
                return HttpResponseRedirect('/')

            m = User.objects.get(username=request.POST['username'])
            if m.password == request.POST['password']:
                request.session['user_id'] = m.id
                return HttpResponseRedirect('/')
        except  KeyError:
            context["error"] = "Your username and password didn't match."

    context["form"]=form 
    return render(request, "hello/login.html", context)

def logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return HttpResponseRedirect('/')

def log_message(request):
    form = LogMessageForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
        else:
            return render(request, "hello/log_message.html", {"form": form})
    else:
        return render(request, "hello/log_message.html", {"form": form})
