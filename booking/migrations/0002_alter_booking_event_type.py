# Generated by Django 4.2.15 on 2024-09-11 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='event_type',
            field=models.CharField(choices=[('Corporate', 'Corporate Event'), ('Special Occasion', 'Special Occasion'), ('Wedding', 'Wedding'), ('Workshop', 'Workshop'), ('Gala', 'Gala Event'), ('Other', 'Other')], max_length=20),
        ),
    ]
