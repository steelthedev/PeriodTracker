from django.db import models
#from accounts.models import Profile
from django.contrib.auth.models import User
# Create your models here.
class Period(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	ovulation_cycle=models.IntegerField()
	Period_date=models.DateTimeField(max_length=300)

	def __str__(self):
		return self.Period_date


		