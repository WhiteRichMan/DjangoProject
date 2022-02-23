
from . import views
from django.conf import settings
from django.urls import path, include 


urlpatterns = [
    path("admin/", views.admin),
    path('__debug__/', include('debug_toolbar.urls')),
]