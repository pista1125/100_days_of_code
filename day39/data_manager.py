import requests
import pandas

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

    # def edit_data(self):
    #     self.get_data()
    #     for city in self.destination_data:
    #         data_url = f"{self.data_url}/{city['id']}"
    #         new_data = {
    #             "price": {
    #                 "iataCode": iata_code.add_iata_code(city["city"])
    #             }
    #         }
    #         response = requests.put(url=data_url, json=new_data)

    def add_row(self, City_from, City_To, valuta, price, Date_To, Date_Back, Night):
        new_data = {
            "price": {
                "City_From": City_from,
                "City_To": City_To,
                "Price": f"{valuta} {price}",
                "Date_To": Date_To,
                "Date_Back": Date_Back,
                "Night": Night
            }
        }
        response = requests.post(url=self.data_url, json=new_data)
        response.json()

    def create_csv(self, City_from, City_To, valuta, price, Date_To, Date_Back, Night):
        new_data ={
            "City_From": City_from,
            "City_To": City_To,
            "Price": f"{valuta}: {price}",
            "Date_To": Date_To,
            "Date_Back": Date_Back,
            "Night": Night
        }
        df = pandas.DataFrame(new_data, index=[0])
        df.to_csv("flight.csv")


