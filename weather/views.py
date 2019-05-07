import requests
from django.shortcuts import render


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=2b7e7ab4395541013bb0df19fba94fac'
    city = 'cairo'
    r = requests.get(url.format(city)).json()
    city_weather = {
        'city': city,
        'temperature': r['main']['temp'],
        'icon': r['weather'][0]['icon'],
    }
    context = {
        'city_weather': city_weather
    }
    return render(request, 'weather/index.html', context)
