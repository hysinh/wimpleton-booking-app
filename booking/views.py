from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from .models import Venue

# Create your views here.
class VenueList(generic.ListView):
     """
     Renders a paginated view of 6 posts the queryset displaying the title and
     basic information about each post allowing user to navigate to older and newer
     posts.
     Displays an multiple descending instances of :model:`blog.Post`.
     **Context**
     ``index``
        The most recent 6 instances instance of :model:`blog.Post`.
     **Template:**
     :template:`blog/index.html`
     """
     model = Venue