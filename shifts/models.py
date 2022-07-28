import uuid
from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from django.dispatch import receiver  
from django.contrib.auth.models import AbstractUser,Group


from django.db.models.signals import (

	pre_save,
	post_save

	)
# Create your models here.


class User(AbstractUser):
	
	is_employee = models.BooleanField(default=False)
	is_employer= models.BooleanField(default=False)
	is_superuser= models.BooleanField(default=False)
	
class Shift(models.Model):

	#https://stackoverflow.com/questions/18676156/how-to-properly-use-the-choices-field-option-in-django
	

	class Types(models.TextChoices):
		LPN='LPN',
		RN ='RN'

	type = models.CharField(
        max_length=3,
        choices=Types.choices,
        default=Types.RN
    )

	created = models.DateTimeField(default=now, editable=True,null=True, blank=True) 
	updated = models.DateTimeField(default=None, editable=True,null=True, blank=True)
	date = models.DateField ('Date')
	start_time = models.DateTimeField ('start time')
	finish_time= models.DateTimeField ('finish time')
	details= models.CharField (max_length=500)
	place_text=models.CharField(max_length=200)

	def __str__(self):
		return self.place_text
	

@receiver(pre_save, sender=Shift)
def shift_pre_save(sender, instance, *args, **kwargs):
	
	#instance.updated =None
	instance.updated=timezone.now()

@receiver(post_save, sender=Shift)
def shift_post_save(sender, instance,created, *args, **kwargs):
	
	if created:
	
		instance.updated=timezone.now()
		instance.save()



class Employee(models.Model):
	id = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True,unique=True)
	shift_id= models.ForeignKey(Shift, null=True, blank=True,on_delete=models.CASCADE)



