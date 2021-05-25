# Generated by Django 3.2.3 on 2021-05-25 12:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('room', '0002_auto_20210525_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='likes',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='room',
            name='air_conditioning',
            field=models.BooleanField(verbose_name='есть кондиционер?'),
        ),
        migrations.AlterField(
            model_name='room',
            name='refrigerator',
            field=models.BooleanField(verbose_name='есть холодильник?'),
        ),
    ]