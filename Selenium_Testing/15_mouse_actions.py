import os
import time


from selenium import webdriver
from selenium.webdriver import ActionChains


# Path to the driver
driver_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.sep + "drivers" + os.sep
chrome_driver_path = driver_path + "chromedriver.exe"
firefox_driver_path = driver_path + "geckodriver.exe"
ie_driver_path = driver_path + "IEDriverServer.exe"
# print(chrome_driver_path + "\n" + firefox_driver_path + "\n" + ie_driver_path)


driver = webdriver.Chrome(executable_path=chrome_driver_path)
# ---------------------------------------------------------- #


# Create object of the actions class
actions_obj = ActionChains(driver)

# Hover
"""
We need to get all the elements that we need to traverse to.
Once we reach the desired element we click the element and use the perform function
"""
url = "https://www.canva.com/"
driver.get(url)
driver.maximize_window()
learn = driver.find_elements_by_xpath('//*[@id="root"]/div/div[3]/div/div[2]/header/div[2]/nav/ul/li[4]/div/a')
tutorials = driver.find_elements_by_xpath('//*[@id="__next"]/div[1]/div/header/div[2]/nav/ul/li[4]/div/div/div/div/div/div/div/div[6]/ul/li[1]/div/ul/li[4]/a/div/span')
actions_obj.move_to_element(learn).move_to_element(tutorials).click().perform()
time.sleep(2)
driver.quit()

# Double click
url = "https://testautomationpractice.blogspot.com/"
driver.get(url)
driver.maximize_window()
element = driver.find_element_by_xpath("//*[@id='HTML10'']/div[1]/button")
actions_obj.double_click(element).perform()


# Right cLick
element = driver.find_element()
actions_obj.context_click(element).perform()


# Drag and drop
source_element = driver.find_element()
target_element = driver.find_element()
actions_obj.drag_and_drop(source=source_element, target=target_element).perform()


driver.close()
