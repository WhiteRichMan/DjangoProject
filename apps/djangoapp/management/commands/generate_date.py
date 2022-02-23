import names
import random
from typing import Any
from datetime import datetime


from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth.models import (User,)
from django.contrib.auth.hashers import make_password

from djangoapp.models import (
    Group,
    Account,
    Student,
    Professor,
)

TOTAL_USER_ACCOUNT = 500


class Command(BaseCommand):

    help = 'Custom command for filing up database'

    def __init__(self, *args: tuple, **kwargs: dict) -> None:
        pass

    def _generate_groups(self) -> None:
        """Generate Group objs"""
        def generate_name(i: int) -> str:
            return f'Группа{inc}'

        inc: int
        for inc in range(20):
            name: str = generate_name(inc)
            Group.objects.create(
                name=name
            )

    def _generate_users(self) -> None:
        """Generating User objects"""

        super_users: int = User.objects.filter(is_superuser="True")

        if super_users.count() <= 1:
            User.objects.create(
                is_superuser=True,
                is_staff=True,
                username='Ryslan',
                email='Ryslanovka@gmail.com',
                password='donthavepassword',
                first_name='Руслан',
                last_name='Загидуллин',
            )
        elif super_users.count() >= 2:
            print('Superuser quantity is limited')

    def _generate_accounts(self) -> None:

        _email_patterns: tuple = (
            '@gmail.com', '@outlook.com', '@yahoo.com',
            '@inbox.ru', '@inbox.ua', '@inbox.kz',
            '@yandex.ru', '@yandex.ua', '@yandex.kz',
            '@mail.ru', '@mail.ua', '@mail.kz',
        )

        for _ in range(TOTAL_USER_ACCOUNT):
            user_password: str = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
            user_first_name: str = names.get_first_name()
            user_last_name: str = names.get_last_name()
            User.objects.create(
                is_superuser=False,
                first_name=user_first_name,
                last_name=user_last_name,
                password=make_password(user_password),
                username=f'{user_first_name.lower()}{user_last_name.lower()}',
                email=f'{user_first_name.lower()}.{user_last_name.lower()}{random.choice(_email_patterns)}'
            )

    def handle(self, *args: tuple, **kwargs: dict) -> None:
        """Handles data filling."""

        start: datetime = datetime.now()

        self._generate_groups()
        self._generate_users()
        self._generate_accounts()

        print(
            'Generating Data: {} seconds'.format(
                (datetime.now()-start).total_seconds()
            )
        )
