# Generated by Django 4.2.3 on 2023-07-26 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internetApp', '0029_remove_reservation_is_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]
