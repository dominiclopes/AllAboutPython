# implicit wait is applicable for all the elements once it is set

import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# Path to the driver
driver_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.sep + "drivers" + os.sep
chrome_driver_path = driver_path + "chromedriver.exe"
firefox_driver_path = driver_path + "geckodriver.exe"
ie_driver_path = driver_path + "IEDriverServer.exe"
# print(chrome_driver_path + "\n" + firefox_driver_path + "\n" + ie_driver_path)


driver = webdriver.Chrome(executable_path=chrome_driver_path)
# ---------------------------------------------------------- #
url = "https://www.expedia.com"
driver.get(url)
driver.implicitly_wait(10)

driver.find_element(By.XPATH, '//*[@id="uitk-tabs-button-container"]/li[2]/a').click()

time.sleep(5)
driver.quit()
