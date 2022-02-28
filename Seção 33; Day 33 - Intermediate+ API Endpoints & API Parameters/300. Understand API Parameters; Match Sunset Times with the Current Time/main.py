# Algumas APIs possuem parâmetros que nos possibilitam conseguir diferentes dados, por exemplo:
# Uma API sem parâmetros ficaria assim ao ser traduzida para o mundo real. Banco, a que horas você fecha? <-- Pergunta
# mais generalizada. Agora com parâmetros: banco, a que horas você fecha no {domingo}? <-- Pergunta mais específica.

import requests
from datetime import datetime

MY_LAT = -43.357178
MY_LONG = -27.568970

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
# Os splits estão separando o datetime não formatado vindo da api. Retorna apenas a hora em formato 24h
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now()
