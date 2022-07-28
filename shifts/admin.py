from django.contrib import admin
from django.db import models

# Register your models here.
from .models import Shift,User,Group

class ShiftAdmin(admin.ModelAdmin):
	list_display=('place_text','type','date','start_time','finish_time','details','created','updated')

class UserAdmin(admin.ModelAdmin):
	list_display=('first_name','last_name','email')
	#group=models.OneToOneField(Group, default=None, blank=True,on_delete=models.CASCADE)
	#search_fields = [group]
	

admin.site.register (Shift, ShiftAdmin)
admin.site.register (User, UserAdmin)