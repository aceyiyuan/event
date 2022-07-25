from django.contrib import admin

# Register your models here.
from .models import Venue

class VenueAdmin(admin.ModelAdmin):
	list_display=('place_text','type','date','start_time','finish_time','details','created','updated')

admin.site.register (Venue, VenueAdmin)