# Generated by Django 3.1.3 on 2021-04-14 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0022_auto_20210414_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pedido_de',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tienda.customer'),
        ),
    ]
