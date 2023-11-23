import requests

class FlightData:
    def __init__(self):
        self.kiwi_endpoint = 'https://api.tequila.kiwi.com'

    def add_iata_code(self, city_name):
        headers = {
            'accept': 'application/json',
            'apikey': 'a4WoTyNzP6TC4XomHLbrjLp8yi8tm6rn',
        }

        params = {
            "term": city_name,
            "location_types": "city"
        }

        response = requests.get(url=f"{self.kiwi_endpoint}/locations/query", params=params, headers=headers)
        result = response.json()
        return result["locations"][0]["code"]