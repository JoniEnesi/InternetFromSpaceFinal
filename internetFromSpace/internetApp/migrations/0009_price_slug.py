# Generated by Django 4.2.3 on 2023-07-17 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internetApp', '0008_remove_price_internet_product_delete_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='slug',
            field=models.SlugField(blank=True, max_length=60, null=True),
        ),
    ]
