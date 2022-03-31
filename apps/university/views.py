from django.db.models import QuerySet
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import (
    authenticate as dj_authenticate,
    login as dj_login,
    logout as dj_logout,
)

from abstracts.handlers import ViewHandler
from auths.forms import CustomUserForm
from auths.models import CustomUser
from university.models import Homework

from django.template import loader
from django.views import View
from django.views.generic.base import TemplateView

class IndexView(ViewHandler, View):

    queryset: QuerySet = \
        Homework.objects.get_not_deleted()
        

    def get(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs
    ) -> HttpResponse:

        if not request.user.is_authenticated:
            return render(
                request,
                'universty/login.html'
            )
    
        homeworks: QuerySet = self.queryset.filter(
            user=request.user
        )

        if not homeworks:
            homeworks = self.queryset

        template_name: str = 'university/index.html'
        # breakpoint()
        context: dict = {
            'ctx_title': 'Start Page',
            'ctx_homeworks': homeworks,
        }

        return self.get_http_response(
            request,
            template_name,
            context
        )

        return HttpResponse('Hello, World!')

# class CreateHomeworkView(view)

class AdminView(ViewHandler, View):

    def get(self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs
        ) -> HttpResponse:

        context: dict = {
            'ctx_title': 'Главная страница',
            'ctx_users': CustomUser.objects.all(),
            }
        template_name = loader.get_template(
            'universty/admin.html'
        )
        return HttpResponse(
            template_name.render(
                context, request
            ),
            content_type='text/html'
        )
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

class ShowView(ViewHandler, View):

    def get(self,
        request: WSGIRequest,
        user_id: str,
        *args: tuple,
        **kwargs
        ) -> HttpResponse:

        homework_id: int = kwargs.get('homework_id', 0)
        user = CustomUser.objects.get(id=user_id)

        context: dict = {
            'ctx_title': 'Профиль пользователя',
            'ctx_user': user,
            }

        template_name = loader.get_template(
            'universty/show.html'
        )

        return HttpResponse(
            template_name.render(
                context, request
            ),

            content_type='text/html'
        )

# def show(request: WSGIRequest, pk: int) -> HttpResponse:
#     user: CustomUser = CustomUser.objects.get(
#         id=pk
#     )
#     context: dict = {
#         'ctx_title': 'Профиль пользователя',
#         'ctx_user': user,
#     }
#     return render(
#         request,
#         template_name='university/profile.html',
#         context=context
#     )

class DeleteView(ViewHandler, View):

    def get(self,
        request: WSGIRequest,
        user_id: str,
        *args: tuple,
        **kwargs
        ) -> HttpResponse:

        return HttpResponse(
            template_name.render(
                context, request
            ),

            content_type='text/html'
        )

class AboutView(ViewHandler, View):
    
    def get(self,
        request: WSGIRequest,
        user_id: str,
        *args: tuple,
        **kwargs
        ) -> HttpResponse:

        template_name = loader.get_template(
            'universty/about.html'
        )

        return HttpResponse(
            template_name.render(
                context, request
            ),

            content_type='text/html'
        )
    

class PrimitiveView(ViewHandler, View):

    def get(self,
        request: WSGIRequest,
        user_id: str,
        *args: tuple,
        **kwargs
        ) -> HttpResponse:


        return HttpResponse(
            template_name.render(
                context, request
            ),

            content_type='text/html'
        )

class LogoutView(ViewHandler, View):

        def get(self,
        request: WSGIRequest,
        user_id: str,
        *args: tuple,
        **kwargs
        ) -> HttpResponse:
        
            form: CustomUserForm = CustomUserForm(
            request.POST
            )   

            context: dict = {
                'form': form,
            }

            return HttpResponse(
                template_name.render(
                    context, request
                ),

                content_type='text/html'
                )

class LoginView(ViewHandler, View):

    def get(self,
        request: WSGIRequest,
        user_id: str,
        *args: tuple,
        **kwargs
        ) -> HttpResponse:

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

            template_name = loader.get_template(
            'universty/login.html'
        )

        return self.get_http_response(
            request,
            template_name,
            context
        )

        return HttpResponse('Hello, World!')



class RegisterView(ViewHandler, View):

    def post(self,
        request: WSGIRequest,
        user_id: str,
        *args: tuple,
        **kwargs
        ) -> HttpResponse:

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

        template_name = loader.get_template(
            'universty/register.html'
        )

        return self.get_http_response(
            request,
            template_name,
            context
        )

