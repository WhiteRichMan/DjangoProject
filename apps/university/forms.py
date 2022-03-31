from django.db.models import QuerySet
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render

from abstracts.handlers import ViewHandler
from auths.forms import CustomUserForm
from auths.models import CustomUser
from university.models import Homework

from django.template import loader
from django.views import View
from django.views.generic.base import TemplateView

class HomeworkView(ViewHandler, View):

    def get(self,
        request: WSGIRequest,
        user_id: str,
        *args: tuple,
        **kwargs
        ) -> HttpResponse:

            user = models.ForeignKey(
        CustomUser, on_delete=models.PROTECT
    )
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    logo = models.ImageField(
        'Лого домашней работы',
        upload_to='homework/',
        max_length=255
    )
    is_checked = models.BooleanField(default=False)

    objects = HomeworkQuerySet().as_manager()

    def __str__(self) -> str:
        return f'{self.subject} | {self.title}'

        homeworks: QuerySet = Homework.objects.filter(
                user=request.user
            )

        template_name = loader.get_template(
        'universty/homework.html' )