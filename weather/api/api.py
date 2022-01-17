from datetime import datetime
import requests
import json
from country_codes import country_codes

API_KEY="e6edf57121404cd9bd485029221501"

weather_api_url = " http://api.weatherapi.com/v1"

# /weather-forecat/<str: for_date>/<str: country_code>/
def get_weather_forecast(for_date=datetime.now().strftime("%Y-%m-%d"), country_code=None):
    
    q = country_codes[country_code]
    dt = for_date
    breakpoint()
    res = requests.get(weather_api_url+f"/current.json?key={API_KEY}&q={q}&aqi=no&dt={for_date}")
    res = res.json()

    f_temp = res['current']['temp_f']
    c_temp = res['current']['temp_c']
    breakpoint()
    


get_weather_forecast('wqasfdc', 'IN')
