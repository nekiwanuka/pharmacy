# Generated by Django 4.1.7 on 2023-04-04 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmashop', '0002_alter_sale_quantity_alter_sale_unit_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='unit_price',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
