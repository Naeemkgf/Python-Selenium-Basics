#import the libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

#set up the driver
path = "C:\\Users\\STARCITY\\Desktop\\streamlit apps\\python_selenium\\chromedriver.exe"
service =Service(executable_path=path)

driver = webdriver.Chrome(service=service)
driver.maximize_window()

fb_url = "https://www.facebook.com"
ig_url = "https://www.instagram.com"

driver.get(url=fb_url)
driver.get(url=ig_url)

#Navigation Commands
#1-back command
driver.back()
print("----Page is back----")
sleep(1)

#2- forward command
driver.forward()
print("-----Page is forward------")
sleep(1)
#3- Refresh command

driver.refresh()
print("--- Page is Refresh---")
sleep(1)

driver.quit()
