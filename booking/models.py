from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Venue(models.Model):
    """
    Stores a single venue entry 
    """
    venue_id = models.IntegerField(unique=True)
    venue_name = models.CharField(max_length=100)
    staff_member = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="venue_bookings"
    )
    venue_description = models.TextField()
    venue_blurb = models.TextField(blank=True)
    venue_capacity = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
