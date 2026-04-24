# ===============================================================
# ISS pass alert
# ===============================================================
import requests
import smtplib
import time
import os
from datetime import datetime
from zoneinfo import ZoneInfo

MY_LAT = 13.072090 # Your Latitude
MY_LNG = 80.201859 # Your Longitude
EMAIL_ID = os.environ.get("EMAIL_ID")
EMAIL_ID_PASSWORD = os.environ.get("EMAIL_ID_PASSWORD")


def is_iss_overhead():
    """Check if the ISS position is within a 5° radius of your location."""
    # ISS API
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    # status_code = iss_response.status_code
    iss_response.raise_for_status()

    iss_data = iss_response.json()
    # data_iss_position = response.json()["iss_position"]
    # data_longitude = response.json()["iss_position"]["longitude"]

    # Convert String to Float data type
    iss_latitude = float(iss_data["iss_position"]["latitude"])
    iss_longitude = float(iss_data["iss_position"]["longitude"])

    # Your Position is within ±5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LNG-5<= iss_longitude <= MY_LNG+5:
        return True
    else:
        return False

def is_night():
    """Check if it is nighttime."""
    # Sunset and sunrise times API
    parameter = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
    response.raise_for_status()

    data = response.json()
    # https://api.sunrise-sunset.org/json?lat=13.072090&lng=80.201859

    # UTC to IST
    # 1. install tzdata package using pip
    # 2. Input ISO 8601 UTC string
    iso_utc_sunrise = data["results"]["sunrise"]
    # 3. Parse the string into a datetime object
    utc_sunrise = datetime.fromisoformat(iso_utc_sunrise)
    # 4. Convert to IST
    ist_sunrise = utc_sunrise.astimezone(ZoneInfo("Asia/Kolkata"))
    # 5. Convert IST to hour (Integer data type)
    sunrise = ist_sunrise.hour
    # print(sunrise)

    # Similarly for Sunset from UTC to IST hour
    iso_utc_sunset = data["results"]["sunset"]
    utc_sunset = datetime.fromisoformat(iso_utc_sunset)
    ist_sunset = utc_sunset.astimezone(ZoneInfo("Asia/Kolkata"))
    sunset = ist_sunset.hour
    # print(sunset)

    # Realtime hour
    hour = datetime.now().hour # Integer data type
    # print(now)

    if sunset <= hour <= sunrise:
        return True
    else:
        return False

# Email me to tell me to "look up"

# Disabled: Prevents sending duplicate emails in GitHub Actions workflows
# while True:
#    time.sleep(60)

if is_iss_overhead() and is_night():
    with smtplib.SMTP("smtp.gmail.com") as connection: 
        connection.starttls()
        connection.login(user=EMAIL_ID, password=EMAIL_ID_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_ID,
            to_addrs= EMAIL_ID,
            msg=f"subject: Look up👆 \n\n The ISS is above you in the sky"
        )


