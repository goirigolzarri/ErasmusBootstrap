# Generated by Django 3.1.3 on 2021-04-23 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0023_auto_20210414_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='bandera',
        ),
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.RemoveField(
            model_name='product',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='product',
            name='talla',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='bandera',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='color',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='fecha',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='talla',
            field=models.CharField(choices=[('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], default='', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='colores',
            field=models.ManyToManyField(related_name='products', to='tienda.ColorProducto'),
        ),
    ]
