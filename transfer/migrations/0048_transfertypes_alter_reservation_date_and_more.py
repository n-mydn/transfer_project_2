# Generated by Django 4.2.1 on 2023-11-10 10:21

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0047_homepagearticletwo_alter_reservation_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransferTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Başlık')),
                ('title_tr', models.CharField(max_length=200, null=True, verbose_name='Başlık')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='Başlık')),
                ('title_de', models.CharField(max_length=200, null=True, verbose_name='Başlık')),
                ('content', ckeditor.fields.RichTextField(verbose_name='İçerik')),
                ('content_tr', ckeditor.fields.RichTextField(null=True, verbose_name='İçerik')),
                ('content_en', ckeditor.fields.RichTextField(null=True, verbose_name='İçerik')),
                ('content_de', ckeditor.fields.RichTextField(null=True, verbose_name='İçerik')),
            ],
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(default=datetime.date(2023, 11, 10), verbose_name='Transfer Tarihi'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='date_of_return',
            field=models.DateField(default=datetime.date(2023, 11, 10), verbose_name='Dönüş Tarihi'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='time_of_return',
            field=models.TimeField(default='13:21', verbose_name='Dönüş Saati'),
        ),
    ]
