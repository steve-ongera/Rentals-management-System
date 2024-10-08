# Generated by Django 5.1 on 2024-09-11 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rentals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=20, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('role', models.CharField(max_length=100)),
                ('photo', models.ImageField(default='workers/photos/avatar.svg', upload_to='workers/photos/')),
                ('passport_photo', models.ImageField(default='workers/passport_photos/Kenya-ID.jpg', upload_to='workers/passport_photos/')),
            ],
        ),
    ]
