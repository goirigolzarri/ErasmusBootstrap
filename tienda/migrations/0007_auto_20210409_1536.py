# Generated by Django 3.1.3 on 2021-04-09 13:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tienda', '0006_pedido_complete'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Producto',
            new_name='Product',
        ),
        migrations.RenameModel(
            old_name='ProductoPedido',
            new_name='OrderItem',
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False, null=True)),
                ('transaction_id', models.CharField(max_length=200, null=True)),
                ('pedido_de', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='direccionenvio',
            name='pedido',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tienda.order'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='pedido',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tienda.order'),
        ),
        migrations.DeleteModel(
            name='Pedido',
        ),
    ]
