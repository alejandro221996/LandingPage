# Generated by Django 3.2.2 on 2021-05-13 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Terapias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre_Paciente')),
                ('lastname', models.CharField(max_length=200, verbose_name='Apellido')),
                ('content', models.TextField(verbose_name='Analisis')),
                ('image', models.ImageField(upload_to='Terapias', verbose_name='Imagen_Paciente')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'terapia',
                'verbose_name_plural': 'terapias',
                'ordering': ['-created'],
            },
        ),
    ]