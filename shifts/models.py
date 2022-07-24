from django.db import models
from django.utils.timezone import now

# Create your models here.

class Venue (models.Model):
	#https://stackoverflow.com/questions/18676156/how-to-properly-use-the-choices-field-option-in-django

	class Types(models.TextChoices):
		LPN='LPN',
		RN ='RN'

	type = models.CharField(
        max_length=3,
        choices=Types.choices,
        default=Types.RN
    )

	created_at = models.DateTimeField(default=now, editable=True,null=True, blank=True)  
	updated_at = models.DateTimeField(default=None, editable=True,null=True, blank=True)
	place_text=models.CharField(max_length=200)

	
	date = models.DateField ('Date')
	start_time = models.DateTimeField ('start time')
	finish_time= models.DateTimeField ('finish time')
	details= models.CharField (max_length=500)


