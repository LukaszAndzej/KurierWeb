# Generated by Django 5.1.5 on 2025-01-24 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_remove_parcel_current_lat_remove_parcel_current_lng_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='parcel',
            name='current_lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='parcel',
            name='current_lng',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
