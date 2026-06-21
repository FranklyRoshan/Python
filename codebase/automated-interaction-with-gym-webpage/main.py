import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import NoSuchElementException, ElementNotInteractableException

# ----------------  Step 1 - Setup, Chrome Profile and Basic Navigation ----------------
# Create Chrome Profile and create account manually.
load_dotenv()
ACCOUNT_EMAIL = os.environ.get("ACCOUNT_EMAIL")
ACCOUNT_PASSWORD = os.environ.get("ACCOUNT_PASSWORD")
GYM_URL = "https://appbrewery.github.io/gym/"

chrome_options = webdriver.ChromeOptions()
# keep the browser open after the program finishes
# If True, you need to *manually* QUIT Chrome before you re-run the script.
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

# create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to gym website
driver.get(GYM_URL)

# ----------------  Step 2 - Automated Login ----------------
# Wait for page to load just in case
# sleep(2)
errors = [NoSuchElementException, ElementNotInteractableException]
wait = WebDriverWait(driver, timeout=2, poll_frequency=.2, ignored_exceptions=errors)

# Click on login button
login_button = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "#login-button")))
login_button.click()

# Type login credentials into the fields
email_input = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "#email-input")))
email_input.clear()
email_input.send_keys(ACCOUNT_EMAIL)
assert email_input.get_property("value") == ACCOUNT_EMAIL

password_input = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "#password-input")))
password_input.clear()
password_input.send_keys(ACCOUNT_PASSWORD)

# Press login button(submit-button)
submit_button = driver.find_element(By.CSS_SELECTOR, value="#submit-button")
submit_button.click()

# Wait for schedule page to load
wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))

# ----------------  Step 3 - Class Booking: Book Upcoming Tuesday Class  ----------------



# driver.close() # closes the currently focused browser tab or window
# driver.quit()  # shuts down the entire WebDriver session and closes all windows