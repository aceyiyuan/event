from django.contrib import admin

# Register your models here.
from .models import Venue

class VenueAdmin(admin.ModelAdmin):
	fields=['place_text','type','date','start_time','finish_time','details','created_at','updated_at']

admin.site.register (Venue, VenueAdmin)