# Generated by Django 5.1 on 2024-09-15 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rentals', '0008_house_house_number_house_is_vacant_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='house',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='houses/images/'),
        ),
        migrations.AddField(
            model_name='house',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='houses/images/'),
        ),
        migrations.AddField(
            model_name='house',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='houses/images/'),
        ),
        migrations.AddField(
            model_name='house',
            name='rent_fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]