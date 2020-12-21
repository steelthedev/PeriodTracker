from django.shortcuts import render,redirect
from .forms import PeriodForm
from datetime import datetime,timedelta
# Create your views here.
def mainpage(request):
  submitbutton = request.POST.get("submit")
  ovulation_cycle=""
  first_day_of_last=""
  context=""
  men_date=""
  if request.method=='POST':
    form=PeriodForm(request.POST)
    if form.is_valid():
      ovulation_cycle=form.cleaned_data.get("ovulation_cycle")
      first_day_of_last=form.cleaned_data.get("first_day_of_last")
      old_date=datetime.strptime(first_day_of_last,'%d-%m-%Y')
      est_date=timedelta(days=ovulation_cycle)
      men_date=old_date + est_date
      context={'form':form,'men_date':men_date,'submitbutton':submitbutton}
    else:
      return redirect('period:main')
  else:   
    form=PeriodForm()
  return render(request,'period/index.html',{'form':form,'submitbutton':submitbutton,'men_date':men_date,'ovulation_cycle':ovulation_cycle})
  
