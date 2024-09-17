from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


TYPE_OF_EVENT_CHOICES = {
        ("Wedding", "Wedding"),
        ("Corporate", "Corporate Event"),
        ("Gala", "Gala Event"),
        ("Special Occasion", "Special Occasion"),
        ("Workshop", "Workshop"),
        ("Other", "Other"),
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
    featured_image = CloudinaryField('image', default='placeholder')
    venue_description = models.TextField()
    venue_blurb = models.TextField(blank=True)
    venue_capacity = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)


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
    client = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="venue_bookings"
        )
    event_type = models.CharField(
        max_length=20,
        choices=TYPE_OF_EVENT_CHOICES
    )
    event_date = models.DateField()
    num_guests = models.IntegerField(
        default=20,
        validators=[
            MaxValueValidator(500, message="Guest count cannot exceed 500 guests"),
            MinValueValidator(20, message="Guest count requires a mimum of 20 guests")
        ]
     )
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    # Tried this for validation error - not working 
    def save(self, *args, **kwargs):
        if self.num_guests > 500:
            raise ValidationError("Guest count cannot exceed 500 guests")
        super(Booking, self).save(*args, **kwargs)


    class Meta:
        ordering = ["event_date", "-client_id"]
        constraints = [
            models.UniqueConstraint(
                fields=['event_date', 'venue'],
                        name='booking_unique_date_venue',
                        violation_error_message='Booking with this Venue already exits.',   
            ),
        ]

    def __str__ (self):
        return f"{self.venue}"
