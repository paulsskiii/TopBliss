import os
import glob

login_button_xpath = "//button[@class='index-button index-button-primary header-login-button']"
email_field_xpath = "//*[@id='email']"
password_field_xpath = "//*[@id='pass']"
submit_button_xpath = "//*[@id='loginbutton']"



reconnect_button = '//*[@id="platformDialogForm"]/div/div[1]/div/div/div/div[2]/div/div[3]/div/div[2]/div[2]/div[2]/div'
EasebrewCare = '//*[@id="__next"]/div/div[1]/div[2]/div/div[2]/div[3]/div/div/div[1]/div[1]/div/div/div[8]/a/div/div[1]'
EasaBrew_Herbal_Coffee = '//*[@id="__next"]/div/div[1]/div[2]/div/div[2]/div[3]/div/div/div[1]/div[1]/div/div/div[4]/a/div/div[1]'

condition = '//*[@id="__next"]/div/div[1]/div[2]/div/div/div/div[1]/ul/li[1]'
messages = '//*[@id="__next"]/div/div[1]/div[2]/div/div/div/div[1]/ul/li[4]'
No_phone_number = '//*[@id="__next"]/div/div[1]/div[2]/div/div/div/div[1]/ul/li[7]'
calendar = '//*[@id="__next"]/div/div[1]/div[2]/div/div/div/div[1]/ul/div[1]/li'
scrollbar = '//*[@id="conversationList"]/div[1]'
ok_btn1 = '/html/body/div[3]/div/div[2]/div/div[2]/div/div[2]/button[2]'
reply_box = '//*[@id="replyBoxComposer"]'
send_btn = '//*[@id="reply_box"]/div[1]/div[2]/div/div[2]/div/span[1]'
SecondToTheLastchat =''
firstToTheLastchat =''
Lastchat = './div[@id][last()]'
chat_send_button = '//*[@id="reply_box"]/div[1]/div[2]/div/div[2]/div/span[1]'


# to include the extension path this will change

base_ext_path = r'C:\Users\Paulsskiii\AppData\Local\Google\Chrome\User Data\Default\Extensions\oehooocookcnclgniepdgaiankfifmmn'
version_folders = glob.glob(os.path.join(base_ext_path, '*'))

if not version_folders:
    raise FileNotFoundError(f"No version folders found inside {base_ext_path}. Please check the path and extension ID.")

latest_version_folder = max(version_folders, key=os.path.getmtime)

ext_path = latest_version_folder.replace('/', '\\')
print(f"ext_path = '{ext_path}'")
  

name_xpath = '//*[@id="pageCustomer"]/div/span'
page_xpath = '//*[@id="__next"]/div/div[2]/nav/div/div[2]/ul[2]/li[2]/a/div[1]/span/div'