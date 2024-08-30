import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_argument('--headless')
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
user_name.send_keys(login_standart_user)
print('Input username')

# time.sleep(1)
# user_name.send_keys(Keys.BACKSPACE)
# time.sleep(1)
# user_name.send_keys(Keys.BACKSPACE)
# time.sleep(1)
# user_name.send_keys('e')
# time.sleep(1)
# user_name.send_keys('r')

user_password = driver.find_element(By.XPATH, '//*[@id="password"]')
user_password.send_keys(password_all)
print('Input password')

user_name.send_keys(Keys.RETURN)

var_filter = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select')
var_filter.click()
time.sleep(2)

var_filter_item = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[2]')
var_filter_item.click()

# time.sleep(2)
# var_filter.send_keys(Keys.RETURN) # не сработало
print('var_filter compete')


# driver.send_keys(Keys.COMMAND, 'X')

# driver.send_keys(Keys.CTRL + 'x').

# driver.send_keys(Keys.CONTROL + 'X')

# driver.send_keys(Keys.SHIFT, 'x').
