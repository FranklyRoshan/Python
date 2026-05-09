# =============================== WEB SCRAPPING ==================================================
from selenium import webdriver
from selenium.webdriver.common.by import By

# keep the browser open after the program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# =============================== Web Scrapping - Amazon's Instant Tea Pot =============================================

# amazon_url = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
# driver.get(amazon_url)
#
# # By.CLASS_NAME (Uses amazon.com websites)
# price_whole = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_fraction = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
#
# if not price_whole or not price_fraction:
#     print("Price not found")
# price = float(price_whole.text.replace(",", "")) + \
#     float(price_fraction.text) / 100
#
# print(f"The is price is {price}")

# =============================== Web Scrapping - python.org ==================================================

python_url = "https://www.python.org/"
driver.get(python_url)

# Locating strategies for a single element
# By.NAME
search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))

# By.ID
button = driver.find_element(By.ID, value="submit")
# print(button.size)

# By.CSS_SELECTION
documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

# By. XPath
bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

# Finding multiple elements
tier_1 = driver.find_elements(By.CLASS_NAME, value="tier-1")
# print(tier_1)

# Challenge: Print the event dates from python.org
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

# Dictionary comprehension
events = {n: {"time": event_times[n].text,"name": event_names[n].text,} for n in range(len(event_times))}

# # Use the Event Name as the Key
# # This is best if every event has a unique name.
# events = {
#     name.text: {"time": time.text}
#     for name, time in zip(event_names, event_times)
# }

# # list comprehension
# events = [
#     {"name": name.text, "time": time.text}
#     for name, time in zip(event_names, event_times)
# ]

# # Conventional way
# events = {}
# for n in range(len(event_times)):
#     events[n] = {
#         "time": event_times[n].text,
#         "name": event_names[n].text,
#     }

print(events)

# driver.close() # closes the currently focused browser tab or window
driver.quit()  # shuts down the entire WebDriver session and closes all windows

# =============================== Built-in Python function - zip() ==================================================
# zip() is a built-in Python function that takes two or more sequences and "zips" them together into pairs.
# Think of it like a mechanical zipper: it aligns the teeth from two different sides into a single track.

# 🛠️ How it works
# It takes the first item from every list and puts them together, then the second items, and so on.

names = ["Alice", "Bob"]
times = ["10:00", "11:00"]

zipped = list(zip(names, times))
# Result: [('Alice', '10:00'), ('Bob', '11:00')]