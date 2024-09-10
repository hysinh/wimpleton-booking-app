# Generated by Django 4.2.15 on 2024-09-10 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_alter_booking_event_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='event_type',
            field=models.CharField(choices=[('Special Occasion', 'Special Occasion'), ('Workshop', 'Workshop'), ('Gala', 'Gala Event'), ('Wedding', 'Wedding'), ('Other', 'Other'), ('Corporate', 'Corporate Event')], max_length=20),
        ),
        migrations.AddConstraint(
            model_name='booking',
            constraint=models.UniqueConstraint(fields=('event_date', 'venue'), name='booking_unique_date_venue', violation_error_message='Booking with this Venue already exits.'),
        ),
    ]
