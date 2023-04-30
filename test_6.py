

from selenium import webdriver
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


"""АВТОРИЗАЦІЯ"""
user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("ввели логін")
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("ввели пароль")
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print("клікнули на кнопку авторизації")


"""INFO Product #1"""
"""NAME"""
product_1 = driver.find_element(By.XPATH, "//a[@id='item_4_title_link']")
value_product_1 = product_1.text
print(value_product_1)
"""PRICE"""
price_product_1 = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[2]/div")
value_price_product_1 = price_product_1.text
print(value_price_product_1)

select_producr_1 = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")
select_producr_1.click()
print("клік на кнопку ")

cart = driver.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
cart.click()




























