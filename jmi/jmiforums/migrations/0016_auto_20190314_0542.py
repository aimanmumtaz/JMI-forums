# Generated by Django 2.1.7 on 2019-03-14 05:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jmiforums', '0015_auto_20190314_0540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moderator',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 14, 5, 42, 21, 605106, tzinfo=utc), verbose_name='Created on'),
        ),
        migrations.AlterField(
            model_name='user',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 14, 5, 42, 21, 607308, tzinfo=utc), verbose_name='Created on'),
        ),
    ]