# Generated by Django 3.1.3 on 2021-04-14 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0021_auto_20210414_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pedido_de',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='tienda.customer'),
        ),
    ]