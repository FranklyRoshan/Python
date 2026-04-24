# ===============================================================
# Weather Alert SMS
# ===============================================================

import os
import requests
# pip install flask twilio
from twilio.rest import Client
# import smtplib

# OpenWeatherMap API 
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast" # 3-hour / 5-day Forecast API
MY_LAT = 13.082680 # Your latitude
MY_LON = 80.270721 # Your longitude
COUNT = 4 # API will return "COUNT" data records, each representing a 3-hour window. 

# 1. RETRIEVE SECRETS FROM GITHUB ENVIRONMENT
WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")
TWIILIO_ACCOUTN_SID = os.environ.get("TWIILIO_ACCOUTN_SID")
TWIILIO_AUTH_TOKEN = os.environ.get("TWIILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER")
MY_PHONE_NUMBER = os.environ.get("MY_PHONE_NUMBER")
# MY_EMAIL = os.environ.get("MY_EMAIL")
# MY_EMAIL_PASSWORD = os.environ.get("MY_EMAIL_PASSWORD")

# 2. WEATHER API CONFIG
weather_params = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": WEATHER_API_KEY,
    "cnt": COUNT,
}

# 3. GET WEATHER DATA
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
condition_code = [hour_data["weather"][0]["id"] for hour_data in weather_data["list"]]

# 4. CHECK FOR RAIN (Codes < 700 are Rain/Snow/Storm)
will_rain = False
for item in condition_code:
    if item < 700:
        will_rain = True

# 5. SEND SMS VIA TWILIO
if will_rain:
    client = Client(TWIILIO_ACCOUTN_SID, TWIILIO_AUTH_TOKEN)
    message = client.messages.create(
        body="It's gonna rain 🌧️ today. Remember to bring an umbrella ☔",
        from_= TWILIO_PHONE_NUMBER,
        to= MY_PHONE_NUMBER,
    )
    # print(message.body)
    print(message.status)

    # # 6. SEND SMS VIA TWILIO MESSAGE VIA EMAIL
    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(user=MY_EMAIL, password=MY_EMAIL_PASSWORD)
    #     connection.sendmail(
    #         from_addr=MY_EMAIL,
    #         to_addrs=MY_EMAIL,
    #         msg=f"subject: Weather Alert 🌧️ \n\n It's gonna rain 🌧️ today. Remember to bring an umbrella ☔ "
    #     )