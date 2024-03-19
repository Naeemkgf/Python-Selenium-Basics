#import the libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from time import sleep

#set up the driver
path = "C:\\Users\\STARCITY\\Desktop\\streamlit apps\\python_selenium\\chromedriver.exe"
service =Service(executable_path=path)

driver = webdriver.Chrome(service=service)

driver.maximize_window()

url = "https://the-internet.herokuapp.com/javascript_alerts"
driver.get(url=url)

#To  handle alearts in page

xpath = "//*[@id='content']/div/ul/li[3]/button"
driver.find_element(By.XPATH,xpath).click()

aleart = driver.switch_to.alert
text = aleart.text

print("The alert says: ", text)
aleart.send_keys("Selenium")

aleart.accept()# Click on Ok

aleart.dismiss()# Click on Cancel
sleep(2) 

driver.quit()
