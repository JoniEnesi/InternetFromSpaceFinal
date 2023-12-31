# Generated by Django 4.2.3 on 2023-07-17 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('internetApp', '0006_product_price_internet_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pricebusiness',
            old_name='contract',
            new_name='contract1',
        ),
        migrations.RenameField(
            model_name='pricebusiness',
            old_name='data_cap',
            new_name='data1_cap',
        ),
        migrations.RenameField(
            model_name='pricebusiness',
            old_name='download_speed',
            new_name='download1_speed',
        ),
        migrations.RenameField(
            model_name='pricebusiness',
            old_name='internet_id',
            new_name='internet1_id',
        ),
        migrations.RenameField(
            model_name='pricebusiness',
            old_name='internet_model',
            new_name='internet1_model',
        ),
        migrations.RenameField(
            model_name='pricebusiness',
            old_name='internet_price',
            new_name='internet1_price',
        ),
        migrations.RenameField(
            model_name='pricebusiness',
            old_name='internet_title',
            new_name='internet1_title',
        ),
        migrations.RenameField(
            model_name='pricebusiness',
            old_name='setup_cost',
            new_name='setup1_cost',
        ),
        migrations.RenameField(
            model_name='pricebusiness',
            old_name='upload_speed',
            new_name='upload1_speed',
        ),
    ]
