# Generated by Django 2.1.1 on 2018-09-16 15:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OutputSentiment', '0002_auto_20180916_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
