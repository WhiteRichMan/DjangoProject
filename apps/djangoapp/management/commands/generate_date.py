import random
from typing import Any 
from datetime import datetime 

from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth.models import (User,)

from djangoapp.models import (
    Group,
    Account,
    Student,
    Professor,
)

class Command(BaseCommand):

    help = 'Custom command for filing up database'

    def __init__(self, *args: tuple, **kwargs: dict) -> None:
        pass

    def _generate_groups(self)-> None:
        """Generate Group objs"""
        def generate_name(i: int) -> str :
            return f'Группа{inc}' 

        inc : int
        for inc in range(20):
            name: str = generate_name(inc)
            Group.objects.create(
                name=name
            )

    
    def handle(self, *args: tuple, **kwargs: dict) -> None:
        """Handles data filling."""

        start: datetime = datetime.now()

        self._generate_groups()

        print(
            'Generating Data: {} seconds'.format(
                (datetime.now()-start).total_seconds()
            )
        )