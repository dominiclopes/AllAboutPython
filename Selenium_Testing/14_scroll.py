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
url = "https://www.countries-ofthe-world.com/flags-of-the-world.html"
driver.implicitly_wait(10)

# Scroll down by pixel
driver.get(url)
driver.maximize_window()
driver.execute_script("window.scrollBy(0, 5000)")
driver.quit()

# Scroll down until an element is found
driver.get(url)
driver.maximize_window()
element = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr[86]/td[2]')
driver.execute_script("arguments[0].scrollIntoView();", element)
driver.quit()

# Scroll to the end of the page
driver.get(url)
driver.maximize_window()
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
driver.quit()
