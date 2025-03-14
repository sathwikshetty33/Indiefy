# Generated by Django 5.1.1 on 2024-10-13 04:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_customuser_user_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sub_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.substate'),
        ),
        migrations.CreateModel(
            name='seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobileno', models.CharField(max_length=12)),
                ('adharno', models.CharField(max_length=16)),
                ('panno', models.CharField(max_length=20)),
                ('products', models.ManyToManyField(related_name='po', to='products.product')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.seller'),
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
