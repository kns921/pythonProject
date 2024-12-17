from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

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
assert value_login_window == 'Swag Labs'

user_name = driver.find_element(By.XPATH, '//*[@id="user-name"]')
user_name.send_keys('standard_user')

user_password = driver.find_element(By.XPATH, '//*[@id="password"]')
user_password.send_keys('secret_sauce')

button_login = driver.find_element(By.XPATH, '//*[@id="login-button"]')
button_login.click()

url_home = 'https://www.saucedemo.com/inventory.html'
get_url = driver.current_url
print(get_url)
assert url_home == get_url

text_product = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
value_text_product = text_product.text
assert value_text_product == 'Products'

"""Goods"""


class Cart:
    def __init__(self, number, name, price):
        self.number = number
        self.name = name
        self.price = price

    def description(self):
        description = str(self.number) + str(self.name) + str(self.price)
        return description


backpack = Cart(1, ' - Sauce Labs Backpack. ', '$29.99')
light = Cart(2, ' - Sauce Labs Bike Light. ', '$9.99')
shirt = Cart(3, ' - Sauce Labs Bolt T-Shirt. ', '$15.99')
jacket = Cart(4, ' - Sauce Labs Fleece Jacket. ', '$49.99')
onesie = Cart(5, ' - Sauce Labs Onesie. ', '$7.99')
allTheThings = Cart(6, ' - Test.allTheThings() T-Shirt (Red). ', '$15.99')

print("Приветствую тебя в нашем интернет магазине")
print("Выбери один из следующих товаров и укажи его номер:")
print(backpack.description())
print(light.description())
print(shirt.description())
print(jacket.description())
print(onesie.description())
print(allTheThings.description())

"""Selection of goods"""
product_add = int(input('Укажите номер товара '))
if product_add == 1:
    product_var = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    product_var.click()
    print('В корзину добавлен товар: ' + backpack.description())
elif product_add == 2:
    product_var = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
    product_var.click()
    print('В корзину добавлен товар: ' + light.description())
elif product_add == 3:
    product_var = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
    product_var.click()
    print('В корзину добавлен товар: ' + shirt.description())
elif product_add == 4:
    product_var = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')
    product_var.click()
    print('В корзину добавлен товар: ' + jacket.description())
elif product_add == 5:
    product_var = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-onesie"]')
    product_var.click()
    print('В корзину добавлен товар: ' + onesie.description())
elif product_add == 6:
    product_var = driver.find_element(By.XPATH, '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')
    product_var.click()
    print('В корзину добавлен товар: ' + allTheThings.description())
else:
    print('Ошибка! Выберите другое значение.')

"""Basket"""
basket = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
basket.click()
# print('Click Basket')

basket_page = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
value_basket_page = basket_page.text
# print('Test basket OK  name page: ' + value_basket_page)

"""Checkout"""
checkout = driver.find_element(By.XPATH, '//*[@id="checkout"]')
checkout.click()
# print('Click Checkout')

# Checkout page
checkout_page = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
value_checkout_page = checkout_page.text
# print(value_checkout_page)

# Input Your Information
print('Продолжаем оформление введите свои данные:')

first_name = input('Укажите Ваше Имя:')
last_name = input('Укажите Вашу Фамилию:')
post_code = int(input('Укажите Ваш почтовый индекс:'))

first_name_inp = driver.find_element(By.XPATH, '//*[@id="first-name"]')
first_name_inp.send_keys(first_name)

last_name_inp = driver.find_element(By.XPATH, '//*[@id="last-name"]')
last_name_inp.send_keys(last_name)

post_code_inp = driver.find_element(By.XPATH, '//*[@id="postal-code"]')
post_code_inp.send_keys(str(post_code))

continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
continue_button.click()
# print('Checkout Continue')

"""!!! Checkout: Overview"""
# Overview page
overview_page = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
value_overview_page = overview_page.text
# print(value_overview_page)

# Checkout goods
goods = driver.find_element(By.XPATH, '//*[@class="inventory_item_name"]')
value_goods = goods.text
# print('goods name: ' + value_goods)

goods_price = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[1]/div[3]/div[2]/div['
                                            '2]/div')
value_goods_price = goods_price.text
value_goods_price = str(value_goods_price[1:])
# print('price: ' + value_goods_price)

price_item_total = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[6]')
value_price_item_total = price_item_total.text
value_price_item_total = str(value_price_item_total[13:])
print('Цена товара: $:' + value_price_item_total)

# Assert price
assert float(value_goods_price) == float(value_price_item_total)
# print('Test assert total price OK')

# Test total price & Tax
tax_sum = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[7]')
value_tax_sum = tax_sum.text
value_tax_sum = str(value_tax_sum[6:])
print('Налог: $' + value_tax_sum)

price_total_tax = driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[8]')
value_price_total_tax = price_total_tax.text
value_price_total_tax = str(value_price_total_tax[8:])
print('Итоговая стоимость с учетом налогов: $' + value_price_total_tax)

# Assert Tax price + Total
value_price_total_tax = float(value_price_total_tax)
value_tax_sum = float(value_tax_sum)
value_price_item_total = float(value_price_item_total)

act = value_price_item_total + value_tax_sum
act = round(act, 2)
# print(act)

assert value_price_total_tax == act
# print('Assert Total OK')

# Finish
print('Завершение оформления!')
print('Выберите 1, если готовы к завершению')
print('Выберите 0, если хотите отменить заказ')

finish = int(input('Укажите 1 или 0: '))
if finish == 1:
    finish_var = driver.find_element(By.XPATH, '//*[@id="finish"]')
    finish_var.click()
    print('Спасибо за заказ!')

elif finish == 0:
    finish_var_cancel = driver.find_element(By.XPATH, '//*[@id="cancel"]')
    finish_var_cancel.click()
    print('Заказ отменен')
else:
    print('Ошибка! Выберите другое значение.')
