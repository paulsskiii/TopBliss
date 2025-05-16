# Import necessary libraries
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
import time

# Import external variables and modules
import paths
import credentials
from selection import perform_selection
from login import perform_login
from chat_followups import perform_chat_followups

ext_path = paths.ext_path  # Ensure this is an absolute path to an **unpacked** extension

# --- Setup Chrome Options ---
chrome_options = uc.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_argument(f'--load-extension={ext_path}')  # 👈 Unpacked extension folder

# --- Initialize Undetected Chrome Driver ---
driver = uc.Chrome(options=chrome_options, headless=False)  # headless=True disables extension GUI
driver.maximize_window()
actions = ActionChains(driver)

# --- Selenium Actions ---
try:
    driver.get(credentials.Pancake)
    wait = WebDriverWait(driver, 100000)

    # login
    perform_login(driver, wait)

    while True:
        try:
            perform_selection(driver, wait)
            perform_chat_followups(driver, wait)
        except WebDriverException:
            print("Browser closed. Stopping loop.")
            break

except Exception as e:
    print(f"An error occurred during the login process: {e}")

finally:
    print("Script finished.")
    # driver.quit()  # Uncomment if you want to close the browser
