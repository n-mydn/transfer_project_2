# Generated by Django 4.2.1 on 2023-08-26 10:05

import datetime
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0018_alter_car_currency_alter_car_currency_de_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='currency_de',
        ),
        migrations.RemoveField(
            model_name='car',
            name='currency_en',
        ),
        migrations.RemoveField(
            model_name='car',
            name='currency_tr',
        ),
        migrations.RemoveField(
            model_name='car',
            name='price_de',
        ),
        migrations.RemoveField(
            model_name='car',
            name='price_en',
        ),
        migrations.RemoveField(
            model_name='car',
            name='price_tr',
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_surname', models.CharField(max_length=100, verbose_name='Ad-Soyad')),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Telefon Numarası')),
                ('email', models.EmailField(max_length=254, verbose_name='E-Posta')),
                ('date', models.DateField(default=datetime.date(2023, 8, 26), verbose_name='Transfer Tarihi')),
                ('planetime', models.TimeField(verbose_name='Uçak İniş Zamanı')),
                ('flightnumber', models.CharField(max_length=20, verbose_name='Uçuş Numarası')),
                ('anothername', models.TextField(verbose_name='Diğer Yolcular')),
                ('specialrequest', models.TextField(blank=True, null=True, verbose_name='Transferle ilgili özel isteğinizi bu bölüme yazınız:')),
                ('messages', models.CharField(blank=True, max_length=200, null=True, verbose_name='Karşılama Mesajı')),
                ('extras', models.TextField(verbose_name='Ekstralar')),
                ('IdCar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transfer.car', verbose_name='Car')),
            ],
        ),
    ]