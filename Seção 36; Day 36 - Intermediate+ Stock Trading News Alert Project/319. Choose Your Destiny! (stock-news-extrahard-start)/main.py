import requests
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]
ENDPOINT_TELEGRAM = "https://api.telegram.org/bot"
ALPHAVANTAGE_API_KEY = os.environ["ALPHAVANTAGE_API_KEY"]
ALPHAVANTAGE_PARAMETERS = {
    "function": "TIME_SERIES_DAILY",  # TIME_SERIES_XXXX --> INTRADAY, WEEKLY, MONTHLY are alternatives
    "symbol": STOCK,
    "outputsize": "compact",  # full is an alternative, way bigger data
    "datatype": "json",  # csv is an alternative
    "apikey": ALPHAVANTAGE_API_KEY
}
ALPHAVANTAGE_ENDPOINT = "https://www.alphavantage.co/query"
NEWSAPI_KEY = os.environ["NEWSAPI_KEY"]
NEWSAPI_PARAMETERS = {
    "q": COMPANY_NAME,
    "apiKey": NEWSAPI_KEY
}
NEWSAPI_ENDPOINT = "https://newsapi.org/v2/everything"


def calculate_percentage() -> dict:
    alphavantage_response = requests.get(url=ALPHAVANTAGE_ENDPOINT, params=ALPHAVANTAGE_PARAMETERS)
    alphavantage_response.raise_for_status()
    alphavantage_json = alphavantage_response.json()
    daily_data = alphavantage_json["Time Series (Daily)"]
    date_list = list(daily_data)[0:2]
    yesterday = date_list[0]
    before_yesterday = date_list[1]
    yesterday_close = float(daily_data[yesterday]["4. close"])
    before_yesterday_close = float(daily_data[before_yesterday]["4. close"])
    percentage = ((yesterday_close * 100) / before_yesterday_close) - 100

    return {
        "is_over_five": -5 >= percentage or 5 <= percentage,
        "is_percentage_positive": percentage >= 0,
        "percentage": percentage,
        "rounded_percentage": round(percentage, 2),
        "yesterday_date": yesterday,
        "before_yesterday_date": before_yesterday
    }


def get_news() -> list:
    newsapi_response = requests.get(url=NEWSAPI_ENDPOINT, params=NEWSAPI_PARAMETERS)
    newsapi_response.raise_for_status()
    newsapi_json = newsapi_response.json()
    newsapi_articles = newsapi_json["articles"]
    first_three_articles = [
        {
            "title": content["title"],
            "description":content["description"],
            "url": content["url"]
        }
        for content in newsapi_articles[0:3]
    ]

    return first_three_articles


def send_to_telegram(bot_message) -> None:
    response_telegram = requests.get(url=f"{ENDPOINT_TELEGRAM}{TELEGRAM_BOT_TOKEN}"
                                         f"/sendMessage?chat_id={TELEGRAM_CHAT_ID}"
                                         f"&parse_mode=Markdown&text={bot_message}")
    response_telegram.raise_for_status()


def message_formatter() -> None:
    stock_dict = calculate_percentage()
    articles_list = get_news()

    def high_low() -> str:
        high_low_symbol = {"high": "🔼", "low": "🔽"}
        if stock_dict["is_percentage_positive"]:
            return high_low_symbol["high"]
        return high_low_symbol["low"]

    def article_separation() -> str:
        separated_articles = [
            f"\n\n\nHeadline: {article['title']}\nBrief: {article['description']}\nFont: {article['url']}"
            for article in articles_list
        ]
        to_string = " ".join([str(article_from_list) for article_from_list in separated_articles])
        escaped_to_string = to_string.replace("_", "\_").replace("#", "\#").replace("&", "\&").replace("*", "\*")\
            .replace("[", "\[").replace("`", "\`").replace("+", "\+")
        return escaped_to_string

    if stock_dict["is_over_five"]:
        return send_to_telegram(f'{STOCK}: {high_low()} {stock_dict["rounded_percentage"]}%\n{article_separation()}')


message_formatter()
