# Generated by Django 4.2.3 on 2023-07-18 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internetApp', '0015_remove_price_internet_product_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_name', models.CharField(blank=True, max_length=60, null=True)),
                ('reservation_lastname', models.CharField(blank=True, max_length=60, null=True)),
                ('reservation_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('reservation_phone', models.IntegerField(blank=True, null=True)),
                ('reservation_address', models.CharField(blank=True, max_length=100, null=True)),
                ('reservation_street', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
