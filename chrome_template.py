# selenium_template/sel_template.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = '/users/chromedriver'

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(url)


driver.close()