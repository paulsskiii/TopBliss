from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import paths
import credentials
import promotions
import random

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

    # -------------------------------------
    chat_stopper = None

    def random_delay(min_delay=1, max_delay=3):
        """Generate a random delay between min_delay and max_delay."""
        return random.uniform(min_delay, max_delay)

    def randomize_text():
        """Generate a random string for randomization purposes."""
        random_letters = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=random.randint(2, 5)))
        return random_letters

    def type_with_randomization(input_box, base_text):
        """Simulate typing with randomization AFTER the base message."""
        # Step 1: Type the actual message
        input_box.send_keys(base_text)
        print(f"Typed actual message: {base_text}")
        time.sleep(random_delay(0.5, 1.5))  # Delay after typing the message

        # Step 2: Type random string after the message
        random_string = randomize_text()
        input_box.send_keys(random_string)
        print(f"Typed random string: {random_string}")
        time.sleep(random_delay(0.5, 1.5))  # Delay after typing random string

        # Step 3: Delete the random string typed
        input_box.send_keys(Keys.BACKSPACE * len(random_string))
        print(f"Deleted random string: {random_string}")
        time.sleep(random_delay(0.5, 1.5))  # Delay after deleting random string

    def perform_action(input_box, message):
        """Perform the full sequence: random string, typing, deleting, and pressing Enter."""
        # Simulate typing with randomization
        type_with_randomization(input_box, message)

        # Simulate pressing Enter key twice with random delays
        input_box.send_keys(Keys.ENTER)
        print("Pressed Enter to load the promotion details")
        time.sleep(random_delay(1, 3))  # Random delay before second Enter
        
        input_box.send_keys(Keys.ENTER)
        print("Pressed Enter again to send")
        time.sleep(random_delay(1, 3))  # Delay before moving on to the next action

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

            # Simulate typing and interaction with randomization
            random_message = promotions.reply_promotion1  # Your base message here
            perform_action(input_box, random_message)
            # time.sleep(10000)

            # Optional delay before moving to the next div
            time.sleep(random_delay(2, 4))

        except Exception as e:
            print(f"An error occurred: {e}")
            break

    try:
        return True
    except Exception as e:
        print(f"An error occurred during the selection process: {e}")
        return False
