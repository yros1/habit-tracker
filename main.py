import os

import requests_cache
import requests
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

# 1. Create a new user account.
pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": os.environ.get("PIXELA_API_TOKEN"),
    "username": os.environ.get("PIXELA_API_USERNAME"),
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)

# 2. Create a new graph.
graph_endpoint = f"{pixela_endpoint}/{os.environ.get('PIXELA_API_USERNAME')}/graphs"

graph_parameters = {
    "id": os.environ.get("PIXELA_GRAPH_ID"),
    "name": os.environ.get("PIXELA_GRAPH_NAME"),
    "unit": "minute",
    "type": "int",
    "color": "sora",
    "description": "A graph to track coding time."
}

headers = {
    "X-USER-TOKEN": os.environ.get("PIXELA_API_TOKEN")
}

response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
print(response.text)