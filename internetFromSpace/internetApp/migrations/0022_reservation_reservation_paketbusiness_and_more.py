# Generated by Django 4.2.3 on 2023-07-19 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('internetApp', '0021_alter_reservation_reservation_paket'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='reservation_paketBusiness',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='internetApp.pricebusiness'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reservation_paket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='internetApp.price'),
        ),
    ]
