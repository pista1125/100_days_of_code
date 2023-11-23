from data_manager import DataManager
from flight_search import FlightSearch
import pandas


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

all_flight_data = search_flight.search_all_flight(fly_from="BUD", fly_to="PAR", day=90, min_night=2, max_night=7, person=1, price=price)

first_csv = pandas.read_csv("flight.csv")
first_dic = first_csv.to_dict()

index = 1
for option in all_flight_data["data"]:
    #onather option for cheapest file data
    from_city = option["cityFrom"]
    to_city = option["cityTo"]
    from_data = option["route"][0]["local_departure"].split(".")[0]
    back_data = option["route"][1]["local_departure"].split(".")[0]
    night = option["nightsInDest"]
    valuta = "EUR"
    price = option["price"]

    #add new line to the first dic
    first_dic["City_From"][index] = from_city
    first_dic["City_To"][index] = to_city
    first_dic["Price"][index] = f"{valuta}: {price}"
    first_dic["Date_To"][index] = from_data
    first_dic["Date_Back"][index] = back_data
    first_dic["Night"][index] = night
    index += 1
df = pandas.DataFrame(first_dic)

#df.to_csv("flight.csv")

df.to_excel("final.xlsx", index=False)


#If you want to add in sheety application
# sheet_data.add_row(from_city, to_city, valuta, price, from_data, back_data, night)



#sheet_data.create_csv(from_city, to_city, valuta, price, from_data, back_data, night)





