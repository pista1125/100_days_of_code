import requests

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
print(result)