# plane b: manual scroll then there is a checker when it sees the message feild then it will get the relative xpath and get the id of it to be the stopper and the automation will continuefrom selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import paths
import credentials
import promotions



def perform_chat_followups(driver, wait):
        

        print("scrolling down")
        scrollable_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "rc-virtual-list-holder")))
        previous_scroll_top = -1  # init with an invalid value
        while True:
            # get current scrollTop value
            current_scroll_top = driver.execute_script("return arguments[0].scrollTop;", scrollable_element)
            
            # break loop if scrollTop value doesnt change
            if current_scroll_top == previous_scroll_top:
                print("Reached the bottom of the scrollable element.")
                break
            
            # scroll down by 3000px
            driver.execute_script("arguments[0].scrollTop += 3000;", scrollable_element)
            print(f"Scrolled to position: {current_scroll_top}")
            
            # upd prev scrollTop value
            previous_scroll_top = current_scroll_top
            
            # short delay to allow for scroll & update
            time.sleep(1)

        print("Finished scrolling.")

        # locate the last div with id attribute inside the rc-virtual-list-holder-inner container
        print("Selecting the last div with an id attribute...")
        holder_inner = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "rc-virtual-list-holder-inner")))


#  -------------------------------------
        chat_stopper = None

        while True:
            try:
                # Find the last div with an id attribute
                last_div = holder_inner.find_element(By.XPATH, './div[@id][last()]')
                last_div_id = last_div.get_attribute('id')
                print(f"Last div found with ID: {last_div_id}")

                # Break the loop if we've reached the stopper
                if last_div_id == chat_stopper:
                    print("Reached the stopper. Ending loop.")
                    break

                # Update the stopper value on the first iteration
                if chat_stopper is None:
                    chat_stopper = last_div_id
                    print(f"Initial stopper set to: {chat_stopper}")

                # Click the last div
                last_div.click()
                print("Clicked the last div.")

                # Chatting part
                print("Waiting for reply box...")
                input_box = wait.until(EC.element_to_be_clickable((By.XPATH, paths.reply_box)))
                input_box.click()
                input_box.send_keys(promotions.reply_promotion1)
                print(f"Typed message: {promotions.reply_promotion1}")

                # Simulate pressing Enter key twice
                input_box.send_keys(Keys.ENTER)
                print("Pressed Enter to load the promotion details")
                time.sleep(2)
                print("Enter again to send")
                input_box.send_keys(Keys.ENTER)

                # Optional delay before moving to the next div
                time.sleep(4)

            except Exception as e:
                print(f"An error occurred: {e}")
                break


        # add time stop

        # time.sleep(1000000000)

        try:
            
            return True
            
        except Exception as e:
            print(f"An error occurred during the selection process: {e}")
            return False