# Generated by Django 5.1 on 2024-09-16 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rentals', '0010_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='booking_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='is_booked',
            field=models.BooleanField(default=False),
        ),
    ]
