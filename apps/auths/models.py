from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.utils import timezone 

# class File():
#     title: str
#     file: obj

#     class Meta():
#         ordering = (
#             'datetime_deleted'
#         )
#         verbose_name = 'Homework'
#         verbose_name_plural = 'Homeworks'
# # 
# class Homework():
#     title: str 
#     subject: str
#     logo: img
#     is_checked: bool
#     class Meta():
#         ordering = (
#             'datetime_deleted'
#         )
#         verbose_name = 'File'
#         verbose_name_plural = 'Files'    

# Homework.objects.get_not_deleted()

# self.filter(datetime_deleted__isnull=True)

# is_deleted = BooleanField()

# self.filter(is_deleted=False)

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
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        ordering = (
            'date_joined',
        )
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
