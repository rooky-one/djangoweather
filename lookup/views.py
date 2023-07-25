from django.shortcuts import render


# Create your views here....


def home(request):
    import json
    import requests
    # Works 21/07/2023
    api_request = requests.get("http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/322690?res=3hourly&key=ca6ccf25-e065-494b-9f2d-13a38f584994")



    try:
        api = json.loads(api_request.content)
        # api = api_request.content

    except Exception as e:
        api = "Error..."

   # If api.SiteRep.DV.Location.Period.0.value = 7
        # "Test"
        # 00-03hrs < Type: {{ api.SiteRep.DV.Location.Period.0.Rep.0.W }} | Temp: {{ api.SiteRep.DV.Location.Period.0.Rep.0.T }}oC | Rain: {{ api.SiteRep.DV.Location.Period.0.Rep.0.Pp }}% | UV: {{ api.SiteRep.DV.Location.Period.0.Rep.0.U }}% ><br/>

    # API URL goes here:
    # http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/322690?res=3hourly&key=ca6ccf25-e065-494b-9f2d-13a38f584994

    return render(request, 'home.html', {
        'api': api,
    })


def about(request):
    return render(request, 'about.html', {})
