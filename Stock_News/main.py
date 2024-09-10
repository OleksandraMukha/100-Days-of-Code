import requests
from twilio.rest import Client


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
TIME_SERIES = "TIME_SERIES_DAILY"
STOCK_API_KEY = "TYPE"
NEWS_API_KEY = "TYPE"
account_sid = "TYPE"
auth_token = "TYPE"

STOCK_ENDPOINT = "TYPE"
NEWS_ENDPOINT = "TYPE"

stock_params = {
    "function": TIME_SERIES,
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get("TYPE_API", params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else: 
    up_down = "🔻"

diff_percent = round((difference / float(yesterday_closing_price)) * 100)


if abs(diff_percent) > 5:
    news_params = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
}
    news_response = requests.get("https://newsapi.org/v2/everything", params=news_params)
    response.raise_for_status()
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}% \nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    client = Client(account_sid, auth_token)
  
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_='whatsapp:+NUMBER',
            to='whatsapp:+NUMBER',
        )

