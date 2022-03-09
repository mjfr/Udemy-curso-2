import requests
import os
import datetime as dt

KIWI_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
KIWI_APIKEY = os.environ["KIWI_KEY"]
KIWI_HEADERS = {
    "apikey": KIWI_APIKEY,
    "Content-Encoding": "gzip"
}


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.today_date = dt.datetime.today()
        self.tomorrow_date = self.today_date + dt.timedelta(days=1)
        self.six_months = self.today_date + dt.timedelta(days=180)
        self.search_params = {
            "fly_from": "fromIATA",
            "fly_to": "toIATA",
            "dateFrom": self.tomorrow_date.strftime("%d/%m/%Y"),
            "dateTo": self.six_months.strftime("%d/%m/%Y"),
            "flight_type": "oneway",  # Round que estava sendo pedido no desafio, não retornava dados. Na documentação
            # Está dito que logo mais sairá de prática.
            "max_stopovers": "0",
            "curr": "GBP",
            "limit": "20"  # Poucos resultados para ficar mais leve
        }

    def get_prices(self, fly_from, fly_to):
        self.search_params["fly_from"] = fly_from
        self.search_params["fly_to"] = fly_to
        flight_response = requests.get(url=KIWI_ENDPOINT, params=self.search_params, headers=KIWI_HEADERS)
        flight_response.raise_for_status()
        return flight_response.json()
