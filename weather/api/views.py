from django.shortcuts import render
from datetime import datetime
from django.conf import settings
from .country_codes import country_codes
import requests
from django.http import JsonResponse

# Create your views here.


weather_api_url = "http://api.weatherapi.com/v1"

def the_forecast_view(request, for_date=datetime.now().strftime("%Y-%m-%d"), country_code="IN"):

    result = get_weather_forecast(for_date, country_code)
    return JsonResponse(result)


def get_weather_forecast(for_date=datetime.now().strftime("%Y-%m-%d"), country_code="IN"):    
    try:
        if type(country_code) == list:
            q = country_codes[str(country_code[0])]
            dt = for_date[0]
        else:
            q = country_codes[str(country_code)]
            dt = for_date

        # print(f"[+] Querying {weather_api_url}/current.json?key={settings.API_KEY}&q={q}&aqi=no&dt={dt}")
        res = requests.get(weather_api_url+f"/current.json?key={settings.API_KEY}&q={q}&aqi=no&dt={dt}")
        res = res.json()

        #Farenhite Temp
        f_temp = res['current']['temp_f']

        # Celcius Temp
        c_temp = res['current']['temp_c']
        c_temp = float(c_temp)

        if c_temp >= 20:
            ret = {"forecast": "good"}
        elif 10 <= c_temp <20:
            ret = {"forecast": "soso"}
        else:
            ret = {"forecast": "bad"}
    except Exception as e:
        ret = {"Error":"Check Your Input of wait for a while"}
        print(f"get_weather_forecast:: {e} ")


    return ret