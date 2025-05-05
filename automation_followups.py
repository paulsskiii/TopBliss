# Import necessary libraries from Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Import variables from external files
import paths
import credentials
# Import the selection module
from selection import perform_selection
from login import perform_login
from chat_followups import perform_chat_followups

# --- Driver Setup ---
# Specify the path to your chromedriver executable
service = Service(executable_path="chromedriver.exe")
# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=service)
# Maximize window
driver.maximize_window()

# --- Selenium Actions ---
try:
    
    driver.get(credentials.Pancake)
    wait = WebDriverWait(driver, 10)

    # login scripts
    perform_login(driver, wait)

    # side bar selection
    perform_selection(driver, wait)

    # chat automation
    perform_chat_followups(driver, wait)

except Exception as e:
    # Print any error that occurs
    print(f"An error occurred during the login process: {e}")

finally:
    # 7. Close the browser window
    # driver.quit() # Uncomment to close browser automatically
    print("Script finished.")