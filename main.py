from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # ✅ FIX: missing import
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def send_snapchat_message(username, password, message, recipient):
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)

    try:
        driver.get("https://accounts.snapchat.com/accounts/login")

        # Login
        wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(username)
        wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(password)

        # Submit login
        driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)

        # Wait for navigation (this might change; adjust for your actual flow)
        wait.until(EC.url_contains("snapchat.com"))

        # Navigate to chat/profile (may not be directly accessible without challenges)
        driver.get(f"https://story.snapchat.com/@{recipient}")

        # Wait for message input (selector likely to change; update based on your page)
        msg_box = wait.until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Message']"))
        )
        msg_box.send_keys(message)

        # Send (button may be better than ENTER)
        msg_box.send_keys(Keys.RETURN)

        time.sleep(2)

    finally:
        driver.quit()


if __name__ == "__main__":from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"
    send_snapchat_message(
        "your_username",
        "your_password",
        "Hello!",
        "recipient_username"
    )if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
