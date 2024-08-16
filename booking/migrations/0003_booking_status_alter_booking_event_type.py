# Generated by Django 4.2.15 on 2024-08-16 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_alter_venue_staff_member_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.IntegerField(choices=[(0, 'Pending'), (1, 'Approved')], default=0),
        ),
        migrations.AlterField(
            model_name='booking',
            name='event_type',
            field=models.CharField(choices=[('OCC', 'Special Occasion'), ('COR', 'Corporate Event'), ('GAL', 'Gala Event'), ('OTH', 'Other'), ('WED', 'Wedding'), ('WSP', 'Workshop')], max_length=3),
        ),
    ]
