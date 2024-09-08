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

# print ("Приветствую тебя в нашем интернет магазине")
# print ("Выбери один из следующих товаров и укажи его номер:")
# product = input()
# print(product)

class Goods():
    def __init__(self, number, name):
        self.number = number
        self.name = name
        # self.price = price
        # self.button = button

class Backpack(Goods):
    def __init__(self, number, name):
        self.number = 1
        self.name = name
        # self.price = price
        # self.button = button
#
#     def get_name(self):
#         name_discription = driver.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div').text
#
#
# backpack = Backpack()
# Backpack.get_name()
#
# print(backpack)
