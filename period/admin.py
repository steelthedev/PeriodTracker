from django.contrib import admin
from accounts.models import Profile
<<<<<<< HEAD
# Register your models here.
admin.site.register(Profile)
=======
from .models import Period
from dashboard.models import PeriodDetails
# Register your models here.
admin.site.register(Profile)

# Register your models here.
admin.site.register(PeriodDetails)
admin.site.register(Period)
>>>>>>> fe9aaf9f4e005ea7f8c24396ea02d39255381f47
