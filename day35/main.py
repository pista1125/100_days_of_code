import requests
from twilio.rest import Client
#Weather call
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

# api_key = "1e313878a7ffc19a293eb704b41fbd78"
api_key = "69f04e4613056b159c2761a9d9e664d2"

#SMS call
account_sid = 'ACc9759d9b6afb3e259a72127956af0c4a'
auth_token = 'd25bad54509fa2c35b0ccd7c90584f96'


def sending_sms():
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+14327772526',
        body="Bring an umbrella",
        to='+36307270793'
    )
    print(message.sid)

weather_params = {
    "lat": 66.445302,
    "lon": 25.410103,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts"
}
response = requests.get(url=OWM_Endpoint, params=weather_params )
response.raise_for_status()

weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    sending_sms()
