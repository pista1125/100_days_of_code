import requests
from datetime import datetime, timedelta
class FlightSearch:

    def __init__(self):
        self.headers = {
            'accept': 'application/json',
            'apikey': 'wIGunaGGy9okmN4zSMXoXWd0R12qx0rG',
        }
        self.kiwi_endpoint = 'https://api.tequila.kiwi.com'
        self.search_endpoint = 'https://api.tequila.kiwi.com/v2/search'

    def add_iata_code(self, city_name):
        params = {
            "term": city_name,
            "location_types": "city"
        }

        response = requests.get(url=f"{self.kiwi_endpoint}/locations/query", params=params, headers=self.headers)
        result = response.json()
        return result["locations"][0]["code"]

    def search_all_flight(self, fly_from, fly_to, date_from, date_to, min_night, max_night, person):
        # today = datetime.now()
        # end_day = datetime.now() + timedelta(days=day)
        #f"{today.day}/{today.month}/{today.year}"
        #f"{end_day.day}/{end_day.month}/{end_day.year}"
        from_iata = self.add_iata_code(fly_from)
        to_iata = self.add_iata_code(fly_to)
        params = {
            'fly_from': from_iata,
            'fly_to': to_iata,
            'date_from': date_from,
            'date_to': date_to,
            'nights_in_dst_from':min_night,
            'nights_in_dst_to': max_night,
            'adults': person,
            "flight_type": "round",
            'partner_market': 'usd',
            'limit': '100',
        }

        response = requests.get(url=self.search_endpoint, params=params, headers=self.headers)
        all_flight_data = response.json()
        return all_flight_data



