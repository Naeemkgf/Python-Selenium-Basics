#import the libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from time import sleep

#set up the driver
path = "C:\\Users\\STARCITY\\Desktop\\streamlit apps\\python_selenium\\chromedriver.exe"
service =Service(executable_path=path)

driver = webdriver.Chrome(service=service)
driver.maximize_window()

url = "https://www.globalsqa.com/demo-site/select-dropdown-menu/"
driver.get(url=url)

xpath = "/html/body/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/p/select"

drop_country = Select(driver.find_element(By.XPATH,xpath))
drop_country.select_by_visible_text("Pakistan")  # select country by visible text
print("Selected Country: ", drop_country.first_selected_option.text)

drop_country.select_by_value("PAK")   # select country by value
print("Selected Country: ", drop_country.first_selected_option.text)
sleep(3)

# select country by index
drop_country.select_by_index("4")
sleep(3)

#capture all the option from the dropdown and print it by their index
opt = drop_country.options
print("Totlal Options:",len(opt))
for i in range(len(opt)):
    print(f"Option {i}: {opt[i].text}")
sleep(5)

driver.quit()
