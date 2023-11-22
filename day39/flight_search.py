class FlightSearch:
    import requests
    def __init__(self):

    def add_iata_code(self,city_name):

        headers = {
            'accept': 'application/json',
            'apikey': 'a4WoTyNzP6TC4XomHLbrjLp8yi8tm6rn',
        }

        params = {
            {"term": city_name,
             "location_types": "city"}
        }

        response = requests.get('https://api.tequila.kiwi.com/locations/query', params=params, headers=headers)