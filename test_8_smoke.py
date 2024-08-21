import datetime
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

"""Autorization"""
login_window = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]')
value_login_window = login_window.text
print(value_login_window)
assert value_login_window == 'Swag Labs'
print('OK')

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
print('OK')

text_product = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
value_text_product = text_product.text
print(value_text_product)
assert value_text_product == 'Products'
print('OK')

# Screen Autorization
now_date = datetime.datetime.now().strftime("%H.%M.%S-%Y.%m.%d")
name_screenshot = 'Autorization OK Screenshot ' + now_date + '.png'
driver.save_screenshot(f'screenshots/{name_screenshot}')
print(name_screenshot)

"""Selection of goods"""
name_goods_1 = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
value_name_goods_1 = name_goods_1.text
print('goods 1 name: ' + value_name_goods_1)

price_goods_1 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div')
value_price_goods_1 = price_goods_1.text
print('price 1: ' + value_price_goods_1)

buy_goods_1 = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
buy_goods_1.click()
print('Goods 1 added')

name_goods_2 = driver.find_element(By.XPATH, '//*[@id="item_0_title_link"]/div')
value_name_goods_2 = name_goods_2.text
print('goods 2 name: ' + value_name_goods_2)

price_goods_2 = driver.find_element(By.XPATH, '//*[@id="inventory_container"]/div/div[2]/div[2]/div[2]/div')
value_price_goods_2 = price_goods_2.text
print('price 2: ' + value_price_goods_2)

buy_goods_2 = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
buy_goods_2.click()
print('Goods 2 added')

"""Basket"""
basket = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
basket.click()
print('Click Basket')

basket_page = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
value_basket_page = basket_page.text
print(value_basket_page)

# Screen Basket
now_date = datetime.datetime.now().strftime("%H.%M.%S-%Y.%m.%d")
name_screenshot = 'Basket ' + now_date + '.png'
driver.save_screenshot(f'screenshots/{name_screenshot}')
print(name_screenshot)

"""Checkout"""
checkout = driver.find_element(By.XPATH, '//*[@id="checkout"]')
checkout.click()
print('Click Checkout')

# Checkout page
checkout_page = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
value_checkout_page = checkout_page.text
print(value_checkout_page)

# Screen Checkout page
now_date = datetime.datetime.now().strftime("%H.%M.%S-%Y.%m.%d")
name_screenshot = 'Checkout page ' + now_date + '.png'
driver.save_screenshot(f'screenshots/{name_screenshot}')
print(name_screenshot)

# Input Your Information
first_name = 'Nikolay'
last_name = 'Kuznetsov'
post_code = 600700

first_name_inp = driver.find_element(By.XPATH, '//*[@id="first-name"]')
first_name_inp.send_keys(first_name)

last_name_inp = driver.find_element(By.XPATH, '//*[@id="last-name"]')
last_name_inp.send_keys(last_name)

post_code_inp = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
post_code_inp.send_keys(str(post_code))

continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
continue_button.click()
print('Checkout Continue')
