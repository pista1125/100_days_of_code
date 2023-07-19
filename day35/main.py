import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

# api_key = "1e313878a7ffc19a293eb704b41fbd78"
api_key = "69f04e4613056b159c2761a9d9e664d2"


weather_params = {
    "lat": 46.018070,
    "lon": 17.622770,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts"
}
response = requests.get(url=OWM_Endpoint, params=weather_params )
response.raise_for_status()

weather_data = response.json()
print(weather_data)