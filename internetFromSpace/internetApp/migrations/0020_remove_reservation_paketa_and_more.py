# Generated by Django 4.2.3 on 2023-07-19 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('internetApp', '0019_alter_reservation_paketa'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='paketa',
        ),
        migrations.AddField(
            model_name='reservation',
            name='reservation_paket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='internetApp.price'),
        ),
    ]
