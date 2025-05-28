# Import necessary libraries
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import WebDriverException
import os
import time

# Import external variables and modules
import paths
import credentials
from selection import perform_selection
from login import perform_login
from chat_followups import perform_chat_followups

# --- Get Extension Path ---
ext_path = paths.ext_path  # Should point to an unpacked folder with manifest.json

# --- Debug: Validate Extension Path ---
if not os.path.exists(ext_path):
    raise FileNotFoundError(f"Extension path not found: {ext_path}")
elif not os.path.exists(os.path.join(ext_path, "manifest.json")):
    raise FileNotFoundError(f"No manifest.json in extension folder: {ext_path}")
else:
    print(f"[INFO] Extension loaded from: {ext_path}")

# --- Setup Chrome Options ---
chrome_options = uc.ChromeOptions()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-blink-features=AutomationControlled')

# ✅ Important fix: Also use --disable-extensions-except
chrome_options.add_argument(f'--load-extension={ext_path}')
chrome_options.add_argument(f'--disable-extensions-except={ext_path}')  # Optional but helps

# --- Initialize Undetected Chrome Driver ---
driver = uc.Chrome(options=chrome_options, headless=False)  # headless=False is required
driver.maximize_window()
actions = ActionChains(driver)

# --- Selenium Actions ---
try:
    driver.get("chrome://extensions/")  # First, verify if extension shows up
    time.sleep(5)  # Pause so you can check it visually

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
