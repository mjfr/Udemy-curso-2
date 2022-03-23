import requests
from bs4 import BeautifulSoup
import os

ENDPOINT_TELEGRAM = "https://api.telegram.org/bot"
BOT_TOKEN = os.environ["BOT_TOKEN"]
BOT_CHAT_ID = os.environ["BOT_CHAT_ID"]
STANDARD_PRICE_TEST = 400.00
PRODUCT_URL = "https://www.amazon.com.br/dp/B084DWCZY6/ref=pav_d_fromAsin_B07PDHSJ1H_toAsin_B084DWCZY6"
AMAZON_HEADERS = {
    "Accept-Language": "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46"
}
amazon_response = requests.get(url=PRODUCT_URL, headers=AMAZON_HEADERS)
markup = amazon_response.text

soup = BeautifulSoup(markup=markup, parser="lxml")
product_title = soup.find(name="span", id="productTitle").getText()
whole_price = float(soup.find(name="span", class_="a-price-whole").getText().replace(".", "").replace(",", ""))
fraction_price = float(soup.find(name="span", class_="a-price-fraction").getText())
float_price = whole_price + fraction_price

TELEGRAM_PARAMS = {
    "chat_id": BOT_CHAT_ID,
    "text": f"Parece que um produto que você mostrou interesse está com um desconto agora.\nProduto: {product_title}\n"
            f"Valor:R$%.2f\nLink: {PRODUCT_URL}" % whole_price,
    "parse_mode": "HTML"
}


def telegram_price_messenger_bot():
    response_telegram = requests.get(url=f"{ENDPOINT_TELEGRAM}{BOT_TOKEN}/sendMessage", params=TELEGRAM_PARAMS)
    return response_telegram.json()


if float_price <= STANDARD_PRICE_TEST:
    telegram_price_messenger_bot()


# Um possível 'upgrade' seria hospedar o bot no site https://www.pythonanywhere.com/, criar um cronograma de execução e
# substituir as constantes PRODUCT_URL e STANDARD_PRICE_TEST por um dicionário que guardaria o produto, url e valor
# assim o app ficaria mais automatizado e haveria a opção de expansibilidade. Claro, adicionando as possíveis operações
# como pesquisar os produtos cadastrados, excluir os produtos cadastrados etc.
