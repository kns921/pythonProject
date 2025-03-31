from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument('--headless')
# запуск тестов без открытия браузера

g = Service()
driver = webdriver.Chrome(options=options, service=g)
bace_url = 'https://www.saucedemo.com/'
driver.get(bace_url)
driver.maximize_window()

login_standart_user = 'standard_user'
login_error_user = 'standard_user1'
password_all = 'secret_sauce'

login_window = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]')
value_login_window = login_window.text
print('Negative test start')
print(value_login_window)
assert value_login_window == 'Swag Labs'
print('OK')

user_name = driver.find_element(By.XPATH, '//*[@id="user-name"]')
user_name.send_keys(login_error_user)
print('Input error username')

user_password = driver.find_element(By.XPATH, '//*[@id="password"]')
user_password.send_keys(password_all)
print('Input password')

button_login = driver.find_element(By.XPATH, '//*[@id="login-button"]')
button_login.click()
print('Click login button')

warrning_text = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')
value_warrning_text = warrning_text.text
assert value_warrning_text == 'Epic sadface: Username and password do not match any user in this service'
print('Negative test - OK')
