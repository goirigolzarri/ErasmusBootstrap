# Generated by Django 3.1.3 on 2021-06-28 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0033_auto_20210628_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stock_virtual',
        ),
    ]