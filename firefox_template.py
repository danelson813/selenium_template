from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

firefox_driver_path = '/Users/geckodriver'

service = Service(firefox_driver_path)
driver = webdriver.Firefox(service=service)

url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(url)

driver.close()
