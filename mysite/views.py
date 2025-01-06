from django.shortcuts import HttpResponse, redirect
from django.contrib.auth import login

from django.shortcuts import render

from mysite.forms import RegisterForm


# Create your views here.

def index_view(request):
    return HttpResponse('Hello World')


def test_view(request):
    return render(request, 'base.html')


def signup_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('/')
    if request.POST:
        print(form.errors)

    return render(request, 'signup.html', {'form': form})
