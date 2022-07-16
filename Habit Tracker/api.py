import datetime
import os

import requests

TOKEN = "dsfhjs343438hjdrh8"
USERNAME="infernus2k"
pixela_endpoint = "https://pixe.la/v1/users"
parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsofService": "yes",
    "notMinor": "yes",
}

# r = requests.post(url="https://pixe.la/v1/users", json=parameters)
# print(r.text)

post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/pushups1"

graph_parameters = {
    "id": "pushups1",
    "name": "Pushup Challenge",
    "unit": "Reps",
    "type": "int",
    "color": "ichou",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# r = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(r.text)
now = datetime.datetime.now()

date = now.strftime("%Y%m%d")

post_parameters = {
    "date": date,
    "quantity": "40",
}

r = requests.post(url=post_endpoint, json=post_parameters, headers=headers)

print(r)