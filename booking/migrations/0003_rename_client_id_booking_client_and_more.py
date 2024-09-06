# Generated by Django 4.2.15 on 2024-09-06 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_alter_booking_event_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='client_id',
            new_name='client',
        ),
        migrations.AlterField(
            model_name='booking',
            name='event_type',
            field=models.CharField(choices=[('OCC', 'Special Occasion'), ('COR', 'Corporate Event'), ('GAL', 'Gala Event'), ('WSP', 'Workshop'), ('OTH', 'Other'), ('WED', 'Wedding')], max_length=3),
        ),
    ]
