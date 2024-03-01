import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(executable_path="C:\\Users\\STARCITY\\Desktop\\streamlit apps\\python_selenium\\chromedriver.exe")

driver = webdriver.Chrome(service=service)

link = 'https://pi.ai/es/talk'

driver.get(url=link)

time.sleep(2)

def skip():
    first_skip = "/html/body/div/main/div/div/button"
    second_skip = "/html/body/div/main/div/div/button"
    last_skip = "/html/body/div/main/div/div/div[1]/div[1]/div[2]/button[1]"
    driver.find_element(by=By.XPATH,value=first_skip).click()
    time.sleep(3)
    driver.find_element(by=By.XPATH,value=second_skip).click()
    time.sleep(3)
    driver.find_element(by=By.XPATH,value=last_skip).click()
    time.sleep(3)

skip()

def query_sender(query):
    xpath_input= "/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/div/textarea"
    xpath_sender = "/html/body/div/main/div/div/div[3]/div[1]/div[4]/div/button"
    driver.find_element(by=By.XPATH,value=xpath_input).send_keys(query)
    time.sleep(1)
    driver.find_element(by=By.XPATH,value=xpath_sender).click()
    time.sleep(1)

query_sender("Hello,How are you")
time.sleep(10)
driver.quit()