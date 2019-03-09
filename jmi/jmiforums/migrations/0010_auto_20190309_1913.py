# Generated by Django 2.1.7 on 2019-03-09 19:13

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jmiforums', '0009_auto_20190309_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('ans_id', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('ans_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('comment_text', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='moderator',
            name='id',
        ),
        migrations.RemoveField(
            model_name='question',
            name='id',
        ),
        migrations.RemoveField(
            model_name='subforum',
            name='arti_count',
        ),
        migrations.RemoveField(
            model_name='subforum',
            name='id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AddField(
            model_name='moderator',
            name='mod_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='moderator',
            name='subforum_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='moderatorOf', to='jmiforums.Subforum'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='ques_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='subforum',
            name='subforum_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='user',
            name='user_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='moderator',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 9, 19, 13, 17, 891738, tzinfo=utc), verbose_name='Created on'),
        ),
        migrations.AlterField(
            model_name='question',
            name='subforum_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subforum_question', to='jmiforums.Subforum'),
        ),
        migrations.AlterField(
            model_name='question',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_question', to='jmiforums.User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 9, 19, 13, 17, 892531, tzinfo=utc), verbose_name='Created on'),
        ),
        migrations.AddField(
            model_name='comment',
            name='subforum_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subforum_comment', to='jmiforums.Subforum'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comment', to='jmiforums.User'),
        ),
        migrations.AddField(
            model_name='answer',
            name='subforum_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subforum_answer', to='jmiforums.Subforum'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_answer', to='jmiforums.User'),
        ),
    ]
