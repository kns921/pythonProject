from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from login_page import LoginPage


class TestT:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        # запуск тестов без открытия браузера
        # self.options.add_argument('--headless')
        self.service = Service()
        self.base_url = 'https://www.saucedemo.com/'
        self.url_home = 'https://www.saucedemo.com/inventory.html'
        self.password = 'secret_sauce'
        self.users = [
            'standard_user',
            'locked_out_user',
            'problem_user',
            'performance_glitch_user',
            'error_user',
            'visual_user'
        ]

    def test_select_product(self):
        browser = webdriver.Chrome(options=self.options, service=self.service)
        browser.get(self.base_url)
        browser.maximize_window()

        """Autorization"""
        login = LoginPage(browser)

        for usr in self.users:
            # if usr ==
            login.authorization(login_name=usr, password=self.password)

            url_home = self.url_home
            get_url = browser.current_url
            assert url_home == get_url
            print(get_url)

            header_locator = (By.XPATH, '//*[@id="header_container"]/div[2]/span')
            text_product = WebDriverWait(browser, 30).until(EC.element_to_be_clickable(header_locator)).text
            assert text_product == 'Products'
            print('Login success')

            self.logout_button(browser)

    @staticmethod
    def logout_button(browser):
        burger_button_locator = (By.XPATH, '//button[@id="react-burger-menu-btn"]')
        logout_button_locator = (By.XPATH, '//a[@id="logout_sidebar_link"]')

        burger_button = WebDriverWait(browser, 30).until(EC.element_to_be_clickable(burger_button_locator))
        browser.execute_script("arguments[0].click();", burger_button)
        print('burger_button')
        lg_button = WebDriverWait(browser, 30).until(EC.element_to_be_clickable(logout_button_locator))
        lg_button.click()
        print('lg_button')


# test = TestT()
# browser_instance = test.test_select_product()
# test.logout_button(browser_instance)
test = TestT()
test.test_select_product()
