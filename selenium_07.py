#import the libraries
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#set up the driver
path = "C:\\Users\\STARCITY\\Desktop\\streamlit apps\\python_selenium\\chromedriver.exe"
service =Service(executable_path=path)

driver = webdriver.Chrome(service=service)

url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

driver.get(url=url)

driver.maximize_window()

# driver.find_element(By.NAME,"username").send_keys("Admin")
# # Wait for username input field to be visible
username_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "username")))
username_input.send_keys("Admin")
sleep(4)
driver.find_element(By.NAME,"password").send_keys("admin123")
sleep(4)

xpath= "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"
driver.find_element(By.XPATH,xpath).click()
sleep(4)

xpath1 = "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/img"
driver.find_element(By.XPATH,xpath1).click()
sleep(4)

xpath_logout = "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a"
driver.find_element(By.XPATH, xpath_logout).click()
print('Logged out')
sleep(10)
driver.quit()
