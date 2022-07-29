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
	city=models.CharField (max_length=20,editable=True,null=True, blank=True)
	place=models.CharField (max_length=500,editable=True,null=True, blank=True)
	unit=models.CharField (max_length=50,editable=True,null=True, blank=True)
	

	def __str__(self):
		return self.place
	

@receiver(pre_save, sender=Shift)
def shift_pre_save(sender, instance, *args, **kwargs):
	
	#instance.updated =None
	instance.updated=timezone.now()

@receiver(post_save, sender=Shift)
def shift_post_save(sender, instance,created, *args, **kwargs):
	
	if created:
	
		instance.updated=timezone.now()
		instance.save()

class User(AbstractUser):

	class Roles(models.TextChoices):
		employee='Employee',
		employer='Employer',
		owner ='Owner',
		admin ='Admin'

	role = models.CharField(
        max_length=15,
        choices=Roles.choices,
        default=Roles.employee
    )

	""" or

    class User(models.Model) :
    # NEW
    ROLES = (('employee', 'Employee'), ('employer', 'Employer'),...)
    role = models.CharField(
        max_length=20,
        choices=ROLES,
        default='employee'
    )

	"""

	
class Employer(models.Model):

	id = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True,unique=True)
	shift_id= models.ForeignKey(Shift, null=True, blank=True,on_delete=models.CASCADE)
	org_name=models.CharField(max_length=50,null=True, blank=True)
	org_city=models.CharField(max_length=50,null=True, blank=True)
	org_unit=models.CharField(max_length=100,null=True, blank=True)





