from typing import Optional

from django.contrib import admin
from django.http import HttpRequest
from django.contrib.auth.admin import UserAdmin

from auths.models import (
    CustomUser,
)
from auths.forms import (
    CustomUserCreationForm,
    CustomUserChangeForm,
)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    # Форма - некая вспомогательная сущность между моделями
    # и как правило html, сериалайзерами и т.д
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = (
        (
            None, {
                'fields': (
                    'email', 'password',
                ),
            }
        ),
        (
            'Permissions', {
                'fields': ('is_active',)
            }
        ),
    )
    # for fields to be used in editing users
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': (
                    'email', 'password1', 'password2', 'is_active',
                ),
            }
        ),
    )
    # for fields to be used when creating a user
    list_display = ('email', 'is_active',)
    list_filter = ('email', 'is_active',)
    search_fields = ('email',)
    ordering = ('email',)
    

    def get_readonly_fields(self, request: HttpRequest,
                            obj: Optional[CustomUser] = None) -> tuple:
        if obj:
            return self.readonly_fields + (
                'email',
                'is_root',
                'is_staff',
                'datetime_joined',
            )
        return self.readonly_fields


admin.site.register(CustomUser, CustomUserAdmin)