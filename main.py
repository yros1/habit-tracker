import os
from time import process_time

import requests_cache
import requests
from dotenv import load_dotenv
from datetime import datetime

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

# response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(response.text)

# 3. Get the graph!
# Browse https://pixe.la/v1/users/a-know/graphs/test-graph! This is also the /v1/users/<username>/graphs/<graphID> API.
# In my case https://pixe.la/v1/users/yros1/graphs/coding-graph-1

#4. Post pixel value to the graph.
# /v1/users/<username>/graphs/<graphID>
pixel_creation_endpoint = f"{graph_endpoint}/{os.environ.get('PIXELA_GRAPH_ID')}"

today = datetime.now()
# print(today.strftime("%Y%m%d"))

pixel_creation_parameters = {
    "date": f"{today.strftime('%Y%m%d')}",
    "quantity": "120",
    "optionalData": "{\"comment\": \"Coding time for today.\"}"
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_creation_parameters, headers=headers)
# print(response.text)

#5. Update pixel value on the graph.
# PUT /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
pixel_update_endpoint = f"{pixel_creation_endpoint}/{today.strftime('%Y%m%d')}"

pixel_update_parameters = {
    "quantity": "30",
    "optionalData": "{\"comment\": \"Updated coding time for today.\"}"
}

# response = requests.put(url=pixel_update_endpoint, json=pixel_update_parameters, headers=headers)
# print(response.text)

#6. Delete pixel value on the graph.
# DELETE /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>
pixel_delete_endpoint = f"{pixel_creation_endpoint}/{today.strftime('%Y%m%d')}"

response = requests.delete(url=pixel_delete_endpoint, headers=headers)
print(response.text)