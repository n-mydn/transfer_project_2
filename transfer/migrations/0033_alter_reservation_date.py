# Generated by Django 4.2.1 on 2023-09-13 06:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0032_reservation_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(default=datetime.date(2023, 9, 13), verbose_name='Transfer Tarihi'),
        ),
    ]
