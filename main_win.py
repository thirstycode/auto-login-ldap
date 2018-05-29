import os

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.firefox.options import Options
import time

username = ""
password = ""

# <----to run headless---->
options = Options()
options.set_headless(headless=True)
# <------------------------>

browser = webdriver.Firefox(firefox_options=options,executable_path="drivers/windows/geckodriver.exe")

try:
	browser.get("http://internet.iitb.ac.in")
except WebDriverException:
	print("Check Ethernet Connection Properly, DNS not found.")
	quit()

input_username = browser.find_elements_by_xpath("//input[@name='uname']")
if len(input_username) > 0:
	ActionChains(browser).move_to_element(input_username[0]).click().send_keys(username).perform()
	time.sleep(1)
else:
	print("Already Logged In")

try : 	
	input_password = browser.find_elements_by_xpath("//input[@name='passwd']")
	ActionChains(browser).move_to_element(input_password[0]).click().send_keys(password).perform()
	time.sleep(1)
except:
	pass

try:
	login_button = browser.find_element_by_xpath("//input[@value='Login']")
	ActionChains(browser).move_to_element(login_button).click().perform()
except:
	pass

time.sleep(3)

browser.get("http://internet.iitb.ac.in")
login_status = browser.find_elements_by_xpath("//input[@value='Logout']")

if len(login_status) > 0:
    print("Login Successfull")
else:
	print("Bad Username or Password")