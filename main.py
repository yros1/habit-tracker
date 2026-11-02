import os

import requests_cache
import requests
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

# 1. Create a new user account
pixela_endpoint = "https://pixe.la/v1/users"

user_parameters = {
    "token": os.environ.get("PIXELA_API_TOKEN"),
    "username": os.environ.get("PIXELA_API_USERNAME"),
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)