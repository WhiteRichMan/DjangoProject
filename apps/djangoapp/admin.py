from typing import Optional

from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest
from auths.models import CustomUser
from abstracts.models import (
     DateTimeCustom,
)

from . models import (
    Group,
    Student,
    Professor,
    )


# class UserAdmin(admin.ModelAdmin):
    # redonly_fields = ()
    # user_fields = ('first_name', 'last_name', 'email', 
    #                     'username', 'is_active', 'is_staff',
    #                     'is_superuser', 'date_joined', 'last_login',)
                        
    # def get_readonly_fields(
    #     self,
    #     request: WSGIRequest,
    #     obj: Optional[User] = None
    # ) -> tuple:
    #     if obj:
    #         return self.readonly_fields + self.user_fields
    #     return self.readonly_fields


# class AccountAdmin(admin.ModelAdmin):
    # readonly_fields = (
    #     'datatime_created',
    #     'datatime_updated',
    #     'datatime_deleted',
    #     )

    # def get_readonly_fields(
    #     self,
    #     request: WSGIRequest,
    #     obj: Optional[Account] = None
    # ) -> tuple:
    #     if obj:
    #         return self.readonly_fields + ('description',)
    #     return self.readonly_fields


class GroupAdmin(admin.ModelAdmin):
    readonly_fields = (
        'datetime_created',
        'datetime_updated',
        'datetime_delited',
        )


class StudentAdmin(admin.ModelAdmin):
    readonly_fields = (
        'datetime_created',
        'datetime_updated',
        'datetime_delited',
        )
    list_filter = (
        'age',
        'gpa',
    )
    searh_filter = (
        'account__full_name',
    )
    list_display = (
        'age',
        'gpa',
    )
    STUDENT_MAX_AGE = 16

    def student_age_validation(
        self,
        obj: Optional[Student]
    ) -> tuple:
        if obj and obj.age <= self.STUDENT_MAX_AGE:
            return True
        return False

    def get_readonly_fields(
        self,
        request: WSGIRequest,
        obj: Optional[Student] = None
    ) -> tuple:

        result: bool = self.student_age_validation(obj)
        if result:
            return self.readonly_fields + ('age',)
        return self.readonly_fields


class ProfessorAdmin(admin.ModelAdmin):
    readonly_fields = (
        'datetime_created',
        'datetime_updated',
        'datetime_delited',
        )



admin.site.register(
    Group, GroupAdmin
    )

admin.site.register(
    Student, StudentAdmin
    )

admin.site.register(
    Professor, ProfessorAdmin
    )
