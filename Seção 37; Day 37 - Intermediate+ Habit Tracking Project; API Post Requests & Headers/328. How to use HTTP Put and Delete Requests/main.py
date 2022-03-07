import requests
import os
import datetime as dt

# today = dt.datetime.now()
# today = dt.datetime.now() - dt.timedelta(days=1)
today = dt.datetime.now() - dt.timedelta(days=19)

someday = dt.datetime(year=2021, month=3, day=7)
date = today.strftime("%Y%m%d")

USERNAME = os.environ["PIXELA_USERNAME"]
TOKEN = os.environ["PIXELA_TOKEN"]
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"
PIXEL_PUT_DELETE_ENDPOINT = f"{PIXEL_ENDPOINT}/{date}"

headers = {
    "X-USER-TOKEN": TOKEN
}

pixel_config = {
    "date": date,
    "quantity": "240"
}

# response = requests.put(url=PIXEL_ENDPOINT, json=pixel_config, headers=headers)
# response = requests.put(url=PIXEL_PUT_DELETE_ENDPOINT, json=pixel_config, headers=headers)
response = requests.delete(url=PIXEL_PUT_DELETE_ENDPOINT, headers=headers)
print(response.text)
response.raise_for_status()
