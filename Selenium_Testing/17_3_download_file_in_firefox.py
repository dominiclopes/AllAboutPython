import os
import time


from selenium import webdriver


# Path to the driver
driver_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.sep + "drivers" + os.sep
chrome_driver_path = driver_path + "chromedriver.exe"
firefox_driver_path = driver_path + "geckodriver.exe"
ie_driver_path = driver_path + "IEDriverServer.exe"
# print(chrome_driver_path + "\n" + firefox_driver_path + "\n" + ie_driver_path)

fp = webdriver.FirefoxProfile()
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain,application/pdf")  #MIME type
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", os.path.dirname(os.path.abspath(__file__)))
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("pdfjs.disabled", True)


driver = webdriver.Firefox(executable_path=firefox_driver_path, firefox_profile=fp)
# ---------------------------------------------------------- #
url = "http://demo.automationtesting.in/FileDownload.html"
driver.get(url)
driver.maximize_window()


driver.find_element_by_id("textbox").send_keys("This is for trial purpose")
driver.find_element_by_id("createTxt").click()  # Click on the generate button
driver.find_element_by_id("link-to-download").click()  # Click on the download link
time.sleep(10)

driver.quit()
