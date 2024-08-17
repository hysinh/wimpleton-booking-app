from django.db import models
from django.contrib.auth.models import User


TYPE_OF_EVENT_CHOICES = {
        ("WED", "Wedding"),
        ("COR", "Corporate Event"),
        ("GAL", "Gala Event"),
        ("OCC", "Special Occasion"),
        ("WSP", "Workshop"),
        ("OTH", "Other"),
    }

STATUS = ((0, "Pending"), (1, "Approved"))


# Create your models here.
class Venue(models.Model):
    """
    Stores a single venue entry 
    """
    venue_name = models.CharField(max_length=100)
    staff_member = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="venue_listings"
    )
    venue_description = models.TextField()
    venue_blurb = models.TextField(blank=True)
    venue_capacity = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["-venue_name"]


    def __str__ (self):
        return f"{self.venue_name}"


# TextChoice code source:
# https://docs.djangoproject.com/en/5.0/ref/models/fields/#enumeration-types
class Booking(models.Model):
    """
    Stores a single booking entry
    """
    booking_id = models.AutoField(primary_key=True)
    venue = models.ForeignKey(Venue, on_delete=models.PROTECT)
    client_id = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="venue_bookings"
        )
    event_type = models.CharField(
        max_length=3,
        choices=TYPE_OF_EVENT_CHOICES
    )
    event_date = models.DateField()
    num_guests = models.IntegerField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        unique_together = ('venue', 'event_date')
        ordering = ["-event_date", "-client_id"]


    def __str__ (self):
        return f"{self.event_date}, {self.venue}, {self.client_id}"

