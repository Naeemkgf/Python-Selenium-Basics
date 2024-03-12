#import the libraries
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#set up the driver
path = "C:\\Users\\STARCITY\\Desktop\\streamlit apps\\python_selenium\\chromedriver.exe"
service =Service(executable_path=path)

driver = webdriver.Chrome(service=service)

url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

driver.get(url=url)

driver.maximize_window()

#Application Commands
title = driver.title #title of the page
url = driver.current_url #current url of the page
page_source = driver.page_source #source code of the page
print("Page Title is: ", title)
print(f" Current URL is : {url}")
print("Source Code is:\n", page_source)

#Output
#Page Title is:  OrangeHRM
#Current URL is : https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

sleep(0.4)   #give some time for browser to load
driver.quit()
