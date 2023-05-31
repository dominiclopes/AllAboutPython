import os
import time


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Path to the driver
driver_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.sep + "drivers" + os.sep
chrome_driver_path = driver_path + "chromedriver.exe"
firefox_driver_path = driver_path + "geckodriver.exe"
ie_driver_path = driver_path + "IEDriverServer.exe"
# print(chrome_driver_path + "\n" + firefox_driver_path + "\n" + ie_driver_path)
# ---------------------------------------------------------- #
chrome_options = Options()
chrome_options.add_experimental_option(
    "prefs", {"download.default_directory": os.path.dirname(os.path.abspath(__file__))})


driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
# ---------------------------------------------------------- #
url = "http://demo.automationtesting.in/FileDownload.html"
driver.get(url)
driver.maximize_window()


driver.find_element_by_id("textbox").send_keys("This is for trial purpose")
driver.find_element_by_id("createTxt").click()  # Click on the generate button
driver.find_element_by_id("link-to-download").click()  # Click on the download link

time.sleep(10)
driver.quit()
