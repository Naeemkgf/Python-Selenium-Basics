#import libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep

service = Service(executable_path="C:\\Users\\STARCITY\\Desktop\\streamlit apps\\python_selenium\\chromedriver.exe")

driver = webdriver.Chrome(service=service)


url = "https://www.facebook.com"

driver.get(url=url)
driver.maximize_window()
sleep(1)



#tags and id's for elements on the page using CSS-SELECTOR
driver.find_element(By.CSS_SELECTOR,'input#email').send_keys('naeembozdar')#tag is not necessary


#tags and class for elements on the page using CSS-SELECTOR
driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("naeembozdar") #class=(_55r1 _6luy) we skip this because there is an space in class
sleep(3)


#tags and attribute  for elements on the page using CSS-SELECTOR
driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("Abc@gmail.com")
sleep(3)


#tags,class and attribute  for elements on the page using CSS-SELECTOR
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_pass]").send_keys("naeembozdar") #class=(_55r1 _6luy) we skip this because there is an space in class
sleep(3)

driver.quit()

