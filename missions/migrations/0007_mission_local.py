# Generated by Django 2.2 on 2020-07-14 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missions', '0006_auto_20191114_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='mission',
            name='local',
            field=models.BooleanField(default=False),
        ),
    ]
