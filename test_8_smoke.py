import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# запуск тестов без открытия браузера
options.add_argument('--headless')
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

# Screen Autorization
now_date = datetime.datetime.now().strftime("%H.%M.%S-%Y.%m.%d")
name_screenshot = 'Autorization Screenshot ' + now_date + '.png'
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
print('Test basket OK  name page: ' + value_basket_page)

# Screen Basket
now_date = datetime.datetime.now().strftime("%H.%M.%S-%Y.%m.%d")
name_screenshot = 'Basket Screenshot ' + now_date + '.png'
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
name_screenshot = 'Checkout page Screenshot ' + now_date + '.png'
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

"""Checkout: Overview"""
# Overview page
overview_page = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
value_overview_page = overview_page.text
print(value_overview_page)

# Screen Overview
now_date = datetime.datetime.now().strftime("%H.%M.%S-%Y.%m.%d")
name_screenshot = 'Overview Screenshot ' + now_date + '.png'
driver.save_screenshot(f'screenshots/{name_screenshot}')
print(name_screenshot)

# Checkout goods
goods_1 = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
value_goods_1 = goods_1.text
print('goods 1 name: ' + value_goods_1)

goods_1_price = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div['
                                              '2]/div')
value_goods_1_price = goods_1_price.text
print('price 1: ' + value_goods_1_price)

goods_2 = driver.find_element(By.XPATH, '//*[@id="item_0_title_link"]/div')
value_goods_2 = goods_2.text
print('goods 2 name: ' + value_goods_2)

goods_2_price = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[4]/div[2]/div['
                                              '2]/div')
value_goods_2_price = goods_2_price.text
print('price 2: ' + value_goods_2_price)

# Assert price
assert value_goods_1_price == value_price_goods_1
assert value_goods_2_price == value_price_goods_2
print('Assert price OK')

# Test sum goods
num_price_1 = value_goods_1_price
num_price_1 = num_price_1[1:]

num_price_2 = value_goods_2_price
num_price_2 = num_price_2[1:]

# Test total price & Tax
test_total_price = float(num_price_1) + float(num_price_2)

item_total = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[6]')
value_item_total = item_total.text
value_item_total = float(value_item_total[13:])

assert test_total_price == value_item_total
print('Test assert total price OK')

tax_var = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[7]')
value_tax_var = tax_var.text
value_tax_var = float(value_tax_var[6:])

# Total
total_var = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[8]')
value_total_var = total_var.text
value_total_var = float(value_total_var[8:])

assert test_total_price + value_tax_var == value_total_var
print('Test Total price OK')

"""Complete"""
finish_button = driver.find_element(By.XPATH, '//*[@id="finish"]')
finish_button.click()
print('Finish button click')

complete_var = driver.find_element(By.XPATH, '//*[@id="checkout_complete_container"]/h2')
complete_var = complete_var.text
print(complete_var)

# Screen Complete
now_date = datetime.datetime.now().strftime("%H.%M.%S-%Y.%m.%d")
name_screenshot = 'Complete Screenshot ' + now_date + '.png'
driver.save_screenshot(f'screenshots/{name_screenshot}')
print(name_screenshot)
