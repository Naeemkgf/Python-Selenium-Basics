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

url = "https://demo.nopcommerce.com/register?returnUrl=%2F"

driver.get(url=url)

driver.maximize_window()

#Conditional Commands 


#1- is_displayed()
search_box = driver.find_element(By.NAME,"q")
print("Search box is displayed: ", search_box.is_displayed())

#2- is_enabled()
print("Search box is enabled: ",search_box.is_enabled())
sleep(2)


#3- is_selected()
male_radio_button = driver.find_element(By.ID,"gender-male")
female_radio_button = driver.find_element(By.ID,"gender-female")

male_radio_button.click()
print("After selecting Male radio button")
print(male_radio_button.is_selected())
print(female_radio_button.is_selected())

female_radio_button.click()
print("After selecting Female radio button")
print(male_radio_button.is_selected())
print(female_radio_button.is_selected())

driver.quit()
