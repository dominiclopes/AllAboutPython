import os
import time

from selenium import webdriver


chrome_driver_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + \
                     os.sep + "drivers" + os.sep + "chromedriver.exe"
web_driver = webdriver.Chrome(chrome_driver_path)


url = "https://www.browserstack.com/users/sign_in"
web_driver.get(url)
web_driver.maximize_window()

# Sign in
web_driver.find_element_by_id("user_email_login").send_keys("dominicjlopes@yahoo.com")
web_driver.find_element_by_id("user_password").send_keys("BrowserstackTest")

submit_button = web_driver.find_element_by_id("user_submit")
web_driver.execute_script("arguments[0].scrollIntoView();", submit_button)
submit_button.click()

# Click the bell icon
web_driver.implicitly_wait(10)
web_driver.find_element_by_id("beamer-notification-toggle").click()

# Get the notification
for i in range(20):
    notification = web_driver.find_element_by_xpath("/html/body/div/div[2]/div/div[{}]".format(i))
    print(notification.text)

time.sleep(5)
web_driver.close()
