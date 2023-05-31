import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

chrome_driver_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + \
                     os.sep + "drivers" + os.sep + "chromedriver.exe"
web_driver = webdriver.Chrome(chrome_driver_path)


url = "https://www.browserstack.com/automate/capabilities"
web_driver.get(url)
web_driver.maximize_window()
# web_driver.implicitly_wait(10)

# Find the capabilities generator header
capabilities_generator_header = web_driver.find_element_by_id("capabilities-generator")
# Scroll until the element is found
web_driver.execute_script("arguments[0].scrollIntoView();", capabilities_generator_header)

# Click the menu option
web_driver.find_element_by_id("doc-os-trigger").click()
# Select the operating system as android
web_driver.find_element_by_class_name("icon-browser-sprite.icon-android.select-android").click()

# Clicking the device option
web_driver.find_element_by_id("doc-device-trigger").click()
# Select the device
web_driver.find_element_by_xpath("//*[@id='doc-device-options']/div[1]/div[2]/ul[1]/li[2]/a").click()

# Get the results
result_key = web_driver.find_elements_by_class_name("key")
result_value = web_driver.find_elements_by_class_name("value")
result_dict = {k.text.strip('"'): v.text.strip('"') for k, v in zip(result_key, result_value)}
print(result_dict)

time.sleep(3)
web_driver.close()



