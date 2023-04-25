
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), chrome_options=options)

base_url = 'https://www.saucedemo.com/'
login_standard_user = "standard_user"
password_all = "secret_sauc"

driver.get(base_url)
driver.maximize_window()

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("ввели логін")
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("ввели пароль")
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print("клікнули на кнопку авторизації")

#warring_test = driver.find_element(By.XPATH, "//h3[@data-test='error']") #знаходимо повідомлення про помилку
#value_warring_test = warring_test.text      #читаємо повідомлення і зберігаємо в змінну
#якщо значенн змінної відповідає тому що написано
#assert value_warring_test == "Epic sadface: Username and password do not match any user in this service"
#то виводимо прінт
#print("good test")


warring_test2 = driver.find_element(By.XPATH, "//h3[@data-test='error']")
value_warring_test2 = warring_test2.text
assert value_warring_test2 == "Epic sadface: Username and password do not match any user in this service"
print("неправельний пароль")




















