# Generated by Django 2.1.5 on 2019-02-14 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0068_rack_new_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='asset_tag',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='name',
            field=models.CharField(blank=True, max_length=64, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='asset_tag',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='rack',
            name='asset_tag',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='rack',
            name='facility_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
