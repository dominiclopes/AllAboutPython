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
driver.switch_to.frame()  # provide name, id or index
# we do not have to locate the element in this case, just pass hte name, id or index

# Switch to the page
driver.switch_to.default_content()

# Now switch to another frame
