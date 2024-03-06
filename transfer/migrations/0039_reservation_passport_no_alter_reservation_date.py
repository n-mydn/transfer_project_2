# Generated by Django 4.2.1 on 2023-11-04 09:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0038_popular_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='passport_no',
            field=models.CharField(default='', max_length=15, verbose_name='Pasaport Numarası'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(default=datetime.date(2023, 11, 4), verbose_name='Transfer Tarihi'),
        ),
    ]