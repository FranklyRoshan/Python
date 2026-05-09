from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep the browser open after the program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the (fake) newsletter registration page
app_brewery = "https://secure-retreat-92358.herokuapp.com/"
driver.get(app_brewery)

# Find the first name, last name, and email fields
# By CLASS_NAME
# first_name = driver.find_element(By.CLASS_NAME, value="top")
# last_name = driver.find_element(By.CLASS_NAME, value="middle")
# email = driver.find_element(By.CLASS_NAME, value="bottom")

# By NAME Tag
first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

# Fill out the form
first_name.send_keys("Franklyn")
last_name.send_keys("Richards")
email.send_keys("franklyn@gmail.com")

# Locate the sign-up button and click on it
# sign_up = driver.find_element(By.CLASS_NAME, value="btn-block")
sign_up = driver.find_element(By.CSS_SELECTOR, value="form button")
sign_up.click()

# driver.close() # closes the currently focused browser tab or window
# driver.quit()  # shuts down the entire WebDriver session and closes all windows