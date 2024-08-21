from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Venue, Booking

# Register your models here.
@admin.register(Venue)
class VenueAdmin(SummernoteModelAdmin):
    list_display = ('venue_name', 'venue_blurb', 'venue_capacity', )
    search_fields = ['title']
    list_filter = ('venue_capacity',)
    prepopulated_fields = {'venue_slug': ('venue_name',)}
    summernote_fields = ('venue_description',)


admin.site.register(Booking)