# Generated by Django 3.1.3 on 2021-04-24 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0027_auto_20210423_1936'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bandera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, default='images/default.png', null=True, upload_to='images/')),
                ('name', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='bandera',
            field=models.ManyToManyField(related_name='products', to='tienda.Bandera'),
        ),
    ]
