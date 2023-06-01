from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# FinFire credentials

Benutzername = "80034"
passwort = "Erfolgbergers0401#"

# initialize the Chrome driver
# put your chromdrive version in the directory of the file

driver = webdriver.Chrome("chromedriver")

# head to Finfire login page

import time
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://finfire.de/login/#/login::/app/")

time.sleep(5)
'''
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
'''
# find username/email field and send the username itself to the input field

driver.find_element("id", "input-11").send_keys(Benutzername)

time.sleep(5)

# find password input field and insert password as well

driver.find_element("id", "input-12").send_keys(passwort)

time.sleep(10)

# click login buttoncontent

driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()