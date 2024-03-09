from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

path = "C:\\Users\\STARCITY\\Desktop\\streamlit apps\\python_selenium\\chromedriver.exe"
service =Service(executable_path=path)

driver = webdriver.Chrome(service=service)

url = "http://www.automationpractice.pl/index.php"

driver.get(url=url)
driver.maximize_window()
sleep(1)

#Xpath
driver.find_element(By.XPATH,"/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]").send_keys('T-shirts')
driver.find_element(By.XPATH,'/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/button').click()
sleep(3)

driver.quit()
