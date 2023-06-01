from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)


import time

driver.get('https://bergers.odoo.com/web/login')
time.sleep(5)
driver.maximize_window()

wait = WebDriverWait(driver, 5)
username_field = wait.until(EC.presence_of_element_located((By.NAME, 'login')))
password_field = wait.until(EC.presence_of_element_located((By.NAME, 'password')))

username_field.send_keys('xetic1@gmail.com')
password_field.send_keys('$BMW320.i$')

password_field.send_keys(Keys.RETURN)

driver.implicitly_wait(5)

links = driver.find_elements("xpath", "//a[@href]")
for link in links:
if "Kontakte" in link.get_attribute("innerHTML"):
time.sleep(5)
link.click()
break