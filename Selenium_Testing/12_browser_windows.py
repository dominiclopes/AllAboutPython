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
print(driver.current_window_handle)
# perform a click option that opens a new page
print(driver.window_handles)
# Now we have all the window handles

for handle in driver.window_handles:
    driver.switch_to.window(handle)
    print(driver.title)
