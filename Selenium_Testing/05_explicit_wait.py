# explicit is more like condition based and is specific to the elements

import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


# Path to the driver
driver_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.sep + "drivers" + os.sep
chrome_driver_path = driver_path + "chromedriver.exe"
firefox_driver_path = driver_path + "geckodriver.exe"
ie_driver_path = driver_path + "IEDriverServer.exe"
# print(chrome_driver_path + "\n" + firefox_driver_path + "\n" + ie_driver_path)


driver = webdriver.Chrome(executable_path=chrome_driver_path)
# ---------------------------------------------------------- #
driver.maximize_window()

url = "https://www.expedia.com"
driver.get(url)
driver.implicitly_wait(5)

driver.find_element(By.XPATH, '//*[@id="uitk-tabs-button-container"]/li[2]/a').click()
time.sleep(2)

from_field = driver.find_element(
    By.XPATH, '//*[@id="wizard-flight-tab-roundtrip"]/div/div[1]/div/div[1]/div/div/div/button')
from_field.send_keys("SFO")
time.sleep(2)

to_field = driver.find_element(
    By.XPATH, '//*[@id="wizard-flight-tab-roundtrip"]/div/div[1]/div/div[2]/div/div/div/button')
to_field.send_keys("NYC")
time.sleep(2)

departing = driver.find_element(By.ID, "d1-btnker")
departing.clear()
departing.send_keys("10/01/2021")

returning = driver.find_element(By.ID, "d2-btnker")
returning.clear()
returning.send_keys("12/01/2021")

driver.find_element(By.XPATH, '//*[@id="wizard-flight-pwa-1"]/div[4]/div[2]/button').click()

wait = WebDriverWait(driver, 10)
element = wait.until(ec.element_to_be_clickable((By.XPATH, "path_to_the_element")))
element.click()

time.sleep(5)
driver.quit()
