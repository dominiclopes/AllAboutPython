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

# Difference between full screen and maximize window
# Taking a ss
url = "https://www.youtube.com/"
driver.get(url)
driver.maximize_window()
driver.save_screenshot("ss1.png")
time.sleep(3)

driver.fullscreen_window()
driver.save_screenshot("ss2.png")
time.sleep(3)
driver.quit()

