# Generated by Django 4.2.15 on 2024-09-16 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0005_alter_booking_event_type_alter_booking_num_guests'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='event_type',
            field=models.CharField(choices=[('Corporate', 'Corporate Event'), ('Wedding', 'Wedding'), ('Other', 'Other'), ('Special Occasion', 'Special Occasion'), ('Gala', 'Gala Event'), ('Workshop', 'Workshop')], max_length=20),
        ),
    ]
