from django.shortcuts import render
from django.http import HttpResponse
from django.apps import AppConfig
from django.core.handlers.wsgi import WSGIRequest
from djangoapp.models import Student
from djangoapp.models import Account
from djangoapp.models import User


def index(request: WSGIRequest) -> HttpResponse:
    """Search First User."""
    
    user: User = User.objects.first()
    name: str = user.first_name

    account: Account = user.account
    name_account: str = account.full_name

    student: Student = account.student
    gpa: int = student.gpa

    text: str=f'<h1>Name:{name}<br>account:{name_account}<br> GPA:{gpa}</h1>'

    response: HttpResponse = HttpResponse(text)

    return response    


def index_html(request: WSGIRequest) -> HttpResponse:
    """Test html Page"""
    return HttpResponse(
        '<h1>Start Page</h1>'
    )