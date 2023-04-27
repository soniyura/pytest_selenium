import time
from selenium import webdriver
from selenium.webdriver import Keys  #підключити Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), chrome_options=options)

base_url = 'https://www.saucedemo.com/'
login_standard_user = "standard_user"
password_all = "secret_sauce"

driver.get(base_url)
driver.maximize_window()

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("ввели логін")

password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("ввели пароль")
password.send_keys(Keys.RETURN)

filter = driver.find_element(By.XPATH , "//select[@data-test='product_sort_container']")
filter.click()
print("клік фільтер")
time.sleep(2)
filter.send_keys(Keys.DOWN)
#filter = driver.find_element(By.XPATH, "//option[@value='za']")
time.sleep(2)
filter.send_keys(Keys.RETURN)










































