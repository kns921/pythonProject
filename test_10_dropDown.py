import datetime
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# запуск тестов без открытия браузера
# options.add_argument('--headless')
g = Service()
driver = webdriver.Chrome(options=options, service=g)
bace_url = 'https://www.saucedemo.com/'
driver.get(bace_url)
driver.maximize_window()

"""Autorization"""
login_window = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]')
value_login_window = login_window.text
print(value_login_window)
assert value_login_window == 'Swag Labs'
print('Autorization form OK')

user_name = driver.find_element(By.XPATH, '//*[@id="user-name"]')
user_name.send_keys('standard_user')

user_password = driver.find_element(By.XPATH, '//*[@id="password"]')
user_password.send_keys('secret_sauce')

button_login = driver.find_element(By.XPATH, '//*[@id="login-button"]')
button_login.click()
print('Click login button')

url_home = 'https://www.saucedemo.com/inventory.html'
get_url = driver.current_url
print(get_url)
assert url_home == get_url
print('URL OK')

text_product = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
value_text_product = text_product.text
print(value_text_product)
assert value_text_product == 'Products'
print('Autorization test OK')

"""Drop Down with Select"""
# создание экземпляра класса Select, для возможности обращения к скрытым элементам дроп-дауна
sel = Select(driver.find_element(By.XPATH, '//select[@class="product_sort_container"]'))

time.sleep(3)
sel.select_by_visible_text('Price (low to high)')

# Screen Select
now_date = datetime.datetime.now().strftime("%H.%M.%S-%Y.%m.%d")
name_screenshot = 'Select OK Screenshot ' + now_date + '.png'
driver.save_screenshot(f'screenshots/{name_screenshot}')
print(name_screenshot)
