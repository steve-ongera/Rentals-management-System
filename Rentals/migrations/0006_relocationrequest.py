# Generated by Django 5.1 on 2024-09-14 21:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rentals', '0005_worker_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelocationRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('request_date', models.DateTimeField(auto_now_add=True)),
                ('decision_date', models.DateTimeField(blank=True, null=True)),
                ('current_house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='current_relocations', to='Rentals.house')),
                ('desired_house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='desired_relocations', to='Rentals.house')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rentals.tenant')),
            ],
        ),
    ]