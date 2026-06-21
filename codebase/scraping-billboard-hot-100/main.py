from urllib import response

import requests
from datetime import datetime
from fake_useragent import UserAgent
URL = "https://www.billboard.com/charts/hot-100/"

ua = UserAgent()
headers = {'User-Agent' : ua.random}

response = requests.get(URL, headers=headers)
status = response.status_code
# print(response.text)

# Key Points
# Use strptime() to parse a string into a datetime.
# Use strftime() to format a datetime into a string.

date_string = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
date_object = datetime.strptime(date_string, "%Y-%m-%d").date()
print(date_object)

