import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains



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

"""СКРОЛИТЬ"""
# time.sleep(2)
# #скролить сторінку scrollTo(Х, У) Х-по ширині У-по висоті
# driver.execute_script("window.scrollTo(0, 200 )")
# time.sleep(2)

"""НАВЕДЕННЯ НА ЕЛЕМЕНТ"""
action = ActionChains(driver)
t_shirt = driver.find_element(By.XPATH, "//button[@id='add-to-cart-sauce-labs-onesie']")
action.move_to_element(t_shirt).perform()
print('навівся')
time.sleep(2)

"""СКРІНИТЬ"""
#додаєємо час коли був зроблений скрін
now_data = datetime.datetime.utcnow().strftime("%Y.%m.%d. %H.%M.%S")
#вставляємо дату та час в неймінг скріна
name_screenshot = 'screen ' + now_data + '.png'
#робить скрін
driver.save_screenshot('/Users/macbook/AquaProjects/pytest_selenium/screen/' + name_screenshot)





















