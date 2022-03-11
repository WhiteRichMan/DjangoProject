from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
)
from auths.models import CustomUser
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
)
from django import forms


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = (
            'email',
        )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = (
            'email',
        )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = (
            'email',
        )


class CustomUserForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput
    )

    class Meta:
        model = CustomUser
        fields = (
            'email',
            'password',
        )
