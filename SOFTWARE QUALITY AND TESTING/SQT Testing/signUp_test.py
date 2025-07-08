from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

driver = webdriver.Chrome()

driver.get("http://127.0.0.1/project/view/opi_features/auth_feature/signup.html")
driver.maximize_window()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "name")))

rand_num = random.randint(1000, 9999)
test_name = f"testuser"
test_email = f"test{rand_num}@example.com"
test_password = "testpass123"

driver.find_element(By.ID, "name").send_keys(test_name)
driver.find_element(By.ID, "email").send_keys(test_email)
driver.find_element(By.ID, "password").send_keys(test_password)
driver.find_element(By.ID, "confirm_password").send_keys(test_password)
driver.find_element(By.ID, "type1").click()  

driver.save_screenshot("C:/Users/ASUS/Pictures/SS/signup_before_submit.png")
print('Screenshot saved: "signup_before_submit.png"')

submit_button = driver.find_element(By.XPATH, "//input[@type='submit' and @name='signup']")
submit_button.click()

time.sleep(3) 

driver.save_screenshot("C:/Users/ASUS/Pictures/SS/signup_after_submit.png")
print('Screenshot saved: "signup_after_submit.png"')

driver.quit()
