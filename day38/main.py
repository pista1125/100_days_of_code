import requests
from datetime import datetime

Gender = "male"
Weight = 100
Height = 192
Age = 27

APP_ID = "6b4fa182"
API_KEY = "059db4892b720940df8b1bd346d5a2b3"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
 "query": exercise_text,
 "gender":Gender,
 "weight_kg":Weight,
 "height_cm":Height,
 "age":Age
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()

#add a time to code:
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


#Google sheet add
sheety_endpoint = "https://api.sheety.co/3727bd71eca068dbb436d2a3d48374eb/myWorkouts/workouts"

retrieve_response = requests.get(url=sheety_endpoint)
row = retrieve_response.json()

#2 take information to google sheet

for data in result["exercises"]:
    new_data = {
        "workout": {
            "date" : today_date,
            "time": now_time,
            "exercise": data["user_input"],
            "duration": data["duration_min"],
            "calories": data["nf_calories"]
            }
    }
    add_response = requests.post(url=sheety_endpoint, json=new_data)