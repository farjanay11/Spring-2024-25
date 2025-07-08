from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get('http://127.0.0.1/project/') 
    time.sleep(7)  

    driver.save_screenshot("C:/Users/ASUS/Pictures/SS/before_impression_increase.png")
    print(f'Screenshot saved: "before_impression_increase.png"')

    impression_stat_div = driver.find_element(By.CLASS_NAME, 'ad_impression_class')
    impression_count_elem = impression_stat_div.find_element(By.TAG_NAME, 'p')
    count_before = int(impression_count_elem.text.strip())

    impression_button = driver.find_element(By.CLASS_NAME, 'impression')
    impression_button.click()

    time.sleep(3)

    driver.save_screenshot("C:/Users/ASUS/Pictures/SS/after_impression_increase.png")
    print(f'Screenshot saved: "after_impression_increase.png"')

    updated_stat_div = driver.find_element(By.CLASS_NAME, 'ad_impression_class')
    updated_count_elem = updated_stat_div.find_element(By.TAG_NAME, 'p')
    count_after = int(updated_count_elem.text.strip())

    print("Impression count before click:", count_before)
    print("Impression count after click: ", count_after)

    if count_after > count_before:
        print("Success: Impression count increased.")
    else:
        print("Failed: Impression count did not increase.")

finally:
    driver.quit()
