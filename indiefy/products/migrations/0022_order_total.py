# Generated by Django 5.1.1 on 2024-10-20 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_order_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.IntegerField(default=100),
        ),
    ]
