# Generated by Django 3.2.2 on 2021-05-13 16:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 13, 16, 53, 13, 523084, tzinfo=utc), verbose_name='Fecha de publicacion'),
        ),
    ]
