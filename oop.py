from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from login_page import LoginPage


class TestMall:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        # self.options.add_argument('--headless')   # запуск тестов без открытия браузера
        self.service = Service()
        self.base_url = 'https://www.saucedemo.com/'
        self.url_home = 'https://www.saucedemo.com/inventory.html'
        self.header_locator = (By.XPATH, '//*[@id="header_container"]/div[2]/span')
        self.error_value_locator = (By.XPATH, '//h3[@data-test="error"]')
        self.error_button_locator = (By.XPATH, '//button[@class="error-button"]')
        self.burger_button_locator = (By.XPATH, '//button[@id="react-burger-menu-btn"]')
        self.logout_button_locator = (By.XPATH, '//a[@id="logout_sidebar_link"]')
        self.password = 'secret_sauce'
        self.users = [
            'standard_user',
            'locked_out_user',
            'problem_user',
            'performance_glitch_user',
            'error_user',
            'visual_user'
        ]

    def test_mall(self):
        """Метод тестирования авторизации"""
        driver = webdriver.Chrome(options=self.options, service=self.service)
        driver.get(self.base_url)  # открытие страницы
        driver.maximize_window()
        """Авторизация"""
        login = LoginPage(driver)
        """Перебор пользователей циклом"""
        for usr in self.users:
            login.authorization(login_name=usr, password=self.password)
            try:
                url_home = self.url_home
                get_url = driver.current_url
                assert url_home == get_url
                print(get_url)

                text_product = login.wait_elements(self.header_locator).text
                assert text_product == 'Products'
                print(f'Login Success: {usr}')
                # выход из системы
                self.logout_button(driver)
            except AssertionError:
                """Обработка исключения с заблокированным пользователем"""
                error_value = login.wait_elements(self.error_value_locator).text
                error_button = login.wait_elements(self.error_button_locator)
                print(f'Error!: {error_value}')
                error_button.click()
        driver.quit()
        print('Exit browser')

    def logout_button(self, driver):
        """Метод выхода из системы"""
        login = LoginPage(driver)

        burger_button = login.wait_elements(self.burger_button_locator)
        burger_button.click()
        print('Click Burger-button')
        lg_button = login.wait_elements(self.logout_button_locator)
        lg_button.click()
        print('Logout Success')


test = TestMall()
test.test_mall()
