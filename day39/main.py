from data_manager import DataManager
from flight_search import FlightSearch
import pandas
from datetime import datetime, timedelta
from notification_manager import NotificationManager

email = NotificationManager()
sheet_data = DataManager()
search_flight = FlightSearch()

today = datetime.now()
end_day = datetime.now() + timedelta(days=90)

        #f"{today.day}/{today.month}/{today.year}"
        #f"{end_day.day}/{end_day.month}/{end_day.year}"
#if you need search iatacode, use this:

#sheet_data.edit_data()

#print(sheet_data.get_data())

#2. api call for cheapest fly


flight_data = search_flight.search_all_flight(fly_from="Budapest", fly_to="Brussel", date_from=f"{today.day}/{today.month}/{today.year}", date_to=f"{end_day.day}/{end_day.month}/{end_day.year}", min_night=2, max_night=7, person=1)

flight_dic = {
    "City_From": {0: None},
    "City_To": {0: None},
    "Price": {0: None},
    "Date_To": {0: None},
    "Date_Back": {0: None},
    "Night": {0: None},
    "Link": {0: None}
}

index = 0
for option in flight_data["data"]:
    #onather option for cheapest file data
    from_city = option["cityFrom"]
    to_city = option["cityTo"]
    from_data = option["route"][0]["local_departure"].split(".")[0]
    back_data = option["route"][1]["local_departure"].split(".")[0]
    night = option["nightsInDest"]
    valuta = "EUR"
    price = option["price"]
    link = option['deep_link']

    #add new line to the first dic
    flight_dic["City_From"][index] = from_city
    flight_dic["City_To"][index] = to_city
    flight_dic["Price"][index]= f"{valuta}: {price}"
    flight_dic["Date_To"][index] = from_data
    flight_dic["Date_Back"][index] = back_data
    flight_dic["Night"][index] = night
    flight_dic["Link"][index] = link
    index += 1

df = pandas.DataFrame(flight_dic)

df.to_csv("flight.csv")

df.to_excel("flight.xlsx")



#If you want to add in sheety application
# sheet_data.add_row(from_city, to_city, valuta, price, from_data, back_data, night)
#sheet_data.create_csv(from_city, to_city, valuta, price, from_data, back_data, night)





email.send_mail("pista1125@gmail.com", "pista1125@gmail.com", "proba", "hello")

