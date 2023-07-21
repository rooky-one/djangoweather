from django.shortcuts import render


# Create your views here....


def home(request):
    import json
    import requests
    # Works 21/07/2023
    api_request = requests.get("http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/322690?res=3hourly&key=ca6ccf25-e065-494b-9f2d-13a38f584994")



    try:
        api = json.loads(api_request.content)

    except Exception as e:
        api = "Error in attempting to retrieve API request from http://datapoint.metoffice.gov.uk/..."

    # API URL goes here:
    # http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/322690?res=3hourly&key=ca6ccf25-e065-494b-9f2d-13a38f584994

    return render(request, 'home.html', {
        'api': api,
    })


def about(request):
    return render(request, 'about.html', {})
