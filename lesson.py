
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService




options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), chrome_options=options)


driver.get('https://www.saucedemo.com/')
driver.maximize_window()
#user_name = driver.find_element(By.ID, "user-name") #ID
#user_name = driver.find_element(By.NAME, "user-name") #NAME
#user_name = driver.find_element(By.XPATH, '//*[@id="user-name"]') # full XPATH
#user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]') #id XPATH
user_name = driver.find_element(By.XPATH, "//input[@data-test='username']") #data-test XPATH
user_name.send_keys("standard_user")


