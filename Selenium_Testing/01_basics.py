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


# # Example 1
# driver.get("http://ww7.demoaut.com/")
# print(driver.__dir__())
# print(driver.title)
# print(driver.current_url)
# driver.close()  # Close only the current browser

# Example 2
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)
print(driver.current_url)
driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()
time.sleep(2)
driver.quit()  # Closes all opened browsers
