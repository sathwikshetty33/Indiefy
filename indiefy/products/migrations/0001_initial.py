# Generated by Django 5.1.1 on 2024-09-21 11:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='not specified', max_length=100)),
                ('image', models.ImageField(null=True, upload_to='product_images/')),
                ('description', models.TextField(default='description')),
            ],
        ),
        migrations.CreateModel(
            name='StateCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='not specified', max_length=100)),
                ('image', models.ImageField(null=True, upload_to='product_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='not specified', max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images/')),
                ('product_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.producttype')),
                ('state_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.statecategory')),
            ],
        ),
    ]
