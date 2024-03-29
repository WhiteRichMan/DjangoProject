# Generated by Django 3.0 on 2022-02-11 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, default='2022-11-02', verbose_name='время создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='datetime_delited',
            field=models.DateTimeField(blank=True, null=True, verbose_name='время удаления'),
        ),
        migrations.AddField(
            model_name='group',
            name='datetime_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='время обновления'),
        ),
    ]
