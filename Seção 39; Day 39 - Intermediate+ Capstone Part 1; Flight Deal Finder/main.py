from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
SET_LOCATION = "LON"
SET_CITY = "London"

# Pequeno disclaimer em minha defesa, o código ficou um lixo, confuso, feio mas também estou programando no momento
# depois de varar uma noite e minha cabeça está péssima. O que está comentado abaixo é para que o código não consuma
# todas as cotas mensais do Sheety.


# flight_search_data = FlightSearch()
sheet_data = DataManager()
price_data = sheet_data.get_data()["prices"]
# print(price_data)
# for data in price_data:
#     if data["iataCode"] == '':
#         data["iataCode"] = flight_search_data.get_iata_code(data["city"])
#         sheet_data.put_data(data["iataCode"], data["id"])
# print(price_data)

flight_data = FlightData()
prices = {}
price_list = []
flight = None
# Primeiro for rodando na planilha para deixar os dados da planilha disponíveis para o segundo for e para obter o
# iataCode
for data in price_data:
    flight_price = flight_data.get_prices(SET_LOCATION, data["iataCode"])
    # Segundo for rodando no retorno json que contém as informações dos possíveis voos que cumprem os requisitos
    for flight in flight_price["data"]:
        price_list.append(flight["price"])
    try:
        min_price = min(price_list)
        prices[data["iataCode"]] = min_price
        price_list.clear()
        print(f"{flight['cityTo']}: £{min_price}")
        # Se o preço mínimo dos voos futuros forem menores que o preço especificado na planilha, um alerta é enviado
        if data["lowestPrice"] > min_price:
            notificator = NotificationManager(f"Low price alert! Only £{min_price} to fly from {SET_CITY}-"
                                              f"{SET_LOCATION} to {flight['cityTo']}-{data['iataCode']} from "
                                              f"{flight['local_departure'].split('T')[0]}"
                                              f" to {flight['local_arrival'].split('T')[0]}")
            notificator.send()
            # Gera erro caso não haja voos disponíveis, assim o preço mínimo não existiria.
    except ValueError:
        print(f"No flights found for {data['city']}, trying to find flights to {data['city']} with 1 stopover.")
        flight_data_w_stop_over = FlightData(stop_overs=1)
        flight_price_w_stop_over = flight_data_w_stop_over.get_prices(SET_LOCATION, data["iataCode"])

        for flight_stop_over in flight_price_w_stop_over["data"]:
            price_list.append(flight_stop_over["price"])
        try:
            min_price = min(price_list)
            prices[data["iataCode"]] = min_price
            price_list.clear()
            print(f"{flight_stop_over['cityTo']}: £{min_price} w/ stopover at {flight_stop_over['route'][0]['cityTo']}")
            if data["lowestPrice"] > min_price:
                notificator = NotificationManager(f"Low price alert! Only £{min_price} to fly from {SET_CITY}-"
                                                  f"{SET_LOCATION} to {flight['cityTo']}-{data['iataCode']} from "
                                                  f"{flight['local_departure'].split('T')[0]}"
                                                  f" to {flight['local_arrival'].split('T')[0]}\n\nFlight has 1 stop"
                                                  f"over, via {flight_stop_over['route'][0]['cityTo']} city.")
                notificator.send()
        except ValueError:
            print(f"No flights found for {data['city']}")

