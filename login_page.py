from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def authorization(self, login_name, password):
        """Autorization"""
        login_window = (WebDriverWait(self.driver, 30).until
                        (EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[1]'))).text)
        assert login_window == 'Swag Labs'

        user_name = (WebDriverWait(self.driver, 30).until
                     (EC.element_to_be_clickable((By.XPATH, '//*[@id="user-name"]'))))
        user_name.send_keys(login_name)

        user_password = (WebDriverWait(self.driver, 30).until
                         (EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]'))))
        user_password.send_keys(password)

        button_login = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]')))
        button_login.click()
