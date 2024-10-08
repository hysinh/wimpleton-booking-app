from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Venue, Booking, Contact

# Register your models here.
@admin.register(Venue)
class VenueAdmin(SummernoteModelAdmin):
    list_display = ('venue_name', 'id', 'venue_blurb', 'venue_capacity', )
    search_fields = ['title']
    list_filter = ('venue_capacity',)
    prepopulated_fields = {'slug': ('venue_name',)}
    summernote_fields = ('venue_description',)


@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    list_display = ('venue', 'event_date', 'event_type', 'client', 'booking_id', )
    search_fields = ['venue']
    list_filter = ['venue']


@admin.register(Contact)
class ContactAdmin(SummernoteModelAdmin):
    list_display = ('name', 'email', 'read', )
    search_fields = ['name']
    list_filter = ['read']