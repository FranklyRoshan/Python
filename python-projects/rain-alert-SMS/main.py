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
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
VIRTUAL_TWILIO_NUMBER = os.environ.get("VIRTUAL_TWILIO_NUMBER")
VERIFIED_NUMBER = os.environ.get("VERIFIED_NUMBER")
# EMAIL_ID = os.environ.get("EMAIL_ID")
# EMAIL_ID_PASSWORD = os.environ.get("EMAIL_ID_PASSWORD")

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
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body="It's gonna rain 🌧️ today. Remember to bring an umbrella ☔",
        from_= VIRTUAL_TWILIO_NUMBER,
        to= VERIFIED_NUMBER,
    )
    # print(message.body)
    print(message.status)

    # # 6. SEND SMS VIA TWILIO MESSAGE VIA EMAIL
    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(user=EMAIL_ID, password=EMAIL_ID_PASSWORD)
    #     connection.sendmail(
    #         from_addr=EMAIL_ID,
    #         to_addrs=EMAIL_ID,
    #         msg=f"subject: Weather Alert 🌧️ \n\n It's gonna rain 🌧️ today. Remember to bring an umbrella ☔ "
    #     )