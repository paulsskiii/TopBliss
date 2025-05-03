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
    # 1. Open the target URL (from credentials.py)
    print(f"Navigating to: {credentials.Pancake}")
    driver.get(credentials.Pancake)

    # --- Wait for and interact with elements ---
    # Use WebDriverWait for robustness (wait up to 10 seconds)
    wait = WebDriverWait(driver, 10)

    # 2. Click the initial login button on the header (XPath from paths.py)
    print("Waiting for header login button...")
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, paths.login_button_xpath)))
    login_button.click()
    print("Clicked header login button.")

    # # 3. Input email (XPath from paths.py, email from credentials.py)
    # print("Waiting for email field...")
    # email_field = wait.until(EC.visibility_of_element_located((By.XPATH, paths.email_field_xpath)))
    # email_field.send_keys(credentials.username)
    # print("Entered email.")

    # # 4. Input password (XPath from paths.py, password from credentials.py)
    # print("Waiting for password field...")
    # password_field = wait.until(EC.visibility_of_element_located((By.XPATH, paths.password_field_xpath)))
    # password_field.send_keys(credentials.password)
    # print("Entered password.")

    # # 5. Click the final login button (XPath from paths.py)q
    # print("Waiting for submit button...")
    # submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, paths.submit_button_xpath)))
    # submit_button.click()
    # print("Clicked final login button.")

    # 6. (Optional) Wait to observe the result
    print("Login attempt submitted. Pausing for 10 seconds...")
    time.sleep(10)


    WebDriverWait(driver, 10000).until(
    EC.presence_of_element_located((By.XPATH, paths.condition))
)
    
    
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

