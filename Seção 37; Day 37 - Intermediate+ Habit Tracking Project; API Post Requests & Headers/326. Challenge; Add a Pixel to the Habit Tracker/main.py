import requests
import os

USERNAME = os.environ["PIXELA_USERNAME"]
TOKEN = os.environ["PIXELA_TOKEN"]
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"

headers = {
    "X-USER-TOKEN": TOKEN
}

pixel_config = {
    "date": "20210307",
    "quantity": "240"
}

response = requests.post(url=PIXEL_ENDPOINT, json=pixel_config, headers=headers)
print(response.text)
response.raise_for_status()
