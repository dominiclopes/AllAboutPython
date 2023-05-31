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


driver = webdriver.Firefox(executable_path=firefox_driver_path)
# ---------------------------------------------------------- #
elements = driver.find_elements(By.TAG_NAME, "a")
print(len(elements))

for link in elements:
    print(link.text)


driver.find_element_by_link_text()
driver.find_element_by_partial_link_text()
