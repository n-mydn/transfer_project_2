# Generated by Django 4.2.1 on 2023-12-29 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0052_alter_car_max_people_alter_car_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='', verbose_name='Fotoğraf')),
            ],
        ),
        migrations.AlterField(
            model_name='reservation',
            name='time_of_return',
            field=models.TimeField(default='17:32', verbose_name='Dönüş Saati'),
        ),
    ]