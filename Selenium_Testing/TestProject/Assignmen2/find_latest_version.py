import requests
import json


output = requests.get("https://www.browserstack.com/list-of-browsers-and-platforms.json?product=automate")
output = json.loads(output.text)


# Print latest version of Chrome & Firefox on windows
chrome_version, firefox_version = 0, 0
for desktop in output["desktop"]:
    if desktop["os"] == "Windows":
        for browser in desktop["browsers"]:
            browser_type = browser["browser"]
            # Check if the browser version is not beta and convert it to float
            browser_version = browser["browser_version"]

            try:
                browser_version = float(browser_version)
                if browser_type == "chrome" and browser_version > chrome_version:
                    chrome_version = browser_version
                if browser_type == "firefox" and browser_version > firefox_version:
                    firefox_version = browser_version
            except ValueError:
                pass
print("Latest Chrome Version: {}, Latest Firefox Version {}".format(chrome_version, firefox_version))


# Print latest version of Chrome & Firefox on windows
device_os_version = 0
for mobile in output["mobile"]:
    if mobile["os_display_name"] == "ios":
        for device in mobile["devices"]:
            if device["device"] == "iPhone 8" and float(device["os_version"]) > device_os_version:
                device_os_version = float(device["os_version"])
print("Latest iPhone 8 device version {}".format(device_os_version))
