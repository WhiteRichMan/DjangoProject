from datetime import (
    datetime,
)

from django.db import models
from django.db.models import (
    QuerySet,
)
from django.conf import settings
from django.contrib.auth.models import (
    User,
)
from django.core.exceptions import (
    ValidationError,
)

from abstracts.models import (
     DateTimeCustom,
)

from auths.models import CustomUser

class GroupQuerySet(QuerySet):

    HIGH_GPA_LEVEL = 4.0

    def get_students_with_high_gpa(self) -> QuerySet :
        return self.filter(
            gpa__gt = self.HIGH_GPA_LEVEL
        )

class Group(DateTimeCustom):
    NAME_MAX_LENGTH = 10

    name = models.CharField(
        verbose_name='имя',
        max_length=NAME_MAX_LENGTH
    )

    def __str__(self) -> str:
        return f'Группа: {self.name}'

    class Meta:
        ordering = (
            'id',
        )
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    objects = GroupQuerySet().as_manager()

class AccountQuerySet(QuerySet):



    def get_superusers(self) -> QuerySet :
        return self.filter(
            user__is_superuser = True
        )  

class Account(DateTimeCustom):
    FULL_NAME_MAX_LENGTH = 20

    CustomUser = models.OneToOneField(
        CustomUser,
        verbose_name='пользователь',
        on_delete=models.CASCADE
    )
    full_name = models.CharField(
        verbose_name='полное имя',
        max_length=FULL_NAME_MAX_LENGTH
    )
    description = models.TextField()

    def __str__(self) -> str:
        return f'Аккаунт: {self.user.id} / {self.full_name}'

    class Meta:
        ordering = (
            'full_name',
        )
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'

    objects = AccountQuerySet().as_manager()

class StudentQuerySet(QuerySet):
    ADULT_AGE = 18

    def get_adult_students(self) -> QuerySet:
        return self.filter(
            age__gte=self.ADULT_AGE
        )


class Student(DateTimeCustom):
    MAX_AGE = 27

    account = models.OneToOneField(
        Account,
        verbose_name='аккаунт',
        on_delete=models.CASCADE
    )
    group = models.ForeignKey(
        Group,
        verbose_name='группа',
        on_delete=models.PROTECT
    )
    age = models.IntegerField(
        verbose_name='Возраст студента',
    )
    gpa = models.FloatField(
        verbose_name='Среднее значение GPA'
    )
    objects = StudentQuerySet().as_manager()

    def __str__(self) -> str:
        return 'Студент: {0} / {1} / {2}'.format(
            self.account.full_name,
            self.age,
            self.gpa,
        )

    def save(
        self,
        *args: tuple,
        **kwargs: dict
    ) -> None:
    
        if self.age > self.MAX_AGE:
            # v1
            # self.age = self.MAX_AGE

            # v2
            raise ValidationError(
                f'Допустимый возраст: {self.MAX_AGE}'
            )
        super().save(*args, **kwargs)

    def delete(self) -> None:
        datetime_now: datetime = datetime.now()

        self.datetime_deleted = datetime_now

        self.save(
            update_fields=['datetime_deleted']
        )
        # NOTE: Actual thing that will be triggered
        #
        # super().delete()

    class Meta:
        ordering = (
            'gpa',
        )
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Professor(DateTimeCustom):
    FULL_NAME_MAX_LENGTH = 20
    TOPIC_MAX_LENGTH = 10

    TOPIC_JAVA = 'java'
    TOPIC_PYTHON = 'python'
    TOPIC_TS = 'typescript'
    TOPIC_JS = 'javascript'
    TOPIC_RUBY = 'ruby'
    TOPIC_GO = 'golang'
    TOPIC_SQL = 'sql'
    TOPIC_SWIFT = 'swift'
    TOPIC_PHP = 'php'
    TOPIC_DELPHI = 'deplhi'
    TOPIC_PERL = 'perl'

    TOPIC_CHOICES = (
        (TOPIC_JAVA, 'Java'),
        (TOPIC_PYTHON, 'Python'),
        (TOPIC_TS, 'TypeScript'),
        (TOPIC_JS, 'JavaScript'),
        (TOPIC_RUBY, 'Ruby'),
        (TOPIC_GO, 'GoLang'),
        (TOPIC_SQL, 'SQL'),
        (TOPIC_SWIFT, 'Swift'),
        (TOPIC_PHP, 'PHP'),
        (TOPIC_DELPHI, 'Deplhi'),
        (TOPIC_PERL, 'Perl'),
    )

    full_name = models.CharField(
        verbose_name='полное имя',
        max_length=FULL_NAME_MAX_LENGTH
    )
    topic = models.CharField(
        verbose_name='предмет',
        max_length=TOPIC_MAX_LENGTH,
        choices=TOPIC_CHOICES,
        default=TOPIC_JAVA
    )
    students = models.ManyToManyField(
        Student
    )

    def __str__(self) -> str:
        return f'Профессор: {self.full_name} / Топик: {self.topic}'

    def save(self, *args: tuple, **kwargs: dict) -> None:
        super().save(*args, **kwargs)

    class Meta:
        ordering = (
            'topic',
        )
        verbose_name = 'Профессор'
        verbose_name_plural = 'Профессоры'