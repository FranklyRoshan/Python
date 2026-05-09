import dataclasses
from urllib import response

import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("PIXELA_TOKEN")


GRAPH_ID = "graph1"

# Pixela Website - https://pixe.la/
pixela_endpoint = "https://pixe.la/v1/users"

params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# 1. Sign up Pixela
# response = requests.post(url=pixela_endpoint, json=params)
# print(response.text)
# 1st Time
# {"message":"Success. Let's visit https://pixe.la/@franklyn , it is your profile page!","isSuccess":true}
# 2nd Time
# {"message":"This user already exist.","isSuccess":false}
# Web link: https://pixe.la/v1/users?token=jfi#w23c@nr$1&username=franklyn&agreeTermsOfService=yes&notMinor=yes


# 2. Create a graph
# Request Header
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# Request Body
graph_config = {
    "id": GRAPH_ID,
    "name": "Study",
    "unit": "hours",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response)
# print(response.text)
# Web link: https://pixe.la/v1/users/franklyn/graphs/graph1.html

# 3. POST
today = datetime.now()

# Request Header
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# Request Body
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you study today? (float) "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)
# Web link: https://pixe.la/v1/users/franklyn/graphs/graph1.html


# 4. PUT (Update)
date = today.strftime("%Y%m%d")
# Request Header
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
# Request Body
new_pixela_data = {
    "quantity": "2.5",
}

# response = requests.put(url=update_endpoint, json=new_pixela_data, headers=headers)
# print(response.text)
# Web link: https://pixe.la/v1/users/franklyn/graphs/graph1.html

# 5. DELETE
date = today.strftime("%Y%m%d")
# Request Header
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
# Request Body (Not required)

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
# Web link: https://pixe.la/v1/users/franklyn/graphs/graph1.html