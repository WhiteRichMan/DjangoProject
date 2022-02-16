
from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('index_html/', views.index_html)
]