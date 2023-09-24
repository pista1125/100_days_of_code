import requests

my_website = "https://pixe.la/@istvan95"

TOKEN = "htetonsnteosnse"
USERNAME = "istvan95"
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
    "id": "graph1",
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

#delete hello nn bkb