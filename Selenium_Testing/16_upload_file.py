import os
import time


from selenium import webdriver


# Path to the driver
driver_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.sep + "drivers" + os.sep
chrome_driver_path = driver_path + "chromedriver.exe"
firefox_driver_path = driver_path + "geckodriver.exe"
ie_driver_path = driver_path + "IEDriverServer.exe"
# print(chrome_driver_path + "\n" + firefox_driver_path + "\n" + ie_driver_path)


driver = webdriver.Chrome(executable_path=chrome_driver_path)
# ---------------------------------------------------------- #
url = "https://testautomationpractice.blogspot.com/"
driver.get(url)
driver.maximize_window()

# Switch to the frame (form element)
driver.switch_to.frame(0)

# Find the upload file element # Upload using the send keys option
driver.find_element_by_id("RESULT_FileUpload-10").send_keys(
    os.path.abspath("zoom-video-background-meeting-template-design-db291171eefc26d5bf4dde3b220c2b4a_screen.mp4"))

time.sleep(10)
driver.quit()
