# Generated by Django 5.1 on 2024-09-12 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rentals', '0003_nonstaff'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='gender',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]