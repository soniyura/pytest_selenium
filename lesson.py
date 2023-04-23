
from selenium import webdriver
from selenium.webdriver.common.by import By

#driver = webdriver.Firefox(executable_path='/Users/macbook/AquaProjects/pytest_selenium/geckodriver')

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(executable_path='/Users/macbook/AquaProjects/pytest_selenium/chromedriver', chrome_options=options)

driver.get('https://www.saucedemo.com/')
driver.maximize_window()
#user_name = driver.find_element(By.ID, "user-name") #ID
#user_name = driver.find_element(By.NAME, "user-name") #NAME
#user_name = driver.find_element(By.XPATH, '//*[@id="user-name"]') # full XPATH
#user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]') #id XPATH
user_name = driver.find_element(By.XPATH, "//input[@data-test='username']") #data-test XPATH
user_name.send_keys("standard_user")


