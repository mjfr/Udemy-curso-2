import requests

API_KEY = "*"
MY_LAT = -41.298743
MY_LONG = -38.875640
ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily",
    "appid": API_KEY
}

response = requests.get(url=ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()
print(weather_data)


def bring_umbrella():
    for next_hour in weather_data["hourly"][:12]:
        # print(f'{weather_data["hourly"][next_hour]["weather"]}\t\t{weather_data["hourly"][next_hour]["dt"]}')
        # print(weather_data["hourly"][next_hour]["weather"][0]["id"])
        if next_hour["weather"][0]["id"] < 700:
            print("Bring an Umbrella")


bring_umbrella()
