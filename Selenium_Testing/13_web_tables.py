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
rows = driver.find_elements_by_xpath("xpath_of_the_tr")
columns = driver.find_elements_by_xpath("xpath_of_the_1st_row_data_tag")

# Using for loop and dynamically getting all the elements we get all the columns in the table
# use element.text to get the value