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


url = "https://www.google.com/search?q=chained+to+the+rhythm+lyrics&" \
      "rlz=1C1GCEU_en-GBIN887IN887&oq=chai&aqs=chrome.0.69i59j46j0j46j0j69i61j69i60l2.1146j1j7&sourceid=chrome&ie=UTF-8"
driver.get(url)
print(driver.title)
time.sleep(2)

url = "https://www.google.com/search?q=rise+katy+perry+lyrics&" \
      "rlz=1C1GCEU_en-GBIN887IN887&oq=rise&aqs=chrome.2.69i57j46j69i59j0l2j46l2j0.1726j1j7&sourceid=chrome&ie=UTF-8"
driver.get(url)
print(driver.title)
time.sleep(2)

driver.back()  # navigational command
print(driver.title)
time.sleep(2)

driver.forward()  # navigational command
print(driver.title)
time.sleep(2)

driver.refresh()  # command to refresh the browser

driver.quit()
