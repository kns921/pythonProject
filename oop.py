from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestT:
    def test_select_product(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        g = Service()
        driver = webdriver.Chrome(options=options, service=g)
        bace_url = 'https://www.saucedemo.com/'
        driver.get(bace_url)
        driver.maximize_window()
        print('Start test')

        """Autorization"""
        login_window = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div'
                                                                                             '/div[1]'))).text
        assert login_window == 'Swag Labs'

        user_name = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="user-name"]')))
        user_name.send_keys('standard_user')

        user_password = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password"]')))
        user_password.send_keys('secret_sauce')

        button_login = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]')))
        button_login.click()

        url_home = 'https://www.saucedemo.com/inventory.html'
        get_url = driver.current_url
        print(get_url)
        assert url_home == get_url

        text_product = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*['
                                                                                             '@id="header_container'
                                                                                             '"]/div[2]/span'))).text
        assert text_product == 'Products'


test = TestT()
test.test_select_product()
