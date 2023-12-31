# Generated by Django 4.2.3 on 2023-07-17 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internetApp', '0005_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_title', models.CharField(blank=True, max_length=60, null=True)),
                ('product_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('product_setupCost', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='price',
            name='internet_product',
            field=models.ManyToManyField(to='internetApp.product'),
        ),
    ]
