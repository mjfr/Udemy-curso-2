import requests
import os

KIWI_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
KIWI_APIKEY = os.environ["KIWI_KEY"]
KIWI_HEADERS = {
    "apikey": KIWI_APIKEY
}


class FlightSearch:
    def __init__(self):
        self.kiwi_body = {
            "term": "city/iata_code",
            "locale": "en-US",
            "location_types": "city",
            "&location_types": "airport",
            "limit": "10",
            "active_only": "true"
        }

    def get_iata_code(self, city_name):
        self.kiwi_body["term"] = city_name
        kiwi_response = requests.get(url=KIWI_ENDPOINT, headers=KIWI_HEADERS, params=self.kiwi_body)
        kiwi_response.raise_for_status()
        return kiwi_response.json()["locations"][0]["code"]
