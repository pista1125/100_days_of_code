import requests
from datetime import datetime, timedelta
class FlightSearch:

    def __init__(self):
        self.headers = {
            'accept': 'application/json',
            'apikey': 'a4WoTyNzP6TC4XomHLbrjLp8yi8tm6rn',
        }

    def search_cheaper_flight(self, fly_from, fly_to, day, min_night, max_night, person):
        today = datetime.now()
        end_day =datetime.now() + timedelta(days=day)
        params = {
            'fly_from': fly_from,
            'fly_to': fly_to,
            'date_from': f"{today.day}/{today.month}/{today.year}",
            'date_to': f"{end_day.day}/{end_day.month}/{end_day.year}",
            'nights_in_dst_from': min_night,
            'nights_in_dst_to': max_night,
            'adults': person,
            "flight_type": "round",
            'partner_market': 'usd',
            "limit": "1"
        }

        response = requests.get(url='https://api.tequila.kiwi.com/v2/search', params=params, headers=self.headers)
        flight = response.json()
        return flight

    def search_all_flight(self, fly_from, fly_to, day, min_night, max_night, person, price):
        today = datetime.now()
        end_day = datetime.now() + timedelta(days=day)
        params = {
            'fly_from': fly_from,
            'fly_to': fly_to,
            'date_from': f"{today.day}/{today.month}/{today.year}",
            'date_to': f"{end_day.day}/{end_day.month}/{end_day.year}",
            'nights_in_dst_from':min_night,
            'nights_in_dst_to': max_night,
            'adults': person,
            "flight_type": "round",
            'price_from': price,
            'price_to': f"{round(price * 1.30)}",
            'partner_market': 'usd',
            'limit': '100',
        }

        response = requests.get(url='https://api.tequila.kiwi.com/v2/search', params=params, headers=self.headers)
        all_flight_data = response.json()
        return all_flight_data



