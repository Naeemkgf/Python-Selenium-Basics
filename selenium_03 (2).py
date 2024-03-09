#find sliderand tags  

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

service = Service(executable_path="C:\\Users\\STARCITY\\Desktop\\streamlit apps\\python_selenium\\chromedriver.exe")

driver = webdriver.Chrome(service=service)

url = "http://www.automationpractice.pl/index.php"

driver.get(url=url)
driver.maximize_window()
sleep(2)

slider = driver.find_elements(By.CLASS_NAME,"homeslider-container")
print("Number of sliders: ", len(slider))

tags = driver.find_elements(By.TAG_NAME,"a")

print("The length of the tags:",len(tags))

sleep(5)

driver.quit()
