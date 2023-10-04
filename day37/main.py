import requests
from datetime import datetime
my_website = "https://pixe.la/@istvan95"

TOKEN = "htetonsnteosnse"
USERNAME = "istvan95"

GRAPH_ID = "graph1"
headers = {
    "X-USER-TOKEN": TOKEN
}

# Create pixela account
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


#Pixela Create graphs

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

grap_config = {
    "id": GRAPH_ID,
    "name": "Gym Graph",
    "unit": "db",
    "type": "float",
    "color": "sora"
}
# response = requests.post(url=graph_endpoint, json=grap_config, headers=headers)
# print(response.text)

#Delete pixela graphs
graph_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph2"

# response = requests.delete(url=graph_delete_endpoint, headers=headers)
# print(response.text)

#Config exist graphs
graph_config_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# response = requests.put(url=graph_config_endpoint, json=grap_config, headers=headers)
# print(response.text)


# Post a pixel
pixel_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

date = datetime.now()
today = date.strftime("%Y%m%d")

#oke
post_config = {
    "date": today,
    "quantity": "1"
}

response = requests.post(url=pixel_post_endpoint, json=post_config, headers=headers)
print(response.text)