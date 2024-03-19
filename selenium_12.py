#import the libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from time import sleep

#set up the driver
path = "C:\\Users\\STARCITY\\Desktop\\streamlit apps\\python_selenium\\chromedriver.exe"
service =Service(executable_path=path)

driver = webdriver.Chrome(service=service)

driver.maximize_window()

#To bypass the username and password

#https://the-internet.herokuapp.com/basic_auth  actual url 

url = "https://admin:admin@the-internet.herokuapp.com/basic_auth" #adding the username and pass in url to bypass the popup/aleart login page

driver.get(url=url)

driver.find_element(By.LINK_TEXT,"Elemental Selenium").click()
sleep(10)
driver.close()
