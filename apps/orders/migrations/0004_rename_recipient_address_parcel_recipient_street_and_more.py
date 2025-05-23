# Generated by Django 5.1.5 on 2025-01-21 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_parcel_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='parcel',
            old_name='recipient_address',
            new_name='recipient_street',
        ),
        migrations.AddField(
            model_name='parcel',
            name='pickup_point',
            field=models.CharField(choices=[('KRAKOW_1', 'Punkt Kraków 1 - ul. Rynek Główny 1'), ('KRAKOW_2', 'Punkt Kraków 2 - ul. Floriańska 15'), ('KRAKOW_3', 'Punkt Kraków 3 - ul. Kazimierz 12')], default='Brak danych', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parcel',
            name='recipient_city',
            field=models.CharField(default='Kraków', max_length=100),
        ),
        migrations.AddField(
            model_name='parcel',
            name='recipient_coordinates',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='parcel',
            name='recipient_house_number',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AddField(
            model_name='parcel',
            name='recipient_postal_code',
            field=models.CharField(default='00-000', max_length=10),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('NEW', 'Nowe'), ('PICKED_UP', 'Kurier odebrał paczkę'), ('SORTING', 'Paczka jest na sortowni'), ('OUT_FOR_DELIVERY', 'Wydana do doręczenia'), ('DELIVERED', 'Doręczona')], default='NEW', max_length=20),
        ),
    ]
