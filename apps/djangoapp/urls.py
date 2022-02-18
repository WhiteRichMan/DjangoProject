
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index_html_test),
    path('index_html/', views.index_html)
]