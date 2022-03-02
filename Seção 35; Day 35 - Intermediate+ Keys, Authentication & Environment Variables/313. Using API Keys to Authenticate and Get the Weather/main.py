# Autenticação e por que autenticar?
# A autenticação serve para limitar o uso da aplicação visto que certos dados possuem custos para serem gerados, logo,
# uma maneira de controlar a quantidade de vezes que esses dados podem ser utilizados é através da autenticação das APIs
import requests

API_KEY = "*"
MY_LAT = -41.298743
MY_LONG = -38.875640
ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY
}

response = requests.get(url=ENDPOINT, params=parameters)
print(f"Status code: {response.status_code}")
print(response.json())
