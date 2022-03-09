import requests
import os

SHEETY_ENDPOINT = "https://api.sheety.co/97fc889332836425c14090a0171f2b63/flightDeals/prices"
SHEETY_HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.environ['SHEETY_BEARER']}"
}


class DataManager:
    def __init__(self):
        self.params = {}
        self.object_id = None
        self.sheety_get_response = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_HEADERS)
        self.sheety_put_response = None

    def get_data(self):
        self.sheety_get_response.raise_for_status()
        return self.sheety_get_response.json()

    def put_data(self, iata_code, object_id):
        self.params = {
            "price": {
                "iataCode": iata_code
            }
        }
        self.object_id = object_id
        self.sheety_put_response = requests.put(url=f"{SHEETY_ENDPOINT}/{self.object_id}", headers=SHEETY_HEADERS,
                                                json=self.params)
        self.sheety_put_response.raise_for_status()
        return self.sheety_put_response.json()
