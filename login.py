from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import paths
import credentials

def perform_login(driver, wait):
    
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

    print("Manual Login Required")
    WebDriverWait(driver, 10000).until(
        EC.presence_of_element_located((By.XPATH, paths.condition))
    )
    
    try:
        
        return True
        
    except Exception as e:
        print(f"An error occurred during the selection process: {e}")
        return False