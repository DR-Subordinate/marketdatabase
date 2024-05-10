# Generated by Django 4.2.13 on 2024-05-10 09:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_data_form', '0004_market_remove_product_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='market',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 5, 10, 9, 31, 58, 732526, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='market',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
