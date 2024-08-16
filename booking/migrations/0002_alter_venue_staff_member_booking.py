# Generated by Django 4.2.15 on 2024-08-16 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='staff_member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='venue_listings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.IntegerField(unique=True)),
                ('event_type', models.CharField(choices=[('OCC', 'Special Occasion'), ('WED', 'Wedding'), ('OTH', 'Other'), ('GAL', 'Gala Event'), ('WSP', 'Workshop'), ('COR', 'Corporate Event')], max_length=3)),
                ('event_date', models.DateField()),
                ('num_guests', models.IntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='venue_bookings', to=settings.AUTH_USER_MODEL)),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='booking.venue')),
            ],
        ),
    ]
