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
login_window = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]').text
assert login_window == 'Swag Labs'

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

text_product = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span').text
assert text_product == 'Products'

"""Goods"""
products = driver.find_elements(By.XPATH, '//div[@class="inventory_item"]')


def search_product(index=0):
    if index < len(products):
        product = products[index]
        product_name = product.find_element(By.XPATH, './/div[@class="inventory_item_name "]').text
        product_price = product.find_element(By.XPATH, './/div[@class="inventory_item_price"]').text
        print(f"{index + 1}. {product_name} - {product_price}")
        search_product(index + 1)


print("Список доступных товаров: ")
search_product()

"""Selection of goods"""


def input_good_number():
    product_index = int(input("Укажите номер товара: ")) - 1
    if 0 <= product_index < len(products):
        product = products[product_index]
        product_name = product.find_element(By.XPATH, './/div[@class="inventory_item_name "]').text
        product_price = product.find_element(By.XPATH, './/div[@class="inventory_item_price"]').text
        product_button = product.find_element(By.XPATH, './/button')

        product_button.click()
        print(f"В корзину добавлен товар: {product_name} - {product_price}")
    else:
        print("Ошибка! Вы выбрали некорректный номер товара.")
        input_good_number()


input_good_number()

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
post_code = input('Укажите Ваш почтовый индекс:')

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
overview_page = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span').text
# print(overview_page)

# Checkout goods
goods = driver.find_element(By.XPATH, '//*[@class="inventory_item_name"]').text
# print('goods name: ' + goods)

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


def fin():
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
        fin()


fin()
