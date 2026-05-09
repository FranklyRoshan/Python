from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep, time

# keep the browser open after the program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/cookieclicker/")

# Wait for page to load just in case
sleep(3)

# Handle initial popups (cookies consent doesn't have to be clicked, but language does)
print("Looking for language selection...")
try:
    # Select English language
    # lang = driver.find_element(By.ID, value="langSelect-EN")
    lang = driver.find_element(By.CSS_SELECTOR, value="#langSelect-EN")
    print(f'Found the "{lang.text}" language button, Clicking...')
    lang.click()
    sleep(3)
except NoSuchElementException:
    print("Language selection not found")

# wait for everything to settle
sleep(2)

# Find the big cookies to click
cookie = driver.find_element(By.ID, value="bigCookie")

# Get all store items (products 0-19)
item_ids = [f"product{i}" for i in range(20)]

# set timers
wait_time = 5
timeout = time() + wait_time # Check for purchases every 5 seconds
five_mins = time() + 60 * 5 # Run for 5 minutes

while True:
    cookie.click()

    if time() > five_mins:
        try:
            # Get current cookie count
            cookies_elements = driver.find_element(By.ID, value="cookies")
            cookie_text = cookies_elements.text
            # Extract number form text like "123 cookies"
            cookie_count = int(cookie_text.strip()[0].replace(",",""))

            """
            CSS Attribute Selectors
            Selector	    Meaning
            [id='abc']	    exact match
            [id^='abc']	    starts with
            [id$='abc']	    ends with
            [id*='abc']	    contains
            """

            # Find all available products in the store
            products =  driver.find_elements(By.CSS_SELECTOR, value="div[id^='product']")

            # Find the most expensive item we can afford
            best_item = None
            for product in reversed(products): # Start from most expensive (bottom of list)
                # check if item is available and affordable (enabled class)
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break

            # Buy the best item if found
            if best_item:
                best_item.click()
                print(f"Bought item: {best_item.get_attribute('id')}")

        except (NoSuchElementException, ValueError):
            print("Couldn't find cookie count or items")

        # Reset timer
        timeout = time() + wait_time

    # stop after 5 minutes
    if time() > five_mins:
        try:
            cookies_elements = driver.find_element(By.ID, value="cookies")
            print(f"Final result: {cookies_elements.text}")
        except NoSuchElementException:
            print("couldn't get final cookie count")
        break

# driver.close() # closes the currently focused browser tab or window
# driver.quit()  # shuts down the entire WebDriver session and closes all windows
