import requests
import os

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": os.environ["PIXELA_TOKEN"],
    "username": os.environ["PIXELA_USERNAME"],
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Diferente do .get(), usamos o kwarg json para passar os parâmetros
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)
# response.raise_for_status()
