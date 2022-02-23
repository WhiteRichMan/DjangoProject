from wsgiref.simple_server import WSGIRequestHandler
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    return(HttpResponse('<h1>Hello World</h1>'))

def admin(request) -> HttpResponse:
    return render(
        request,
        "index.html",
        context={"users":User.objects.all()}
    )