# Generated by Django 2.0.7 on 2018-07-10 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missions', '0003_auto_20180710_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='count_of_words',
            field=models.PositiveIntegerField(default=20),
        ),
        migrations.AlterField(
            model_name='mission',
            name='lang',
            field=models.TextField(default='ru'),
        ),
        migrations.AlterField(
            model_name='mission',
            name='mode',
            field=models.TextField(default='select'),
        ),
        migrations.AlterField(
            model_name='mission',
            name='result',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mission',
            name='step',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='mission',
            name='words',
            field=models.TextField(default='[{}]'),
        ),
    ]
