# Generated by Django 4.2.3 on 2023-07-21 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internetApp', '0024_alter_reservation_reservation_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='reservation_phone',
            field=models.BigIntegerField(blank=True, max_length=16, null=True),
        ),
    ]