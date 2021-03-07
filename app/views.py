from django.shortcuts import render,redirect
from .models import Event
def dashboard(request):
	events=Event.objects.all()	
	return render(request,'dashboard.html',{'events':events})
def create(request):
	if request.method=="POST":
		name=request.POST['name']
		location=request.POST['location']
		date=request.POST['date']
		time=request.POST['time']
		image=request.FILES['image']
		like = request.POST.get("like", None)
		if like:
			query=Event.objects.create(Event_Name=name,Creation_Date=date,Creation_Time=time,Location=location,Image=image,is_liked=True)
		else:
			query=Event.objects.create(Event_Name=name,Creation_Date=date,Creation_Time=time,Location=location,Image=image)
		return redirect('/app')
	else:
		return render(request,'create.html')
# Create your views here.
