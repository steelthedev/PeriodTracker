from django.db import models
#from accounts.models import Profile
from django.contrib.auth.models import User
from period.models import Period
# Create your models here.
class PeriodDetails(models.Model):
	period_date=models.ForeignKey(Period,on_delete=models.CASCADE)
	

def __str__(self):
	return self.user.first_name