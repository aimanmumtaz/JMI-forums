# Generated by Django 2.1.7 on 2019-02-21 10:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jmiforums', '0004_moderator_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moderator',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 21, 10, 2, 59, 743023, tzinfo=utc), verbose_name='Created on'),
        ),
    ]
