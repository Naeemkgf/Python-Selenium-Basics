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
sleep(3)  # Let the page load

driver.find_element(By.NAME,"search_query").send_keys("Dresses")
sleep(3)

driver.find_element(By.NAME,"submit_search").click()
sleep(10)

x_path ='/html/body/div/div[2]/div/div[3]/div[2]/ul/li[1]/div/div[1]/div/a[1]/img'

driver.find_element(By.XPATH,x_path).click()
sleep(7)

driver.find_element(By.CLASS_NAME,"home").click()
sleep(5)

t_shirt_xpath = '/html/body/div/div[1]/header/div[3]/div/div/div[6]/ul/li[3]/a'
driver.find_element(By.XPATH,t_shirt_xpath).click()
sleep(5)

driver.quit()


