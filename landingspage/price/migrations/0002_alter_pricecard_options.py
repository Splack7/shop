# Generated by Django 4.1.4 on 2023-02-20 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pricecard',
            options={'verbose_name': 'Цена', 'verbose_name_plural': 'Цены'},
        ),
    ]
