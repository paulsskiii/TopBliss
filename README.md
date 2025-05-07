# 🥞 Topbliss_sel - Pancake Chat Automation

This project automates customer follow-ups on the Pancake platform, especially for contacts **without a number** in the filter. It uses **Selenium WebDriver** to perform browser tasks and automates chat interactions for follow-up messages.

---

# 🚀 Getting Started

To run this Pancake chat automation, follow the steps below:

### 1. 🧾 Clone the Repository

First, clone this repo to your machine:

```bash
git clone https://github.com/yourusername/Topbliss_sel.git
cd Topbliss_sel
```

> Replace `yourusername` with the actual GitHub username or repo link.

---

### 2. 🐍 Install Selenium

Make sure you have Python installed, then install Selenium:

```bash
pip install selenium
```

---

### 3. 🌐 ChromeDriver Setup

This project uses ChromeDriver to control your Chrome browser.

- If `chromedriver.exe` does not work or is incompatible:
  1. Visit [Chrome for Testing](https://googlechromelabs.github.io/chrome-for-testing/)
  2. Download the **ChromeDriver** version that matches your installed Chrome version.
  3. Replace the `chromedriver.exe` file in the project root with the one you downloaded.

> ✅ Be sure your **Chrome version and ChromeDriver version match exactly** to avoid errors.


--

### 4. 🥞 Pancake Extension Setup

To use the Pancake extension with the automation:

1. **Ensure the Pancake extension is installed on your Chrome browser.**  
   - If not installed, download it from the Chrome Web Store:  
     👉 [Pancake V2 Extension](https://chromewebstore.google.com/detail/pancake-v2/oehooocookcnclgniepdgaiankfifmmn?hl=en)

2. **Find the extension ID**:
   - Go to `chrome://extensions/` in your Chrome browser.
   - Click “Details” under the Pancake extension.
   - Look for the **ID** (a long string of letters) and take note of it.

3. **Locate the extension directory on your computer**:
   - Open File Explorer and go to:  
     ```
     C:\Users\<YourUsername>\AppData\Local\Google\Chrome\User Data\Default\Extensions\
     ```
   - Replace `<YourUsername>` with your actual Windows username.
   - Inside this folder, look for the folder name that matches the extension ID you noted earlier.
   - Navigate into that folder and into the version folder inside it.
   - Copy the full path (e.g.,  
     `C:\<user>\<user>\AppData\Local\Google\Chrome\User Data\Default\Extensions\<ID>\2.1.0_0`)

4. **Set the path in the project**:
   - Open the `paths.py` file in the project directory.
   - Replace the value of the `ext_path` variable with the full path you copied:
     ```python
     ext_path = "C:\Users\Paulsskiii\AppData\Local\Google\Chrome\User Data\Default\Extensions\oehooocookcnclgniepdgaiankfifmmn\2.1.0_0"
     ```
   - Make sure the string is prefixed with `r` to avoid issues with backslashes.


---

### 5. ▶️ Run the Automation

Once everything is set up, simply run:

```bash
python main.py
```

--

## 🔧 How It Works

You only need to run the main script:

```bash
python main.py
```

This `main.py` script serves as the **entry point** and orchestrates all other modules in the automation flow.

---

## 📜 Automation Flow

1. **Start with `main.py`**  
   - The central script that initiates the process and connects everything.

2. **`automation_followups.py`**  
   - The "mother" script.
   - Calls `login.py` to access the website.
   - Waits for **manual login** (user inputs credentials).

3. **`login.py`**  
   - Automates the webpage access.
   - Stops at login screen for **manual credential input**.

4. **`selection.py`**  
   - Performs filter selection.
   - Pauses at **calendar selection** for manual date input.
   - Continues when the user clicks OK.

5. **`chat_followups.py`**  
   - Handles the **chat automation** for customer follow-ups.

6. **`promotions.py`**  
   - Contains the **message templates** used in follow-up chats.

7. **Loop Logic**  
   - After initialization, the script runs in a loop until the browser is manually closed:

   ```python
   while True:
       try:
           perform_selection(driver, wait)
           perform_chat_followups(driver, wait)
       except WebDriverException:
           print("Browser closed. Stopping loop.")
           break
   ```

---

## 📁 File Structure

```
Topbliss_sel/
│
├── __pycache__/                  # Python cache files
├── automation_followups.py       # Main automation logic
├── chat_followups.py             # Handles chat replies
├── chromedriver.exe              # WebDriver executable
├── credentials.py                # Manual login credentials
├── login.py                      # Webpage and login automation
├── main.py                       # Entry point for automation
├── paths.py                      # Manages paths (if used)
├── promotions.py                 # Follow-up message templates
├── README.md                     # Project documentation
└── selection.py                  # Filter and selection automation
```

---

## 📌 Notes

- Requires **manual login** and **calendar input**.
- Ensure `chromedriver.exe` matches your Chrome browser version.
- The script will **continuously loop** until the browser is closed manually.
