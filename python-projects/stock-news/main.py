# ===============================================================
# Stock News
# ===============================================================
import os
import math
import requests
from datetime import date, timedelta
# pip install flask twilio
from twilio.rest import Client

# # 1. RETRIEVE SECRETS FROM GITHUB ENVIRONMENT
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
MY_PHONE_NUMBER = os.environ.get("MY_PHONE_NUMBER")
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()

stock_data = response.json()
time_series = stock_data["Time Series (Daily)"]
sorted_dates = sorted(time_series.keys(), reverse=True)
yesterday_close = float(time_series[sorted_dates[0]]["4. close"])

# 2. - Get the day before yesterday's closing stock price
day_before_yesterday_close = float(time_series[sorted_dates[1]]["4. close"])

# 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = math.floor(abs(yesterday_close - day_before_yesterday_close) * 100) / 100

# 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percent_change = (difference/day_before_yesterday_close) * 100

# 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percent_change > 5:
    # print("Get News")

    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
    today = date.today()
    yesterday = today - timedelta(days=1)

    news_params = {
        "q": COMPANY_NAME,
        "from": yesterday,
        "apikey": NEWS_API_KEY,
    }

    response = requests.get(NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()

    news_data = response.json()


# 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    news_list = news_data["articles"][:3]

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.

# 8. - Create a new list of the first 3 article's headline and description using list comprehension.

# 9. - Send each article as a separate message via Twilio.
client = Client(account_sid, auth_token)
message = client.messages.create(
    body="",
    from_=MY_TWILIO_PHONE_NUMBER,
    to=MY_PHONE_NUMBER,
)
# print(message.body)
print(message.status)


#Optional : Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

