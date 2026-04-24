<<<<<<< HEAD
# ===============================================================
# Weather API
# ===============================================================

=======
# ===============================================================
# Weather API
# ===============================================================


>>>>>>> e43e5df83aa130f8c1fe9f7bde9ed7b21401d11a
import requests
# pip install flask twilio
from twilio.rest import Client
# import smtplib

MY_LAT = 13.082680 # Your latitude
MY_LON = 80.270721 # Your longitude
COUNT = 4 #

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": WEATHER_API_KEY,
    "cnt": COUNT,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
condition_code = [hour_data["weather"][0]["id"] for hour_data in weather_data["list"]]

will_rain = False
for item in condition_code:
    if item < 700:
        will_rain = True

if will_rain:
    client = Client(TWIILIO_ACCOUTN_SID, TWIILIO_AUTH_TOKEN)
    message = client.messages.create(
        body="It's gonna rain 🌧️ today. Remember to bring an umbrella ☔",
        from_= TWILIO_PHONE_NUMBER,
        to= MY_PHONE_NUMBER,
    )
    # print(message.body)
    print(message.status)

    # # Weather Alert Message via Email
    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(user=MY_EMAIL, password=MY_EMAIL_PASSWORD)
    #     connection.sendmail(
    #         from_addr=MY_EMAIL,
    #         to_addrs=MY_EMAIL,
    #         msg=f"subject: Weather Alert 🌧️ \n\n It's gonna rain 🌧️ today. Remember to bring an umbrella ☔ "
    #     )