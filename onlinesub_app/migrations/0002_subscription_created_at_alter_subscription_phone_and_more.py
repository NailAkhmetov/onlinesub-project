# Generated by Django 5.1.2 on 2024-10-27 20:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinesub_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата и время публикации'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='phone',
            field=models.CharField(max_length=50, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='сomponents',
            field=models.TextField(verbose_name='Составляющие'),
        ),
    ]
