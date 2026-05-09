# =============================== Selenium (an open-source framework) =============================================
"""
Selenium is an open-source framework and suite of tools for automating web browsers to test web applications across
different browsers, platforms, and programming languages (Java, Python, C#, Ruby, JavaScript). Key components include
Selenium WebDriver for browser interaction, Selenium IDE for record-and-playback, and Grid for parallel execution
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep the browser open after the program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# create and configure the Chrome webdriver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to Wikipedia
wiki_url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(wiki_url)

# =============================== Web Scrapping with selenium =============================================
# By.CSS_SELECTOR
# Hone in one anchor tag using CSS selectors
# active_editors = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
article_count_list = driver.find_elements(By.CSS_SELECTOR, value="#articlecount li")

# List comprehension
counts = [element.text for element in  article_count_list]

# print(f"Wikipedia currently has {counts[0]} and {counts[1]}.")

# ========================== Automated Interaction with browser using selenium =====================================
# By.CSS_SELECTOR
# Hone in one anchor tag using CSS selectors
active_editors = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# print(active_editors.text)

# active_editors.click()

# Find the element by Link Text
content_portal = driver.find_element(By.LINK_TEXT, value="Content portals")
# content_portal.click()

# Click search icon
search_icon = driver.find_element(By.CLASS_NAME, value="mw-ui-icon-wikimedia-search")
search_icon.click()

# Type into search bar
search_bar = driver.find_element(By.CLASS_NAME, value="cdx-text-input__input")
search_bar.send_keys("Python")

# Press Enter
search_bar_has_value = driver.find_element(By.CLASS_NAME, value="cdx-text-input__input--has-value")
search_bar_has_value.send_keys(Keys.ENTER)

# driver.close() # closes the currently focused browser tab or window
driver.quit()  # shuts down the entire WebDriver session and closes all windows