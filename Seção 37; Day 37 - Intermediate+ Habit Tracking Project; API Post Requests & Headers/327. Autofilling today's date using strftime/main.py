import requests
import os
import datetime as dt

today = dt.datetime.now()
someday = dt.datetime(year=2021, month=3, day=7)
# O método .strftime() serve para formatar uma data da maneira que queremos.
date = today.strftime("%Y%m%d")

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
    "date": date,
    "quantity": "240"
}

response = requests.post(url=PIXEL_ENDPOINT, json=pixel_config, headers=headers)
print(response.text)
response.raise_for_status()
