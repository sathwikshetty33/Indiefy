# Generated by Django 5.1.1 on 2024-10-13 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_product_image_alter_product_seller_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='aunty1.jpg', null=True, upload_to='product_images/'),
        ),
    ]
