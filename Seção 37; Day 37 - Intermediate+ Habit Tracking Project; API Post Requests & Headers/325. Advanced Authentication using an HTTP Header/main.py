import requests
import os

USERNAME = os.environ["PIXELA_USERNAME"]
TOKEN = os.environ["PIXELA_TOKEN"]
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Piano Learning Graph",
    "unit": "min",
    "type": "int",
    "color": "momiji"
}

# Método de autenticação utilizando header
headers = {
    "X-USER-TOKEN": TOKEN
}

# O header é uma forma que apresenta maior segurança ao se passar a apikey
response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
print(response.text)
response.raise_for_status()
