# Generated by Django 4.2.3 on 2023-07-17 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('internetApp', '0007_rename_contract_pricebusiness_contract1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='internet_product',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
