from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.utils import timezone
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError


class CustomUserManager(BaseUserManager):

    def create_user(
        self,
        email: str,
        password: str
    ) -> 'CustomUser':

        if not email:
            raise ValidationError('Email required')

        user: 'CustomUser' = self.model(
            email=self.normalize_email(email),
            password=password
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        email: str,
        password: str
    ) -> 'CustomUser':

        user: 'CustomUser' = self.model(
            email=self.normalize_email(email),
            password=password
        )
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        'Почта/Логин', unique=True
    )
    is_active = models.BooleanField('Активность', default=True)
    is_staff = models.BooleanField('Статус менеджера', default=False)
    date_joined = models.DateTimeField(
        'Дата регистрации', default=timezone.now
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        ordering = (
            'date_joined',
        )
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
