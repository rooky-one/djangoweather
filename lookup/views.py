from django.shortcuts import render

# Create your views here.

def home(request):
	# ApI URL goes here:
	# http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/xml/322690?res=3hourly&key=ca6ccf25-e065-494b-9f2d-13a38f584994

	return render(request, 'home.html', {})

def about(request):
	return render(request, 'about.html', {})