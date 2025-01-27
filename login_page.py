import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.login_window_locator = (By.CLASS_NAME, 'login_logo')
        self.user_name_locator = (By.XPATH, '//input[@id="user-name"]')
        self.user_password_locator = (By.XPATH, '//input[@id="password"]')
        self.login_button_locator = (By.XPATH, '//input[@id="login-button"]')

    def wait_elements(self, locator, timeout=30):
        """Метод для переиспользования ожидания"""
        wt_el = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        return wt_el

    def authorization(self, login_name, password):
        """Метод авторизации"""
        login_window = self.wait_elements(self.login_window_locator).text
        assert login_window == 'Swag Labs'

        user_name = self.wait_elements(self.user_name_locator)
        user_name.clear()
        user_name.send_keys(login_name)
        time.sleep(1)
        user_password = self.wait_elements(self.user_password_locator)
        user_password.clear()
        user_password.send_keys(password)
        time.sleep(1)
        # name_screenshot = 'Screenshot ' + ' .png'
        # self.browser.save_screenshot(f'screenshots/{name_screenshot}')
        button_login = self.wait_elements(self.login_button_locator)
        button_login.click()
        time.sleep(1)
