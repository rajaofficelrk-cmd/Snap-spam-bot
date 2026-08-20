# Snapchat Spam Bot

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Function to send messages
def send_snapchat_message(username, password, message, recipient):
    driver = webdriver.Chrome()  # Ensure you have the ChromeDriver installed
    driver.get("https://accounts.snapchat.com/accounts/login")

    time.sleep(2)

    # Log in to Snapchat
    username_input = driver.find_element_by_name("username")
    password_input = driver.find_element_by_name("password")

    username_input.send_keys(username)
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)

    time.sleep(5)

    # Navigate to the chat
    driver.get(f"https://story.snapchat.com/{recipient}")

    time.sleep(2)

    # Send the message
    message_input = driver.find_element_by_xpath("//textarea[@placeholder='Message']")
    message_input.send_keys(message)
    message_input.send_keys(Keys.RETURN)

    time.sleep(2)

    driver.quit()

# Example usage
if __name__ == "__main__":
    USERNAME = "your_username"
    PASSWORD = "your_password"
    MESSAGE = "Hello! This is a spam message."
    RECIPIENT = "recipient_username"

    for _ in range(10):  # Send the message 10 times
        send_snapchat_message(USERNAME, PASSWORD, MESSAGE, RECIPIENT)
        time.sleep(5)  # Wait 5 seconds between messages
