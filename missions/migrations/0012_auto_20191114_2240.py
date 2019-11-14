# Generated by Django 2.2.7 on 2019-11-14 19:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missions', '0011_auto_20191114_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='finish_time',
            field=models.DateTimeField(default=datetime.datetime(2999, 1, 1, 0, 0), null=True, verbose_name='finish_time'),
        ),
        migrations.AlterField(
            model_name='mission',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 1, 0, 0), null=True, verbose_name='start_time'),
        ),
    ]
