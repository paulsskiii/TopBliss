from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import paths
import credentials

def perform_selection(driver, wait):
    
    try:
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
        # driver.get(credentials.Pancake)



        # print("scrolling down")
        # scrollable_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "rc-virtual-list-holder")))
        # previous_scroll_top = -1  # init with an invalid value
        # while True:
        #     # get current scrollTop value
        #     current_scroll_top = driver.execute_script("return arguments[0].scrollTop;", scrollable_element)
            
        #     # break loop if scrollTop value doesnt change
        #     if current_scroll_top == previous_scroll_top:
        #         print("Reached the bottom of the scrollable element.")
        #         break
            
        #     # scroll down by 3000px
        #     driver.execute_script("arguments[0].scrollTop += 3000;", scrollable_element)
        #     print(f"Scrolled to position: {current_scroll_top}")
            
        #     # upd prev scrollTop value
        #     previous_scroll_top = current_scroll_top
            
        #     # short delay to allow for scroll & update
        #     time.sleep(1)

        # print("Finished scrolling.")

        # # locate the last div with id attribute inside the rc-virtual-list-holder-inner container
        # print("Selecting the last div with an id attribute...")
        # holder_inner = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "rc-virtual-list-holder-inner")))

        # try:
        #     # use xpath to find last div with an id attribute
        #     last_div = holder_inner.find_element(By.XPATH, './div[@id][last()]')
        #     print(f"Last div found with ID: {last_div.get_attribute('id')}")
            
        #     # click last div
        #     last_div.click()
        #     print("Clicked the last div.")
        # except Exception as e:
        #     print(f"An error occurred while selecting the last div: {e}")


        # # chatting part
        # print("Waiting for reply box...")
        # input_box = wait.until(EC.element_to_be_clickable((By.XPATH, paths.reply_box)))
        # input_box.click()
        # input_box.send_keys(message)
        # print(f"Typed message: {message}")

        # # Simulate pressing Enter key
        # input_box.send_keys(Keys.ENTER)
        # print("Pressed Enter.")





        
        # time.sleep(1000000000)
        # print("Selection process completed")
        return True
        
    except Exception as e:
        print(f"An error occurred during the selection process: {e}")
        return False