import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.data_url = "https://api.sheety.co/3727bd71eca068dbb436d2a3d48374eb/flightDeals/prices"
        self.destination_data = {}

    def get_data(self):
        response = requests.get(url=self.data_url)
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data

    def edit_data(self):
        self.get_data()
        for city in self.destination_data:
            data_url = f"{self.data_url}/{city['id']}"
            new_data = {
                "price": {
                    "iataCode": "Testing"
                }
            }
            response = requests.put(url=data_url, json=new_data)