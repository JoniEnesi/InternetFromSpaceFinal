# Generated by Django 4.2.3 on 2023-07-18 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('internetApp', '0017_reservation_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='slug',
            new_name='paketa',
        ),
    ]
