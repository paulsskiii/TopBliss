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

# --- Driver Setup ---
# Specify the path to your chromedriver executable
service = Service(executable_path="chromedriver.exe")
# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=service)
# Maximize window
driver.maximize_window()

# --- Selenium Actions ---
try:
    wait = WebDriverWait(driver, 10)

   
    print("clinking messages")
    click_messages = wait.until(EC.element_to_be_clickable((By.XPATH, paths.messages)))
    click_messages.click()

    
    print("clinking phone no number")
    click_No_phone_number = wait.until(EC.element_to_be_clickable((By.XPATH, paths.No_phone_number)))
    click_No_phone_number.click()

    print("clinking calendar")
    click_calendar = wait.until(EC.element_to_be_clickable((By.XPATH, paths.calendar)))
    click_calendar.click()


    time.sleep(100000)

except Exception as e:
    # Print any error that occurs
    print(f"An error occurred during the login process: {e}")

finally:
    # 7. Close the browser window
    # driver.quit() # Uncomment to close browser automatically
    print("Script finished.")

