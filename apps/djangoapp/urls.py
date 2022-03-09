from . import views

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path(
        '',
         views.index
    ),
    path(
        'admin/',
         views.admin
    ),
    path(
        'show/<int:user_id>/', 
        views.show,
        name='page_show'
    ),
    path(
        'delete',
        views.delete, 
        name='page_delete'
    )
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)