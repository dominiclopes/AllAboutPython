import time
import os


from selenium import webdriver


# Path to the driver
driver_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.sep + "drivers" + os.sep
chrome_driver_path = driver_path + "chromedriver.exe"
firefox_driver_path = driver_path + "geckodriver.exe"
ie_driver_path = driver_path + "IEDriverServer.exe"
# print(chrome_driver_path + "\n" + firefox_driver_path + "\n" + ie_driver_path)

driver = webdriver.Chrome(executable_path=chrome_driver_path)
# ---------------------------------------------------------- #


url = "https://www.keynotesupport.com/internet/web-contact-form-example-radio-buttons.shtml"
driver.get(url)
driver.implicitly_wait(10)

# Check if the name input element is displayed and enabled
element = driver.find_element_by_id("name1")
print(element.__dir__())
print("Element text: {}, is enabled?: {}, is displayed?: {}".format(
    element.text, element.is_enabled(), element.is_displayed()))

element = driver.find_element_by_css_selector("input[value=Excel]")
print("Element text: {}, is enabled?: {}, is displayed?: {}, is selected?: {}".format(
    element.text, element.is_enabled(), element.is_displayed(), element.is_selected()))

# element.click()
# print("Element text: {}, is enabled?: {}, is displayed?: {}, is selected?: {}".format(
#     element.text, element.is_enabled(), element.is_displayed(), element.is_selected()))
