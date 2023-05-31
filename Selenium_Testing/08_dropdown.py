import os
import time


from selenium import webdriver
from selenium.webdriver.support.ui import Select

# Path to the driver
driver_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.sep + "drivers" + os.sep
chrome_driver_path = driver_path + "chromedriver.exe"
firefox_driver_path = driver_path + "geckodriver.exe"
ie_driver_path = driver_path + "IEDriverServer.exe"
# print(chrome_driver_path + "\n" + firefox_driver_path + "\n" + ie_driver_path)


driver = webdriver.Firefox(executable_path=firefox_driver_path)
# ---------------------------------------------------------- #

element = driver.find_element_by_id("drop_down_element")
drp = Select(element)

# select by visible text
drp.select_by_visible_text("select me")

# select by index
drp.select_by_index(2)

# select by value
drp.select_by_value("radio-2")

# Capture all options and print them as output
print(drp.options, len(drp.options))
