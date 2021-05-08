from django.shortcuts import render,redirect
from period.models import Period

# Create your views here.
def dashboard(request):
	user=request.user
	if user.is_authenticated:
		#period=Period.objects.get(user=user)
		name=user.profile.first_name
		#date=period.Period_date
	else:
		return redirect('main')



	return render(request,'dashboard/base.html',{'name':name})