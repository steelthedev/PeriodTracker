from django.contrib import admin

from .models import Period
from dashboard.models import PeriodDetails
# Register your models here.


# Register your models here.
admin.site.register(PeriodDetails)
admin.site.register(Period)
