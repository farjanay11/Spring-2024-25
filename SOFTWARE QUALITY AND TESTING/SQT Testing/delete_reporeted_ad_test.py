from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

driver = webdriver.Chrome()

driver.get("http://127.0.0.1/project/view/opi_features/auth_feature/signin.html")
driver.maximize_window()
time.sleep(3)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "name")))
driver.find_element(By.ID, "name").send_keys("adminadmin")    
driver.find_element(By.ID, "password").send_keys("110918")  
driver.find_element(By.XPATH, "//input[@type='submit' and @name='login']").click()
time.sleep(3)

WebDriverWait(driver, 10).until(EC.url_contains("admin_menu.php"))

admin_url = driver.current_url
print("Logged in redirect URL:", admin_url)

match = re.search(r'id=(\d+)', admin_url)
admin_id = match.group(1) if match else "1"  
print("Detected Admin ID:", admin_id)

reported_ad_url = f"http://127.0.0.1/project/view/tishat_features/report_ads/reported_ads.php?id={admin_id}"
driver.get(reported_ad_url)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "reported_ad_info_container"))
)
driver.save_screenshot("C:/Users/ASUS/Pictures/SS/before_delete_reported_ad.png")
print('Screenshot saved: "before_delete_reported_ad.png"')

delete_button = driver.find_element(By.XPATH, "(//div[@class='delete_btn']/button)[1]")
time.sleep(3)
delete_button.click()

WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "confirmPopup")))
time.sleep(3)
WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.ID, "confirmYes"))).click()

popup_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "popupMessage")))
print("Popup Message:", popup_message.text)

time.sleep(1)
driver.save_screenshot("C:/Users/ASUS/Pictures/SS/after_delete_reported_ad.png")
print('Screenshot saved: "after_delete_reported.png"')

WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "confirmOk"))).click()

driver.quit()
