from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver
from pyvirtualdisplay import Display
import pyvirtualdisplay
import json

display = Display(visible=0, size=(800, 600))
display.start()

fp = webdriver.FirefoxProfile()
success = True
wd = WebDriver(fp)
wd.implicitly_wait(600)
wd.get("http://www.google.com")

display.stop()
