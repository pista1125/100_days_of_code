import requests
from twilio.rest import Client


STOCK_NAME = "XRP"
COMPANY_NAME = "RIPPLE"

kripto_url = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

#api key for alphavantage
api_key = "LRUBG2QIUU9JNDFF"

#api key for newsapi
api_key_news = "cd57936e1ce34f338ebbf5dfa354cfbf"

#api key for sms sending
account_sid = 'ACc9759d9b6afb3e259a72127956af0c4a'
auth_token = '6d24935aac1ef8f19ea13e5ba9cf53f5'

def sending_sms(text):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+14327772526',
        body=text,
        to='+36307270793'
    )

#1. Step: Api call
kripto_param = {
    "function":"DIGITAL_CURRENCY_DAILY",
    "symbol":STOCK_NAME,
    "market": "EUR",
    "apikey": api_key
}

response = requests.get(url=kripto_url, params=kripto_param)
response.raise_for_status()
kripto_data= response.json()['Time Series (Digital Currency Daily)']

data_list = [value for (key, value) in kripto_data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4a. close (EUR)"])

before_yesterday_data = data_list[1]
before_yesterday_closing_price = float(before_yesterday_data["4a. close (EUR)"])

difference = yesterday_closing_price - before_yesterday_closing_price
diff_percent = round((difference / yesterday_closing_price) * 100, 2)

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
#2. checking that need search news:
if abs(diff_percent) > 5:
    pass
news_params = {
    "apiKey": api_key_news,
    "qInTitle": COMPANY_NAME,
}
response_news= requests.get(NEWS_ENDPOINT, params=news_params)
response_news.raise_for_status()
articles = response_news.json()["articles"]
three_articles = articles[:3]

#3. Sending sms from text

sms_text = [f" Stock name: {STOCK_NAME}: {up_down} {diff_percent}Headline: {article['title']} \nBrief: {article['description']} \n" for article in three_articles]
for x in range(3):
    sending_sms(sms_text[x])
