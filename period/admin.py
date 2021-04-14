from django.contrib import admin
from accounts.models import Profile
from .models import Period
from dashboard.models import PeriodDetails
# Register your models here.
admin.site.register(Profile)

# Register your models here.
admin.site.register(PeriodDetails)
admin.site.register(Period)