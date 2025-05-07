# Import necessary libraries from Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

# Import variables from external files
import paths
import credentials
# Import the selection module
from selection import perform_selection
from login import perform_login
from chat_followups import perform_chat_followups
ext_path = paths.ext_path

chrome_options = Options()
chrome_options.add_argument(f'--load-extension={paths.ext_path}')
                
# --- Driver Setup ---
# Specify the path to your chromedriver executable
service = Service(executable_path="chromedriver.exe")
# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=service,options=chrome_options)
# Maximize window
driver.maximize_window()
actions = ActionChains(driver)

# --- Selenium Actions ---
try:
    
    driver.get(credentials.Pancake)
    wait = WebDriverWait(driver, 100000)

    # login scripts
    perform_login(driver, wait)

    while True:
        try:
            # side bar selection
            perform_selection(driver, wait)

            # chat automation
            perform_chat_followups(driver, wait)

        except WebDriverException:
            print("Browser closed. Stopping loop.")
            break  # Exit loop when browser is closed

except Exception as e:
    # Print any error that occurs
    print(f"An error occurred during the login process: {e}")

finally:
    # 7. Close the browser window
    # driver.quit() # Uncomment to close browser automatically
    print("Script finished.")