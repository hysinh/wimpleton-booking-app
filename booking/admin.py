from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Venue, Booking

# Register your models here.
@admin.register(Venue)
class VenueAdmin(SummernoteModelAdmin):
    list_display = ('venue_name', 'venue_blurb' )
    summernote_fields = ('venue_description')


admin.site.register(Booking)