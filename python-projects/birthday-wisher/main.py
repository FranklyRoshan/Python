##################### Extra Hard Starting Project ######################
import os
import pandas
import smtplib
import random
# import datetime as dt
from datetime import datetime

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_EMAIL_PASSWORD = os.environ.get("MY_EMAIL_PASSWORD")


# today = (dt.datetime.today().day, dt.datetime.today().month)
today = datetime.today()
today_tuple = (today.month, today.day,)

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]) : data_row for (index, data_row) in data.iterrows()}

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if today_tuple in birthdays_dict:
    birthdays_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthdays_person["name"])

# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, to_addrs= birthdays_person["email"],
            msg=f"subject: Happy Birthday {birthdays_person["name"]}!\n\n{contents}"
        )



