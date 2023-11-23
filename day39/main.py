from data_manager import DataManager
from flight_search import FlightSearch

sheet_data = DataManager()
search_flight = FlightSearch()

#if you need search iatacode, use this:

#sheet_data.edit_data()

#print(sheet_data.get_data())

#2. api call for cheapest fly

flight_data = search_flight.search_cheaper_flight(fly_from="BUD", fly_to="PAR", day=90, min_night=2, max_night=7, person=1)

#This is the cheapest option for fly

from_city = flight_data["data"][0]["cityFrom"]
to_city = flight_data["data"][0]["cityTo"]
from_data = flight_data["data"][0]["route"][0]["local_departure"].split(".")[0]
back_data = flight_data["data"][0]["route"][1]["local_departure"].split(".")[0]
night = flight_data["data"][0]["nightsInDest"]
valuta = "EUR"
price = flight_data["data"][0]["price"]

#create csv file with this
sheet_data.create_csv(from_city, to_city, valuta, price, from_data, back_data, night)

#3. search all the possible option:

all_flight_data = search_flight.search_all_flight(fly_from="BUD", fly_to="PAR", day=90, min_night=2, max_night=7, person=1, price=64)

for option in all_flight_data["data"]:
    from_city = option["cityFrom"]
    to_city = option["cityTo"]
    from_data = option["route"][0]["local_departure"].split(".")[0]
    back_data = option["route"][1]["local_departure"].split(".")[0]
    night = option["nightsInDest"]
    valuta = "EUR"
    price = option["price"]
    print(from_city,from_data,from_data,back_data,night,price)

#If you want to add in sheety application
# sheet_data.add_row(from_city, to_city, valuta, price, from_data, back_data, night)



#sheet_data.create_csv(from_city, to_city, valuta, price, from_data, back_data, night)





