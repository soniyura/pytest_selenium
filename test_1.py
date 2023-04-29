import datetime
import time

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

user_name = driver.find_element(By.XPATH, "//input[@id='user-name']")
user_name.send_keys(login_standard_user)
print("ввели логін")
password = driver.find_element(By.XPATH, "//input[@id='password']")
password.send_keys(password_all)
print("ввели пароль")
button_login = driver.find_element(By.XPATH, "//input[@id='login-button']")
button_login.click()
print("клікнули на кнопку авторизації")

#text_products = driver.find_element(By.XPATH, "//span[@class='title']") #вибрати поле
#value_text_products = text_products.text #зчитати значення в полі та зберезти в змінну
#print(value_text_products)
#перевірка по елементу на сторінкі чи дійсно в мене відкрилася потрібна сторінка
#умовний оператор перевіряє чи значення змінної відповідає очікуваному результату та виводить повідомлення
#assert value_text_products == 'Products'
#print("good")

#перевірка по url  чи дійсно я знаходжуся на потрібній сторінкі
url =  "https://www.saucedemo.com/inventory.html"
get_url = driver.current_url
print(get_url)

assert url == get_url
print("good url")
time.sleep(3)
#додаєємо час коли був зроблений скрін
now_data = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
#вставляємо дату та час в неймінг скріна
name_screenshot = 'screenshot' + now_data + '.png'
#робить скрін
driver.save_screenshot('/Users/macbook/AquaProjects/pytest_selenium/screen/' + name_screenshot)





















