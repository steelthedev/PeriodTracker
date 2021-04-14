from django.shortcuts import render,redirect
from .forms import PeriodForm
from datetime import datetime,timedelta
from .models import Period
#from django.contrib.auth import User
# Create your views here.
def mainpage(request):
  submitbutton = request.POST.get("submit")
  ovulation_cycle=""
  first_day_of_last=""
  men_date=""
  
  if request.method=='POST':
    form=PeriodForm(request.POST)
    if form.is_valid():
      ovulation_cycle=form.cleaned_data.get("ovulation_cycle")
      first_day_of_last=form.cleaned_data.get("first_day_of_last")
      old_date=datetime.strptime(first_day_of_last,'%d-%m-%Y')
      est_date=timedelta(days=ovulation_cycle)
      men_date=old_date + est_date

      if request.user.is_authenticated:
        period=Period.objects.get(user=request.user)
        period.ovulation_cycle=ovulation_cycle
        period.Period_date=men_date
        period.save()
      else:
        period=Period.objects.create(user=request.user,ovulation_cycle=ovulation_cycle,Period_date=men_date)
        period.save()
    
    else:
      return redirect('period:main')
  else:   
    form=PeriodForm()
  return render(request,'period/index.html',{'form':form,'submitbutton':submitbutton,'men_date':men_date,'ovulation_cycle':ovulation_cycle})
  
