from django.urls import (
    path,
    re_path,
)
from university import views

from university.views import (
    IndexView,
)


urlpatterns = [
    path('',                    views.index,     name='page_main'),
    path('show/<int:user_id>/', views.show,      name='page_show'),
    path('delete/',             views.delete,    name='page_delete'),
    path('about/',              views.about,     name='page_about'),
    path('primitive/',          views.primitive, name='page_primitive'),

    path('register/', views.register, name='page_register'),
    path('login/',    views.login,    name='page_login'),
    path('logout/',   views.logout,   name='page_logout'),
]
