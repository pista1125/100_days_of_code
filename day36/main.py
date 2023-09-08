import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

#api key for alphavantage
api_key = "LRUBG2QIUU9JNDFF"

#api key for newsapi
api_key_news = "cd57936e1ce34f338ebbf5dfa354cfbf"

#1. Step: Api call
tesla_url = "https://www.alphavantage.co/query"
tesla_param = {
    "function":"TIME_SERIES_Daily",
    "symbol":STOCK_NAME,
    "apikey": api_key
}

response = requests.get(url=tesla_url, params=tesla_param)
response.raise_for_status()
tesla_data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in tesla_data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

before_yesterday_data = data_list[1]
before_yesterday_closing_price = float(before_yesterday_data["4. close"])

difference = abs(yesterday_closing_price - before_yesterday_closing_price)


diff_percent = (difference / yesterday_closing_price) * 100
if diff_percent >0.2:
    news_params = {
        "apiKey": api_key_news,
        "qInTitle": COMPANY_NAME,
    }
    response_news= requests.get(NEWS_ENDPOINT, params=news_params)
    response_news.raise_for_status()
    articles = response_news.json()["articles"]
    three_articles = articles[:3]
    print(three_articles)
## STEP 2: Use
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.


#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""