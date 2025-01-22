from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from login_page import LoginPage


class TestT:
    def test_select_product(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        # options.add_argument('--headless')
        g = Service()
        driver = webdriver.Chrome(options=options, service=g)
        bace_url = 'https://www.saucedemo.com/'
        driver.get(bace_url)
        driver.maximize_window()
        print('Start test')

        """Autorization"""
        login_standard_user = "standard_user"
        password_all = "secret_sauce"
        login = LoginPage(driver)
        login.authorization(login_standard_user, password_all)

        url_home = 'https://www.saucedemo.com/inventory.html'
        get_url = driver.current_url
        assert url_home == get_url
        print(get_url)

        text_product = (WebDriverWait(driver, 30).until
                        (EC.element_to_be_clickable((By.XPATH, '//*[@id="header_container"]/div[2]/span'))).text)
        assert text_product == 'Products'

        select_product = (WebDriverWait(driver, 30).until
                          (EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]'))))
        select_product.click()
        print('Click Button')

        basket_product = (WebDriverWait(driver, 30).until
                          (EC.element_to_be_clickable((By.XPATH, '//div[@id="shopping_cart_container"]'))))
        basket_product.click()
        print('Click basket')

        test_success = (WebDriverWait(driver, 30).until
                        (EC.element_to_be_clickable((By.XPATH, '//span[@class="title"]')))).text
        assert test_success == 'Your Cart'
        print('test success')


test = TestT()
test.test_select_product()
