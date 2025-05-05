from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import paths
import credentials


def perform_selection(driver, wait):
    
    try:

        wait = WebDriverWait(driver, 5)
        driver.refresh()

        wait = WebDriverWait(driver, 5)
        
        print("clinking messages")
        click_messages = wait.until(EC.element_to_be_clickable((By.XPATH, paths.messages)))
        click_messages.click()

        print("clinking phone no number")
        click_No_phone_number = wait.until(EC.element_to_be_clickable((By.XPATH, paths.No_phone_number)))
        click_No_phone_number.click()

        print("clinking calendar")
        click_calendar = wait.until(EC.element_to_be_clickable((By.XPATH, paths.calendar)))
        click_calendar.click()
        time.sleep(5)


        # put this on the chat_followups for the iteration
        # Wait for OK button to appear
        print("Waiting for OK button to appear...")
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, paths.ok_btn1))
        )
        print("OK button appeared.")

        # Wait for OK button to disappear
        print("Waiting for OK button to disappear...")
        WebDriverWait(driver, 120).until(
            EC.invisibility_of_element((By.XPATH, paths.ok_btn1))
        )
        print("OK button has disappeared. Proceeding...")
        
        # for checking of the ok condition
       
        return True
        
    except Exception as e:
        print(f"An error occurred during the selection process: {e}")
        return False