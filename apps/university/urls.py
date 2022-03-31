from django.urls import (
    path,
    re_path,
)
from university import views

from university.views import (
    IndexView,
    ShowView,
    AdminView,
    DeleteView,
    AboutView,
    PrimitiveView,
    LoginView,
    RegisterView,
    LogoutView
)

from university.forms import (
    HomeworkView
)



urlpatterns = [
    path('',                    IndexView.as_view(),     name='page_main'),
    path('show/<int:user_id>/', ShowView.as_view(),      name='page_show'),
    path('delete/',             DeleteView.as_view(),    name='page_delete'),
    path('Admin/',              AdminView.as_view(),     name='page_admin'),
    path('about/',              AboutView.as_view(),     name='page_about'),
    path('Homework/',           HomeworkView.as_view(),  name='page_homework'),

    path('register/', RegisterView.as_view(), name='page_register'),
    path('login/',    LoginView.as_view(),    name='page_login'),
    path('logout/',   LogoutView.as_view(),   name='page_logout'),
]