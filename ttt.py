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

"""Selection of goods"""
# lokator = '(//div[@class="inventory_item_name "])'
# lokator_id = '[1]'
# lokator_full = lokator + lokator_id

products = driver.find_element(By.XPATH, '//div[@class="inventory_item_name "]')
products_value = products.text
# for f in products_value:
print(products_value)

a = products
while a > 1:
    a = a + 1
    print(a)




# def input_good_number():
    # product_add = str(input('Укажите наименование товара '))

#
# """Basket"""
# basket = driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
# basket.click()
# # print('Click Basket')
#
# basket_page = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')
# value_basket_page = basket_page.text
# # print('Test basket OK  name page: ' + value_basket_page)