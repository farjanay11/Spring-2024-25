from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://127.0.0.1/project2/view/auth_feature/signin.html")
driver.maximize_window()
time.sleep(2)  

username_input = driver.find_element(By.ID, "username")
password_input = driver.find_element(By.ID, "password")
submit_button = driver.find_element(By.XPATH, "//input[@type='submit' and @name='login']")

username_input.send_keys("advertiser")     
password_input.send_keys("123456")

submit_button.click()
time.sleep(3)  

current_url = driver.current_url
print("Current URL after login attempt:", current_url)

if "menu" in current_url:
    screenshot_name = "login_successful.png"
    print("Login successful")
else:
    screenshot_name = "login_failed.png"
    print("Login failed")

screenshot_path = f"C:/Users/ASUS/Pictures/SS/{screenshot_name}"
driver.save_screenshot(screenshot_path)
print(f"Screenshot saved as: {screenshot_path}")

driver.quit()
