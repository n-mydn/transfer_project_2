# Generated by Django 4.2.1 on 2023-09-12 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0031_reservation_another_traveller'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='no',
            field=models.CharField(default=' ', max_length=200, verbose_name='Rezervasyon No'),
        ),
    ]
