from django.db.models import QuerySet
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.contrib.auth.models import User

from django.shortcuts import render

from auths.models import CustomUser
from auths.forms import CustomUserForm
from django.contrib.auth import (
    authenticate as dj_authenticate,
    login as dj_login,
    logout as dj_logout,
)

from djangoapp.models import (
    Group,
    Student,
    Professor,
)


# def shablon(request: WSGIRequest) -> HttpResponse:
#     """Searh first user"""

#     student: Student = Student.objects.first()
#     gpa: int = student.gpa
    
#     account: CustomUser = student.account
#     name_acc: str = account.full_name

#     CustomUser: CustomUser = account.user
#     name: str = CustomUser.first_name

#     text: str = f'''<h1>Username: {name}<br> Account: {name_acc}<br>
#                         GPA: {gpa}</h1>
#                  '''

#     response: HttpResponse = HttpResponse(text)
#     return response

def index_2(request: WSGIRequest) -> HttpResponse:
    return HttpResponse(
        '<h1>Page: Start</h1>'
    )

def index(request: WSGIRequest) -> HttpResponse:
    users: QuerySet = CustomUser.objects.all()
    context: dict = {
        'ctx_title': 'Главная страница',
        'ctx_users': users,
    }
    return render(
        request,
        'index.html',
        context,
    )
def admin(request: WSGIRequest) -> HttpResponse:
    context: dict = {
        'ctx_title': 'Главная страница',
        'ctx_users': CustomUser.objects.all(),
    }
    
    return render(
        request,
        'admin.html',
        context
    )
def show(request: WSGIRequest, user_id: str) -> HttpResponse:
    CustomUser = CustomUser.objects.get(id=user_id)
    context: dict = {
        'ctx_title': 'Профиль пользователя',
        'ctx_user': user,
    }
    return render(
        request,
        'show.html',
        context
    )
def delete(request: WSGIRequest) -> HttpResponse:

 return HttpResponse(
        '<h1>Page: Delete</h1>'
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
        'djangoapp/login.html',
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
        # Guard Clause
        #
        if not user:
            return render(
                request,
                'university/login.html',
                {'error_message': 'Невереные данные'}
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
            'djangoapp/index.html',
            {'homeworks': homeworks}
        )
    return render(
        request,
        'djangoapp/login.html'
    )

def register(request: WSGIRequest) -> HttpResponse:

    form: CustomUserForm = CustomUserForm(
        request.POST
    )
    if form.is_valid():
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
                'djangoapp/index.html',
                {'homeworks': homeworks}
            )
    context: dict = {
        'form': form
    }
    return render(
        request,
        'djangoapp/register.html',
        context
    )