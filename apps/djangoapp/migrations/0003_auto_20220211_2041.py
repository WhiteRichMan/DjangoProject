# Generated by Django 3.0 on 2022-02-11 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0002_auto_20220211_1926'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='datetime_created',
        ),
        migrations.RemoveField(
            model_name='group',
            name='datetime_delited',
        ),
        migrations.RemoveField(
            model_name='group',
            name='datetime_updated',
        ),
    ]