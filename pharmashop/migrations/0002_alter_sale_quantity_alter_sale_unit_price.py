# Generated by Django 4.1.7 on 2023-04-04 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmashop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='quantity',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='sale',
            name='unit_price',
            field=models.IntegerField(blank=True, max_length=50, null=True),
        ),
    ]
