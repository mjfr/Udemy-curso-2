# Environment Variables são variáveis que estão no próprio sistema e não são visíveis (e talvez não existam) fora do
# sistema. É uma forma segura de testar e subir códigos para a internet sem que informações sensíveis sejam vazadas.
# Uma alternativa para subir os códigos com informações sensíveis é utilizar um .py para configurar as informações e no
# momento de subir o código, explicitamos ao .gitignore que queremos ocultar o .py da configuração.
import requests
import os  # Para usar as Environment Variables, importamos 'os'
ENDPOINT_TELEGRAM = "https://api.telegram.org/bot"
BOT_TOKEN = os.environ["BOT_TOKEN"]  # Para acessar as Environment Variables, fazemos como em dicionários.
BOT_CHAT_ID = os.environ["CHAT_ID"]
API_KEY = os.environ["OPEN_WEATHER_MAP_TOKEN"]
MY_LAT = -41.298743
MY_LONG = -38.875640
ENDPOINT_WEATHER = "https://api.openweathermap.org/data/2.5/onecall"
EXCLUDE_LIST = ["current", "minutely", "daily"]
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily",
    "appid": API_KEY
}

response_weather = requests.get(url=ENDPOINT_WEATHER, params=parameters)
response_weather.raise_for_status()
weather_data = response_weather.json()
print(weather_data)


def bring_umbrella():
    for next_hour in weather_data["hourly"][:12]:
        if next_hour["weather"][0]["id"] < 700:
            return "Bring an Umbrella"


def weather_telegram_bot(bot_message):

    response_telegram = requests.get(url=f"{ENDPOINT_TELEGRAM}{BOT_TOKEN}/sendMessage?chat_id={BOT_CHAT_ID}"
                                         f"&parse_mode=Markdown&text={bot_message}")
    return response_telegram.json()


test = weather_telegram_bot(bring_umbrella())
print(test)
