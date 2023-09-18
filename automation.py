from selenium import webdriver

# chrome_browser = webdriver.Chrome('chromedriver')
# # if file is in the drivers folder ie mac (/usr/local/bin) win (c: drivers)
# print(chrome_browser)

### Alternative way, we will use this based on selenium documentation
# chrome_browser = webdriver.Chrome()
# chrome_browser.maximize_window()
# chrome_browser.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
# print("Selenium Easy Demo" in chrome_browser.title)
# assert "Selenium" in chrome_browser.body
#print(chrome_browser)

from selenium.webdriver.common.by import By
import time

chrome_browser = webdriver.Chrome()
chrome_browser.maximize_window()
chrome_browser.get('http://demo.seleniumeasy.com/basic-first-form-demo.html')

# This solves the issue with the Popup for those that encounter it:
# chrome_browser.implicitly_wait(2)
# popup = chrome_browser.find_element(By.ID, 'at-cv-lightbox-close')
# popup.click()

user_message = chrome_browser.find_element(By.ID, 'user-message')
user_message.clear()
user_message.send_keys('I AM EXTRA COOOOL')

time.sleep(2)
show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-primary')
show_message_button.click()

output_message = chrome_browser.find_element(By.ID, 'display')
time.sleep(3) # added by ME
assert 'I AM EXTRA COOOOL' in output_message.text