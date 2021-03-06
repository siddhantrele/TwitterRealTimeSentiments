# Generated by Django 2.1.1 on 2018-09-16 15:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=500)),
                ('sentiment', models.FloatField()),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
