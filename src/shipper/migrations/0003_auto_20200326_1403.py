# Generated by Django 3.0.4 on 2020-03-26 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipper', '0002_auto_20200325_0101'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_address',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='order',
            name='pickup_address',
            field=models.TextField(default=''),
        ),
    ]
