# Generated by Django 4.2.15 on 2024-08-19 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_data_form', '0006_product_is_bidden'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_inspected',
            field=models.BooleanField(default=False),
        ),
    ]
