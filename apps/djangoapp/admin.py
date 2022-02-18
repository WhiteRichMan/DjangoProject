from datetime import datetime
from typing import Optional
from django.contrib import admin
from django.core.handlers.wsgi import WSGIRequest
from . models import Account
from . models import Group
from . models import Student
from . models import Professor

class AccountAdmin(admin.ModelAdmin):
    readonly_fields = ()

    def get_readonly_fields(
        self,
        request: WSGIRequest,
        obj: Optional[Account] = None
    ) -> tuple:


        if obj:
            return self.readonly_fields + ('description',)
        return self.readonly_fields

admin.site.register(
    Account,AccountAdmin
)


class GroupAdmin(admin.ModelAdmin):
    readonly_fields = ()


    def get_readonly_fields(
        self,
        request: WSGIRequest,
        obj: Optional[Account] = None
    ) -> tuple:
        if obj:
            return self.readonly_fields + ('name',)
        return self.readonly_fields



admin.site.register(
    Group, GroupAdmin
    )


class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ()
    STUDENT_MAX_AGE = 16

    list_filter = (
        'age',
        'gpa',
    )

    search_fields = (
            'account_full_name',
    )

    list_display = (
        'group',
        'age',
    )

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

admin.site.register(
    Student, StudentAdmin
    )


class ProfessorAdmin(admin.ModelAdmin):
    pass

admin.site.register(
    Professor, ProfessorAdmin
)
