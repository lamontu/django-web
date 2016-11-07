from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


def first_page(request):
    return HttpResponse("<h1>users login</h1>")


def user_login(request):
    if request.POST:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            e_name = form.cleaned_data["username"]
            e_word = form.cleaned_data["password"]
            user = authenticate(username=e_name, password=e_word)
            if user is not None:
                login(request, user)
                return redirect("/")

    form = AuthenticationForm()
    ctx = {}
    ctx['form'] = form
    return render(request, "login.html", ctx)


def user_logout(request):
    logout(request)
    return redirect("/")


'''
def diff_response(request):
    if request.user.is_authenticated():
        content = "<p>my dear user</p>"
    else:
        content = "<p>you wired stranger</p>"
    return HttpResponse(content)
'''

   
@login_required
def user_only(request):
    return HttpResponse("<p>This message is for logged in user only.</p>")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
        return redirect("/")
    else:
        form = UserCreationForm()
        ctx = {'form': form}
        return render(request, "register.html", ctx)
 

