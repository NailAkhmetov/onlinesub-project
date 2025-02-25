# Generated by Django 5.1.2 on 2024-10-27 23:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinesub_app', '0004_remove_subscription_image_spotify_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('image', models.URLField(blank=True, max_length=255, null=True, verbose_name='Ссылка на изображение')),
                ('discription', models.TextField(verbose_name='Описание гайда')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата и время публикации')),
            ],
            options={
                'verbose_name': 'Гайд',
                'verbose_name_plural': 'Гайды',
            },
        ),
        migrations.AlterField(
            model_name='subscription',
            name='phone',
            field=models.CharField(max_length=100, verbose_name='Телефон'),
        ),
    ]
