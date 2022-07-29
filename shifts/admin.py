from django.contrib import admin
from django.db import models

# Register your models here.
from .models import Shift,User




class ShiftAdmin(admin.ModelAdmin):

	list_display=('place','type','date','start_time','finish_time','details','created','updated')
	search_fields = ['city']


class UserAdmin(admin.ModelAdmin):
	list_display=('first_name','last_name','email','role')
	search_fields = ['role']
	

admin.site.register (Shift, ShiftAdmin)
admin.site.register (User, UserAdmin)