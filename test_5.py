import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), chrome_options=options)

"""ЗМІННІ"""
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

"""БОКОВЕ МЕНЮ"""
menu = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
menu.click()
time.sleep(2)
print("клікнули на кнопку меню")
link_about = driver.find_element(By.XPATH, "//a[@id='about_sidebar_link']")
link_about.click()

























