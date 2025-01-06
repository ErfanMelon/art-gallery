from django.shortcuts import HttpResponse

from django.shortcuts import render

# Create your views here.

def index_view(request):
    return HttpResponse('Hello World')

def test_view(request):
    return render(request, 'base.html')