import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def send_snapchat_message(username, password, message, recipient):
    driver = webdriver.Chrome()
    driver.get("https://accounts.snapchat.com/accounts/login")
    wait = WebDriverWait(driver, 10)

    # Login
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "password").send_keys(Keys.RETURN)

    # Wait for login to complete
    wait.until(EC.url_contains("https://story.snapchat.com/"))

    # Navigate to chat (use correct URL pattern)
    driver.get(f"https://story.snapchat.com/@{recipient}")
    wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder='Message']"))).send_keys(message)
    driver.find_element(By.XPATH, "//textarea[@placeholder='Message']").send_keys(Keys.RETURN)

    time.sleep(2)
    driver.quit()

# Example (single send – do not loop for spam)
if __name__ == "__main__":
    send_snapchat_message("your_username", "your_password", "Hello!", "recipient_username")
