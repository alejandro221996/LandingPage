# Generated by Django 3.2.2 on 2021-05-13 16:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 13, 16, 46, 5, 339567, tzinfo=utc), verbose_name='Fecha de publicacion'),
        ),
    ]
