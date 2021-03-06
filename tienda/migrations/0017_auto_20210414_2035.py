# Generated by Django 3.1.3 on 2021-04-14 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0016_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='user',
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='customer',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='tienda.customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pedido_de',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='tienda.customer'),
        ),
    ]
