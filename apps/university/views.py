from django.db.models import QuerySet
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import (
    authenticate as dj_authenticate,
    login as dj_login,
    logout as dj_logout,
)
from auths.forms import CustomUserForm
from auths.models import CustomUser
from university.models import Homework

from django.template import loader
from django.views import View
from django.views.generic.base import TemplateView

class IndexView(View):

    template_name = 'universty/login.html'
    queryset = Homework.objects.get_not_deleted()


    def get(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs
    ):
        return HttpResponse('Hello, World!')

class AdminView(View):

    template_name = 'universty/admin.html'
    
    def get(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs
    ):
        return HttpResponse('Admin Page')


# def index(request: WSGIRequest) -> HttpResponse:
#     if not request.user.is_authenticated:
#         return render(
#             request,
#             'university/login.html'
#         )

#     homeworks: QuerySet = Homework.objects.filter(
#         user=request.user
#     )
#     context: dict = {
#         'ctx_title': 'Главная страница',
#         'ctx_homeworks': homeworks,
#     }
#     return render(
#         request,
#         template_name='university/index.html',
#         context=context
#     )

class ShowView(View):

    template_name = 'universty/profile.html'
    queryset = CustomUser.objects.get(id=pk)
 

    def get(
        
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs
        
    ):
        return HttpResponse('Show Page')

def show(request: WSGIRequest, pk: int) -> HttpResponse:
    user: CustomUser = CustomUser.objects.get(
        id=pk
    )
    context: dict = {
        'ctx_title': 'Профиль пользователя',
        'ctx_user': user,
    }
    return render(
        request,
        template_name='university/profile.html',
        context=context
    )


def delete(request: WSGIRequest) -> HttpResponse:
    pass


def about(request: WSGIRequest) -> HttpResponse:
    return render(
        request,
        template_name='university/about.html'
    )


def primitive(request: WSGIRequest) -> HttpResponse:
    return HttpResponse(
        '<h1>Примитивная страница</h1>'
    )


def logout(request: WSGIRequest) -> HttpResponse:

    dj_logout(request)

    form: CustomUserForm = CustomUserForm(
        request.POST
    )
    context: dict = {
        'form': form,
    }
    return render(
        request,
        'university/login.html',
        context
    )


def login(request: WSGIRequest) -> HttpResponse:

    if request.method == 'POST':
        email: str = request.POST['email']
        password: str = request.POST['password']

        user: CustomUser = dj_authenticate(
            email=email,
            password=password
        )
        if not user:
            return render(
                request,
                'university/login.html',
                {'error_message': 'Неверные данные'}
            )
        if not user.is_active:
            return render(
                request,
                'university/login.html',
                {'error_message': 'Ваш аккаунт был удален'}
            )
        dj_login(request, user)

        homeworks: QuerySet = Homework.objects.filter(
            user=request.user
        )
        return render(
            request,
            'university/index.html',
            {'homeworks': homeworks}
        )
    return render(
        request,
        'university/login.html'
    )


def register(request: WSGIRequest) -> HttpResponse:

    form: CustomUserForm = CustomUserForm(
        request.POST
    )
    if not form.is_valid():
        context: dict = {
            'form': form
        }
        return render(
            request,
            'university/register.html',
            context
        )
    user: CustomUser = form.save(
        commit=False
    )
    email: str = form.cleaned_data['email']
    password: str = form.cleaned_data['password']
    user.email = email
    user.set_password(password)
    user.save()

    user: CustomUser = dj_authenticate(
        email=email,
        password=password
    )
    if user and user.is_active:

        dj_login(request, user)

        homeworks: QuerySet = Homework.objects.filter(
            user=request.user
        )
        return render(
            request,
            'university/index.html',
            {'homeworks': homeworks}
        )
